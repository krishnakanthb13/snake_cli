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
        
        # Determine type based on chance
        big_food_chance = self.config.get("food_settings", {}).get("big", {}).get("chance", 0.1)
        if random.random() < big_food_chance:
            self.type = "big"
        else:
            self.type = "small"
            
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
        settings = self.config.get("food_settings", {}).get(self.type, {})
        return settings.get("shape", "•"), settings.get("color", "YELLOW")
