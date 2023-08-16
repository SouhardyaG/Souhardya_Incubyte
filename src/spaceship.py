class Spaceship:
    def __init__(self, x=0, y=0, z=0, direction='N'):
        # Initialize the spaceship with given position and direction
        self.x = x
        self.y = y
        self.z = z
        self.direction = direction

    def move_forward(self):
        # Move the spaceship forward based on its current direction
        if self.direction == 'N':
            self.y += 1
        elif self.direction == 'S':
            self.y -= 1
        elif self.direction == 'E':
            self.x += 1
        elif self.direction == 'W':
            self.x -= 1
        elif self.direction == 'Up':
            self.z += 1
        elif self.direction == 'Down':
            self.z -= 1

    def move_backward(self):
        # Move the spaceship backward based on its current direction
        if self.direction == 'N':
            self.y -= 1
        elif self.direction == 'S':
            self.y += 1
        elif self.direction == 'E':
            self.x -= 1
        elif self.direction == 'W':
            self.x += 1
        elif self.direction == 'Up':
            self.z -= 1
        elif self.direction == 'Down':
            self.z += 1

    def turn_left(self):
        # Turn the spaceship 90 degrees to the left
        if self.direction == 'N':
            self.direction = 'W'
        elif self.direction == 'S':
            self.direction = 'E'
        elif self.direction == 'E':
            self.direction = 'N'
        elif self.direction == 'W':
            self.direction = 'S'

    def turn_right(self):
        # Turn the spaceship 90 degrees to the right
        if self.direction == 'N':
            self.direction = 'E'
        elif self.direction == 'S':
            self.direction = 'W'
        elif self.direction == 'E':
            self.direction = 'S'
        elif self.direction == 'W':
            self.direction = 'N'

    def turn_up(self):
        # Turn the spaceship upwards
        self.direction = 'Up'

    def turn_down(self):
        # Turn the spaceship downwards
        self.direction = 'Down'

    def get_position(self):
        # Return the current position of the spaceship
        return self.x, self.y, self.z

    def get_direction(self):
        # Return the current direction of the spaceship
        return self.direction

    def execute_command(self, command):
        # Execute the given command by calling the appropriate method
        if command == 'f':
            self.move_forward()
        elif command == 'b':
            self.move_backward()
        elif command == 'l':
            self.turn_left()
        elif command == 'r':
            self.turn_right()
        elif command == 'u':
            self.turn_up()
        elif command == 'd':
            self.turn_down()
        else:
            raise ValueError('Invalid command')
