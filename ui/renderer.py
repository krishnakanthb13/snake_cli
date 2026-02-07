import curses
from ui.colors import get_color_pair, get_random_color_pair

class Renderer:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        # Hide cursor
        curses.curs_set(0)
        # Enable non-blocking input for game loop
        self.stdscr.nodelay(True)
        # Enable keypad for arrow keys
        self.stdscr.keypad(True)
        self.max_y, self.max_x = self.stdscr.getmaxyx()

    def clear(self):
        self.stdscr.erase()

    def refresh(self):
        self.stdscr.refresh()

    def draw_snake(self, snake, config):
        mode = config.get("snake_mode", "same_color")
        default_shape = config.get("snake_shape", "█")
        default_color = config.get("snake_color", "GREEN")
        
        for i, (y, x) in enumerate(snake.body):
            if y >= self.max_y or x >= self.max_x: continue # Safety check
            
            shape = default_shape
            attr = get_color_pair(default_color)
            
            if mode == "mixed_color":
                if len(snake.colors) <= i:
                    snake.colors.append(get_random_color_pair())
                attr = snake.colors[i]
            elif mode == "mixed_shape":
                mixed_shapes = ["█", "■", "●", "@", "#", "░"]
                if len(snake.shapes) <= i:
                    snake.shapes.append(mixed_shapes[i % len(mixed_shapes)])
                shape = snake.shapes[i]
            elif mode == "mixed_both":
                mixed_shapes = ["█", "■", "●", "@", "#", "░"]
                if len(snake.colors) <= i:
                    snake.colors.append(get_random_color_pair())
                if len(snake.shapes) <= i:
                    snake.shapes.append(mixed_shapes[i % len(mixed_shapes)])
                attr = snake.colors[i]
                shape = snake.shapes[i]
                
            try:
                self.stdscr.addch(y, x, shape, attr)
            except curses.error:
                pass

    def draw_food(self, food):
        y, x = food.pos
        shape, color = food.get_visuals()
        try:
            self.stdscr.addch(y, x, shape, get_color_pair(color))
        except curses.error:
            pass

    def draw_text(self, y, x, text, attr=0, center=False):
        if center:
            x = (self.max_x - len(text)) // 2
        try:
            self.stdscr.addstr(y, x, text, attr)
        except curses.error:
            pass

    def draw_border(self):
        self.stdscr.border()

    def get_input(self):
        try:
            return self.stdscr.getch()
        except:
            return -1

    def update_bounds(self):
        self.max_y, self.max_x = self.stdscr.getmaxyx()
        return self.max_y, self.max_x
