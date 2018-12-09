# Stating the class
class MarsRover:
    def __init__(self):
        self.position = [10, 4]

    def move_north(self):
        self.position[0] = self.position[0] - 1

    def move_south(self):
        self.position[0] = self.position[0] + 1

    def move_west(self):
        self.position[1] = self.position[1] - 1

    def move_east(self):
        self.position[1] = self.position[1] + 1


# Creating an instance
rover1 = MarsRover()

# Checking
print(rover1.position)

# Moving
rover1.move_north()
rover1.move_west()

# Checking
print(rover1.position)
