class Spaceship:
    def __init__(self, x=0, y=0, z=0, direction="N"):
        # Initialize the spaceship with given position and direction
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        # Move the spaceship forward based on its current direction
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y + 1, z)
        elif self.direction == "S":
            self.position = (x, y - 1, z)
        elif self.direction == "E":
            self.position = (x + 1, y, z)
        elif self.direction == "W":
            self.position = (x - 1, y, z)
        elif self.direction == "Up":
            self.position = (x, y, z + 1)
        elif self.direction == "Down":
            self.position = (x, y, z - 1)

    def move_backward(self):
        # Move the spaceship backward based on its current direction
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y - 1, z)
        elif self.direction == "S":
            self.position = (x, y + 1, z)
        elif self.direction == "E":
            self.position = (x - 1, y, z)
        elif self.direction == "W":
            self.position = (x + 1, y, z)
        elif self.direction == "Up":
            self.position = (x, y, z - 1)
        elif self.direction == "Down":
            self.position = (x, y, z + 1)

    def turn_left(self):
        # Turn the spaceship 90 degrees to the left
        directions = ["N", "W", "S", "E", "Up", "Down"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % len(directions)]

    def turn_right(self):
        # Turn the spaceship 90 degrees to the right
        directions = ["N", "E", "S", "W", "Down", "Up"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def turn_up(self):
        # Turn the spaceship upwards
        directions = ["Up", "N", "Down", "S", "E", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index + 1) % len(directions)]

    def turn_down(self):
        # Turn the spaceship downwards
        directions = ["Down", "S", "Up", "N", "E", "W"]
        current_index = directions.index(self.direction)
        self.direction = directions[(current_index - 1) % len(directions)]

    def execute_command(self, command):
        # Execute a single command by calling the appropriate method
        if command == "f":
            self.move_forward()
        elif command == "b":
            self.move_backward()
        elif command == "l":
            self.turn_left()
        elif command == "r":
            self.turn_right()
        elif command == "u":
            self.turn_up()
        elif command == "d":
            self.turn_down()

    def get_position(self):
        # Return the current position of the spaceship
        return self.position

    def get_direction(self):
        # Return the current direction of the spaceship
        return self.direction
