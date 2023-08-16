import unittest
from src.spaceship import Spaceship  # Import the Spaceship class to test

class TestSpaceship(unittest.TestCase):
    def test_move_forward(self):
        # Create a new Spaceship instance
        spacecraft = Spaceship()
        # Execute the "f" command
        spacecraft.execute_command("f")
        # Assert that the position has moved forward as expected
        self.assertEqual(spacecraft.get_position(), (0, 1, 0))

    def test_move_backward(self):
        # Create a new Spaceship instance
        spacecraft = Spaceship()
        # Execute the "b" command
        spacecraft.execute_command("b")
        # Assert that the position has moved backward as expected
        self.assertEqual(spacecraft.get_position(), (0, -1, 0))

    def test_turn_left(self):
        # Create a new Spaceship instance with initial direction "N"
        spacecraft = Spaceship(direction="N")
        # Execute the "l" command
        spacecraft.execute_command("l")
        # Assert that the direction has turned left as expected
        self.assertEqual(spacecraft.get_direction(), "W")

    def test_turn_right(self):
        # Create a new Spaceship instance with initial direction "N"
        spacecraft = Spaceship(direction="N")
        # Execute the "r" command
        spacecraft.execute_command("r")
        # Assert that the direction has turned right as expected
        self.assertEqual(spacecraft.get_direction(), "E")

    def test_turn_up(self):
        # Create a new Spaceship instance with initial direction "N"
        spacecraft = Spaceship(direction="N")
        # Execute the "u" command
        spacecraft.execute_command("u")
        # Assert that the direction has turned up as expected
        self.assertEqual(spacecraft.get_direction(), "Up")

    def test_turn_down(self):
        # Create a new Spaceship instance with initial direction "N"
        spacecraft = Spaceship(direction="N")
        # Execute the "d" command
        spacecraft.execute_command("d")
        # Assert that the direction has turned down as expected
        self.assertEqual(spacecraft.get_direction(), "Down")

    def test_e2e_scenario(self):
        # Create a new Spaceship instance
        spacecraft = Spaceship()
        # Define a series of commands
        commands = ["f", "r", "u", "b", "l"]
        # Execute each command sequentially
        for command in commands:
            spacecraft.execute_command(command)
        # Assert that the final position and direction are as expected
        self.assertEqual(spacecraft.get_position(), (0, 1, -1))
        self.assertEqual(spacecraft.get_direction(), "Up")

    def test_invalid_command(self):
        # Create a new Spaceship instance
        spacecraft = Spaceship()
        # Assert that executing an invalid command raises a ValueError
        with self.assertRaises(ValueError):
            spacecraft.execute_command("x")

if __name__ == '__main__':
    # Run the unit tests when the script is executed
    unittest.main()
