import random

class Snake:
    def __init__(self, start_pos, direction=(0, 1), initial_length=3):
        self.body = [start_pos]
        # Initialize body with initial length
        y, x = start_pos
        dy, dx = direction
        for i in range(1, initial_length):
            self.body.append((y - dy * i, x - dx * i))
            
        self.direction = direction
        self.growth_pending = 0
        self.shapes = [] # Used for mixed shape mode
        self.colors = [] # Used for mixed color mode

    def change_direction(self, new_direction):
        if new_direction:
            # Prevent reversing directly
            if (new_direction[0], new_direction[1]) != (self.direction[0] * -1, self.direction[1] * -1):
                self.direction = new_direction

    def move(self):
        head_y, head_x = self.body[0]
        dy, dx = self.direction
        new_head = (head_y + dy, head_x + dx)
        
        self.body.insert(0, new_head)
        
        if self.growth_pending > 0:
            self.growth_pending -= 1
        else:
            self.body.pop()
            
        return new_head

    def grow(self, amount=1):
        self.growth_pending += amount

    def check_collision(self, bounds=None, self_collision=True):
        head = self.body[0]
        
        # Self collision
        if self_collision and head in self.body[1:]:
            return True
            
        # Wall collision
        if bounds:
            max_y, max_x = bounds
            y, x = head
            if y < 0 or y >= max_y or x < 0 or x >= max_x:
                return True
                
        return False

    def wrap(self, bounds):
        max_y, max_x = bounds
        head_y, head_x = self.body[0]
        self.body[0] = (head_y % max_y, head_x % max_x)
