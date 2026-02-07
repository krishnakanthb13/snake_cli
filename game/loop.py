import curses
import time
from game.snake import Snake
from game.food import Food
from game.state import GameState
from game.obstacles import Obstacles
from ui.themes import THEMES

class GameController:
    def __init__(self, renderer, config_manager, stats_manager, screen_manager):
        self.renderer = renderer
        self.config = config_manager
        self.stats = stats_manager
        self.screens = screen_manager
        self.state = GameState(self.config)
        self.running = False

    def run(self):
        while True:
            action = self.screens.show_start_page()
            if action == "play":
                self.start_game()
            elif action == "quit":
                break

    def start_game(self):
        self.state.reset()
        max_y, max_x = self.renderer.update_bounds()
        
        # Apply theme
        theme_name = self.config.get("theme", "Classic")
        if theme_name in THEMES:
            theme = THEMES[theme_name]
            self.config.set("snake_color", theme["snake"])
            
        # Initialize snake in center
        start_pos = (max_y // 2, max_x // 2)
        self.snake = Snake(start_pos)
        self.food = Food((max_y, max_x), self.config)
        
        # Initialize obstacles
        self.obstacles = Obstacles((max_y, max_x))
        if self.config.get("obstacles_on"):
            self.obstacles.spawn(5, occupied_positions=self.snake.body + [self.food.pos])
        
        self.running = True
        last_move_time = time.time()
        
        while self.running:
            # Update frequency based on speed
            speed = self.config.get("speed", 10)
            delay = 1.0 / speed
            
            # Handle input
            key = self.renderer.get_input()
            self.handle_input(key)
            
            # Game logic update
            current_time = time.time()
            if current_time - last_move_time >= delay:
                self.update()
                last_move_time = current_time
                
            # Render
            self.draw()
            
            if self.state.game_over:
                self.running = False
                action = self.screens.show_end_page(self.state)
                if action == "restart":
                    self.start_game()
                elif action == "quit":
                    exit()
                return # Back to main loop (start page)

    def handle_input(self, key):
        if key == -1: return
        
        # Directions
        if key in [curses.KEY_UP, ord('w'), ord('W')]:
            self.snake.change_direction((-1, 0))
        elif key in [curses.KEY_DOWN, ord('s'), ord('S')]:
            # If WASD is used, 's' is down. 
            # To allow both, we'll check if it's the KEY_DOWN specifically or 's'
            # If it's 's', we'll only treat it as DOWN for now to avoid accidental stats opening
            self.snake.change_direction((1, 0))
        elif key in [curses.KEY_LEFT, ord('a'), ord('A')]:
            self.snake.change_direction((0, -1))
        elif key in [curses.KEY_RIGHT, ord('d'), ord('D')]:
            self.snake.change_direction((0, 1))
            
        # Overlays
        elif key in [ord('p'), ord('P')]:
            if self.screens.show_pause_overlay() == "quit":
                self.running = False
                self.state.game_over = True
        elif key in [ord('i'), ord('I')]: # Use 'I' for Info/Stats to avoid conflict with 'S' (Down)
            self.screens.show_stats_overlay(self.state)
        elif key in [ord('l'), ord('L')]:
            self.screens.show_leaderboard()
        elif key in [ord('q'), ord('Q')]:
            self.running = False

    def update(self):
        # Move snake
        new_head = self.snake.move()
        self.state.snake_length = len(self.snake.body)
        
        # Collision check
        bounds = (self.renderer.max_y, self.renderer.max_x) if self.config.get("walls_on") else None
        if self.snake.check_collision(bounds=bounds):
            self.state.game_over = True
            return

        if self.config.get("obstacles_on") and self.obstacles.check_collision(self.snake.body[0]):
            self.state.game_over = True
            return
            
        if not self.config.get("walls_on"):
            self.snake.wrap((self.renderer.max_y, self.renderer.max_x))
            
        # Food consumption
        if self.snake.body[0] == self.food.pos:
            points = self.food.get_points()
            food_type = self.food.type
            self.state.update_score(points, food_type)
            
            # Growth strategy: big food gives more growth?
            growth = 2 if food_type == "big" else 1
            self.snake.grow(growth)
            
            self.food.spawn(occupied_positions=self.snake.body)

    def draw(self):
        self.renderer.clear()
        if self.config.get("walls_on"):
            self.renderer.draw_border()
            
        # Draw obstacles
        if self.config.get("obstacles_on"):
            for y, x in self.obstacles.points:
                try:
                    self.renderer.stdscr.addch(y, x, "█", curses.color_pair(7)) # White blocks
                except: pass
                
        self.renderer.draw_food(self.food)
        self.renderer.draw_snake(self.snake, self.config)
        
        # Top HUD
        hud_text = f" Score: {self.state.score} | Length: {len(self.snake.body)} | Time: {self.state.get_survival_time()}s "
        self.renderer.draw_text(0, 2, hud_text, curses.A_REVERSE)
        
        self.renderer.refresh()
