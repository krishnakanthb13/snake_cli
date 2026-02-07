import curses
import sys
from ui.renderer import Renderer
from ui.colors import init_colors
from ui.screens import ScreenManager
from game.loop import GameController
from data.config import ConfigManager
from data.stats import StatsManager
from data.leaderboard import LeaderboardManager

def main(stdscr):
    # Initialize managers
    config_manager = ConfigManager()
    stats_manager = StatsManager()
    leaderboard_manager = LeaderboardManager(stats_manager)
    
    # Initialize colors
    init_colors()
    
    # Initialize renderer
    renderer = Renderer(stdscr)
    
    # Initialize screen manager
    screen_manager = ScreenManager(renderer, config_manager, stats_manager, leaderboard_manager)
    
    # Initialize game controller
    controller = GameController(renderer, config_manager, stats_manager, screen_manager)
    
    # Run the game
    try:
        controller.run()
    except KeyboardInterrupt:
        pass
    except Exception as e:
        # On error, we want to clean up curses before printing the error
        raise e

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except Exception as e:
        print(f"\nGame crashed: {e}")
        sys.exit(1)
