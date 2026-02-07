import random

class Obstacles:
    def __init__(self, bounds):
        self.bounds = bounds
        self.points = []

    def spawn(self, count, occupied_positions):
        max_y, max_x = self.bounds
        self.points = []
        
        for _ in range(count):
            while True:
                y = random.randint(1, max_y - 2)
                x = random.randint(1, max_x - 2)
                pos = (y, x)
                if pos not in occupied_positions and pos not in self.points:
                    self.points.append(pos)
                    break
                    
    def check_collision(self, head):
        return head in self.points
