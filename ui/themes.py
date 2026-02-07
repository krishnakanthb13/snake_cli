from ui.colors import get_color_pair

THEMES = {
    "Classic": {
        "snake": "GREEN",
        "food": "RED",
        "bg": "WHITE",
        "wall": "WHITE"
    },
    "Neon": {
        "snake": "CYAN",
        "food": "MAGENTA",
        "bg": "BLUE",
        "wall": "BLUE"
    },
    "Retro": {
        "snake": "YELLOW",
        "food": "GREEN",
        "bg": "WHITE",
        "wall": "WHITE"
    },
    "Matrix": {
        "snake": "GREEN",
        "food": "WHITE",
        "bg": "GREEN",
        "wall": "GREEN"
    }
}

class ThemeManager:
    def __init__(self, config_manager):
        self.config = config_manager
        self.current_theme = "Classic"

    def apply_theme(self, theme_name):
        if theme_name in THEMES:
            self.current_theme = theme_name
            # Update config settings
            theme = THEMES[theme_name]
            self.config.set("snake_color", theme["snake"])
            # We can expand this to update food settings etc.
            
    def get_theme_names(self):
        return list(THEMES.keys())
