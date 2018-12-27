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

# Control function

def control():
    direction = input(
        'Mars Rover Controls: north, south, west, east, position, '
        'stop: ')
    if direction == 'north':
        rover1.move_north()
        return control()
    elif direction == 'south':
        rover1.move_south()
        return control()
    elif direction == 'west':
        rover1.move_west()
        return control()
    elif direction == 'east':
        rover1.move_east()
        return control()
    elif direction == 'position':
        print(rover1.position)
        return control()
    elif direction == 'stop':
        print('Rover movement stopped.')
        prompt = input('Do you want to end the program (y/n)? Press any other '
                       'Key to abort.')
        if prompt == 'n':
            return control()
        elif prompt == 'y':
            print('Program ended. Returning position.')
            return rover1.position
        else:
            print('Stop aborted. Returning to control.')
            return control()
    else:
        print('Wrong input. Returning to control.')
        return control()

# Calling function
control()