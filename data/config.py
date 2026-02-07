import json
import os

DEFAULT_CONFIG = {
    "speed": 10,
    "walls_on": True,
    "obstacles_on": False,
    "theme": "Classic",
    "snake_shape": "█",
    "snake_color": "GREEN",
    "snake_mode": "same_color",  # same_color, same_shape, mixed_color, mixed_shape, mixed_both
    "food_color": "RANDOM",  # RANDOM or specific color
    "big_food_chance": 10,  # Percentage chance (10 = 10%)
    "food_settings": {
        "small": {"shape": "•", "color": "YELLOW", "point": 10},
        "big": {"shape": "★", "color": "RED", "point": 50, "chance": 0.1}
    },
    "keybindings": {
        "up": ["KEY_UP", "w", "W"],
        "down": ["KEY_DOWN", "s", "S"],
        "left": ["KEY_LEFT", "a", "A"],
        "right": ["KEY_RIGHT", "d", "D"],
        "pause": ["p", "P"],
        "stats": ["i", "I"],
        "leaderboard": ["l", "L"],
        "quit": ["q", "Q"]
    }
}

class ConfigManager:
    def __init__(self, config_file="config.json"):
        self.config_file = config_file
        self.settings = DEFAULT_CONFIG.copy()
        self.load()

    def load(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    user_settings = json.load(f)
                    self.settings.update(user_settings)
            except Exception as e:
                print(f"Error loading config: {e}")

    def save(self):
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.settings, f, indent=4, ensure_ascii=False)
        except Exception as e:
            print(f"Error saving config: {e}")

    def get(self, key, default=None):
        return self.settings.get(key, default)

    def set(self, key, value):
        self.settings[key] = value
        self.save()
