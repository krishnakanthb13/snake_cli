import curses

# Color pair IDs
COLOR_GREEN = 1
COLOR_RED = 2
COLOR_YELLOW = 3
COLOR_BLUE = 4
COLOR_MAGENTA = 5
COLOR_CYAN = 6
COLOR_WHITE = 7

def init_colors():
    if not curses.has_colors():
        return False
        
    curses.start_color()
    curses.use_default_colors()
    
    # Simple color pairs
    curses.init_pair(COLOR_GREEN, curses.COLOR_GREEN, -1)
    curses.init_pair(COLOR_RED, curses.COLOR_RED, -1)
    curses.init_pair(COLOR_YELLOW, curses.COLOR_YELLOW, -1)
    curses.init_pair(COLOR_BLUE, curses.COLOR_BLUE, -1)
    curses.init_pair(COLOR_MAGENTA, curses.COLOR_MAGENTA, -1)
    curses.init_pair(COLOR_CYAN, curses.COLOR_CYAN, -1)
    curses.init_pair(COLOR_WHITE, curses.COLOR_WHITE, -1)
    
    return True

def get_color_pair(color_name):
    mapping = {
        "GREEN": COLOR_GREEN,
        "RED": COLOR_RED,
        "YELLOW": COLOR_YELLOW,
        "BLUE": COLOR_BLUE,
        "MAGENTA": COLOR_MAGENTA,
        "CYAN": COLOR_CYAN,
        "WHITE": COLOR_WHITE
    }
    return curses.color_pair(mapping.get(color_name.upper(), COLOR_WHITE))

def get_random_color_pair():
    import random
    return curses.color_pair(random.randint(1, 7))
