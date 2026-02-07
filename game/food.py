import random

class Food:
    def __init__(self, bounds, config):
        self.bounds = bounds
        self.config = config
        self.pos = (0, 0)
        self.type = "small" # "small" or "big"
        self.spawn()

    def spawn(self, occupied_positions=None):
        max_y, max_x = self.bounds
        
        # Safety check for tiny terminals
        if max_y < 4 or max_x < 4:
            self.pos = (1, 1)
            self.symbol = self.config.get("snake_shape", "█")
            self.color = "YELLOW"
            self.type = "small"
            return
        
        # Determine type based on configurable chance
        big_food_pct = self.config.get("big_food_chance", 10)
        if random.random() < (big_food_pct / 100):
            self.type = "big"
        else:
            self.type = "small"
        
        # Use the same shape as the snake for visual cohesion
        self.symbol = self.config.get("snake_shape", "█")
        
        # Use configured food color or random if set to RANDOM
        food_color = self.config.get("food_color", "RANDOM")
        if food_color == "RANDOM":
            self.color = random.choice(["YELLOW", "CYAN", "MAGENTA", "WHITE", "RED", "BLUE"])
        else:
            self.color = food_color
            
        while True:
            y = random.randint(1, max_y - 2)
            x = random.randint(1, max_x - 2)
            self.pos = (y, x)
            
            if occupied_positions is None or self.pos not in occupied_positions:
                break
                
    def get_points(self):
        settings = self.config.get("food_settings", {}).get(self.type, {})
        return settings.get("point", 10)

    def get_visuals(self):
        return self.symbol, self.color
