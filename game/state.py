import time

class GameState:
    def __init__(self, config):
        self.config = config
        self.score = 0
        self.start_time = time.time()
        self.paused = False
        self.game_over = False
        self.snake_length = 0
        self.food_eaten = {"small": 0, "big": 0}
        self.player_name = "Player"

    def reset(self):
        self.score = 0
        self.start_time = time.time()
        self.paused = False
        self.game_over = False
        self.snake_length = 0
        self.food_eaten = {"small": 0, "big": 0}

    def update_score(self, points, food_type):
        self.score += points
        self.food_eaten[food_type] += 1

    def get_survival_time(self):
        return int(time.time() - self.start_time)

    def get_summary(self):
        return {
            "player": self.player_name,
            "score": self.score,
            "time_survived": self.get_survival_time(),
            "snake_length": self.snake_length,
            "food_eaten": self.food_eaten,
            "settings": {
                "speed": self.config.get("speed"),
                "walls_on": self.config.get("walls_on"),
                "obstacles_on": self.config.get("obstacles_on"),
                "mode": self.config.get("snake_mode"),
                "shape": self.config.get("snake_shape")
            }
        }
