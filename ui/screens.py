import curses
import time

class ScreenManager:
    def __init__(self, renderer, config_manager, stats_manager, leaderboard_manager):
        self.renderer = renderer
        self.config_manager = config_manager
        self.stats_manager = stats_manager
        self.leaderboard_manager = leaderboard_manager

    def show_start_page(self):
        self.renderer.clear()
        self.renderer.stdscr.nodelay(False) # Wait for input
        
        menu_items = [
            ("Speed", "speed", [5, 10, 15, 20]),
            ("Walls", "walls_on", [True, False]),
            ("Obstacles", "obstacles_on", [True, False]),
            ("Theme", "theme", ["Classic", "Neon", "Retro", "Matrix"]),
            ("Snake Shape", "snake_shape", ["█", "■", "●", "@", "#"]),
            ("Snake Color", "snake_color", ["GREEN", "BLUE", "RED", "YELLOW", "WHITE"]),
            ("Mode", "snake_mode", ["same_color", "mixed_color", "mixed_shape", "mixed_both"]),
            ("Start Game", "start", None),
            ("View Leaderboard", "leaderboard", None),
            ("Quit", "exit", None)
        ]
        
        current_selection = 0
        
        while True:
            self.renderer.clear()
            self.renderer.draw_text(2, 0, "S N A K E   C L I", curses.A_BOLD, center=True)
            self.renderer.draw_text(3, 0, "=================", 0, center=True)
            
            for i, item in enumerate(menu_items):
                label, key, options = item
                text = f"{label}"
                if options:
                    current_val = self.config_manager.get(key)
                    text = f"{label}: [ {current_val} ]"
                
                attr = curses.A_REVERSE if i == current_selection else 0
                self.renderer.draw_text(6 + i, 0, text, attr, center=True)
            
            self.renderer.draw_text(self.renderer.max_y - 2, 0, "Use Arrows to Navigate | Space/Enter to Select/Toggle", curses.A_DIM, center=True)
            self.renderer.refresh()
            
            key = self.renderer.get_input()
            if key in [curses.KEY_UP, ord('w')]:
                current_selection = (current_selection - 1) % len(menu_items)
            elif key in [curses.KEY_DOWN, ord('s')]:
                current_selection = (current_selection + 1) % len(menu_items)
            elif key in [10, 13, ord(' ')]: # Enter or Space
                label, key_name, options = menu_items[current_selection]
                
                if key_name == "start":
                    self.renderer.stdscr.nodelay(True)
                    return "play"
                elif key_name == "leaderboard":
                    self.show_leaderboard()
                elif key_name == "exit":
                    return "quit"
                elif options:
                    current_val = self.config_manager.get(key_name)
                    new_idx = (options.index(current_val) + 1) % len(options)
                    self.config_manager.set(key_name, options[new_idx])
            elif key == ord('q'):
                return "quit"

    def show_pause_overlay(self):
        y, x = self.renderer.max_y // 2, self.renderer.max_x // 2
        self.renderer.draw_text(y - 1, 0, " P A U S E D ", curses.A_REVERSE, center=True)
        self.renderer.draw_text(y + 1, 0, "Press 'P' to Resume or 'Q' to Quit", 0, center=True)
        self.renderer.refresh()
        
        self.renderer.stdscr.nodelay(False)
        while True:
            key = self.renderer.get_input()
            if key in [ord('p'), ord('P')]:
                self.renderer.stdscr.nodelay(True)
                return "resume"
            if key in [ord('q'), ord('Q')]:
                return "quit"

    def show_end_page(self, state):
        self.renderer.clear()
        self.renderer.stdscr.nodelay(False)
        
        # Capture player name
        self.renderer.draw_text(5, 0, "G A M E   O V E R", curses.A_BOLD, center=True)
        self.renderer.draw_text(7, 0, f"Score: {state.score}", 0, center=True)
        self.renderer.draw_text(8, 0, f"Time: {state.get_survival_time()}s", 0, center=True)
        
        self.renderer.draw_text(11, 0, "Enter your name for leaderboard:", 0, center=True)
        self.renderer.refresh()
        
        curses.echo()
        curses.curs_set(1)
        name_input = self.renderer.stdscr.getstr(12, (self.renderer.max_x - 10) // 2, 15).decode('utf-8')
        curses.noecho()
        curses.curs_set(0)
        
        state.player_name = name_input if name_input else "Player"
        summary = state.get_summary()
        self.stats_manager.log_session(summary)
        
        while True:
            self.renderer.clear()
            self.renderer.draw_text(5, 0, "G A M E   O V E R", curses.A_BOLD, center=True)
            self.renderer.draw_text(7, 0, f"Final Score: {state.score}", 0, center=True)
            self.renderer.draw_text(8, 0, f"Survival Time: {state.get_survival_time()}s", 0, center=True)
            self.renderer.draw_text(10, 0, f"Small Food: {state.food_eaten['small']} | Big Food: {state.food_eaten['big']}", 0, center=True)
            
            self.renderer.draw_text(13, 0, "[ R ] Play Again", 0, center=True)
            self.renderer.draw_text(14, 0, "[ M ] Main Menu", 0, center=True)
            self.renderer.draw_text(15, 0, "[ Q ] Exit", 0, center=True)
            self.renderer.refresh()
            
            key = self.renderer.get_input()
            if key in [ord('r'), ord('R')]:
                self.renderer.stdscr.nodelay(True)
                return "restart"
            if key in [ord('m'), ord('M')]:
                return "menu"
            if key in [ord('q'), ord('Q')]:
                return "quit"

    def show_leaderboard(self):
        self.renderer.clear()
        self.renderer.stdscr.nodelay(False)
        
        self.renderer.draw_text(2, 0, "L E A D E R B O A R D", curses.A_BOLD, center=True)
        self.renderer.draw_text(3, 0, "=====================", 0, center=True)
        
        page = self.leaderboard_manager.format_leaderboard()
        for i, line in enumerate(page.split("\n")):
            self.renderer.draw_text(5 + i, 0, line, 0, center=True)
            
        self.renderer.draw_text(self.renderer.max_y - 2, 0, "Press any key to return...", curses.A_DIM, center=True)
        self.renderer.refresh()
        self.renderer.get_input()
        self.renderer.stdscr.nodelay(True)

    def show_stats_overlay(self, state):
        # Semi-transparent style (just an overlay)
        h, w = 10, 40
        y, x = (self.renderer.max_y - h) // 2, (self.renderer.max_x - w) // 2
        
        # Simple box using characters
        self.renderer.draw_text(y, x, "+" + "-"*(w-2) + "+")
        for i in range(1, h-1):
            self.renderer.draw_text(y+i, x, "|" + " "*(w-2) + "|")
        self.renderer.draw_text(y+h-1, x, "+" + "-"*(w-2) + "+")
        
        self.renderer.draw_text(y+1, x+2, "C U R R E N T   S T A T S", curses.A_BOLD)
        self.renderer.draw_text(y+3, x+2, f"Score: {state.score}")
        self.renderer.draw_text(y+4, x+2, f"Time:  {state.get_survival_time()}s")
        self.renderer.draw_text(y+5, x+2, f"Length: {state.snake_length}")
        self.renderer.draw_text(y+6, x+2, f"Small: {state.food_eaten['small']} | Big: {state.food_eaten['big']}")
        
        self.renderer.draw_text(y+h-2, x+2, "Press any key to close", curses.A_DIM)
        self.renderer.refresh()
        
        self.renderer.stdscr.nodelay(False)
        self.renderer.get_input()
        self.renderer.stdscr.nodelay(True)
