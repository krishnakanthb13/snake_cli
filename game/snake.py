import random

class Snake:
    def __init__(self, start_pos, direction=(0, 1), initial_length=3, base_symbol="█", base_color="GREEN"):
        self.body = [start_pos]
        # Initialize body with initial length
        y, x = start_pos
        dy, dx = direction
        for i in range(1, initial_length):
            self.body.append((y - dy * i, x - dx * i))
            
        self.direction = direction
        self.growth_pending = [] # Stores (symbol, color) of food eaten but not yet added to tail
        self.symbols = [base_symbol] * initial_length # Head + segments
        self.segment_colors = [base_color] * initial_length
        self.colors = [] # Used for mixed color mode (dynamic/random)

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
        # Symbols are indexed to match body segments. No shift needed if we insert/pop correctly.
        
        if self.growth_pending:
            # Grow by adding the (symbol, color) to the tail
            new_symbol, new_color = self.growth_pending.pop(0)
            self.symbols.append(new_symbol)
            self.segment_colors.append(new_color)
        else:
            self.body.pop()
            
        return new_head

    def grow(self, amount=1, symbol="●", color="YELLOW"):
        for _ in range(amount):
            self.growth_pending.append((symbol, color))

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
