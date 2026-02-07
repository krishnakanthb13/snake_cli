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
        self.max_y, self.physical_x = self.stdscr.getmaxyx()
        self.max_x = self.physical_x // 2

    def clear(self):
        self.stdscr.erase()

    def refresh(self):
        self.stdscr.refresh()

    def draw_snake(self, snake, config):
        mode = config.get("snake_mode", "same_color")
        default_color = config.get("snake_color", "GREEN")
        
        for i, (y, x) in enumerate(snake.body):
            if y >= self.max_y or x >= self.max_x: continue # Safety check
            
            # Application of "Mode" settings for shape
            if mode in ["mixed_shape", "mixed_both"]:
                mixed_shapes = ["█", "■", "●", "@", "#", "░"]
                shape = mixed_shapes[i % len(mixed_shapes)]
            else:
                # Use the symbol stored in the snake for this segment
                shape = snake.symbols[i] if i < len(snake.symbols) else "█"
            
            # Default to the segment's captured color
            segment_color = snake.segment_colors[i] if i < len(snake.segment_colors) else default_color
            attr = get_color_pair(segment_color)
            
            # Application of "Mode" settings for color
            if mode in ["mixed_color", "mixed_both"]:
                if len(snake.colors) <= i:
                    snake.colors.append(get_random_color_pair())
                attr = snake.colors[i]
                
            try:
                # Use two characters for horizontal width to fix vertical speed aspect ratio
                self.stdscr.addstr(y, x * 2, shape * 2, attr)
            except curses.error:
                pass

    def draw_food(self, food):
        y, x = food.pos
        shape, color = food.get_visuals()
        try:
            # Food also needs to be doubled or at least positioned correctly
            # We'll use two characters to match the snake's width
            self.stdscr.addstr(y, x * 2, shape * 2, get_color_pair(color))
        except curses.error:
            pass

    def draw_obstacle(self, y, x):
        try:
            self.stdscr.addstr(y, x * 2, "██", curses.color_pair(7))
        except curses.error:
            pass

    def draw_text(self, y, x, text, attr=0, center=False):
        if center:
            x = (self.physical_x - len(text)) // 2
        try:
            self.stdscr.addstr(y, x, text, attr)
        except curses.error:
            pass

    def draw_border(self):
        # We need to draw the border at the edge of the LOGICAL grid
        # self.max_x * 2 is the physical width. 
        # But indices are 0 to (max_x*2)-1.
        w = self.max_x * 2
        h = self.max_y
        
        # Draw top and bottom
        for x in range(w):
            try:
                self.stdscr.addch(0, x, curses.ACS_HLINE)
                self.stdscr.addch(h-1, x, curses.ACS_HLINE)
            except curses.error: pass
            
        # Draw sides
        for y in range(h):
            try:
                self.stdscr.addch(y, 0, curses.ACS_VLINE)
                self.stdscr.addch(y, w-1, curses.ACS_VLINE)
            except curses.error: pass
            
        # Draw corners
        try:
            self.stdscr.addch(0, 0, curses.ACS_ULCORNER)
            self.stdscr.addch(0, w-1, curses.ACS_URCORNER)
            self.stdscr.addch(h-1, 0, curses.ACS_LLCORNER)
            self.stdscr.addch(h-1, w-1, curses.ACS_LRCORNER)
        except curses.error: pass

    def get_input(self):
        try:
            return self.stdscr.getch()
        except:
            return -1

    def update_bounds(self):
        self.max_y, self.physical_x = self.stdscr.getmaxyx()
        self.max_x = self.physical_x // 2
        return self.max_y, self.max_x
