import unittest
from src.spaceship import Spaceship

class TestSpaceship(unittest.TestCase):
    def test_move_forward(self):
        # Create a spaceship instance and execute the 'f' command
        spacecraft = Spaceship()
        spacecraft.execute_command("f")
        
        # Assert that the spaceship's position has moved forward in the 'N' direction
        self.assertEqual(spacecraft.get_position(), (0, 1, 0))

    def test_move_backward(self):
        # Create a spaceship instance and execute the 'b' command
        spacecraft = Spaceship()
        spacecraft.execute_command("b")
        
        # Assert that the spaceship's position has moved backward in the 'S' direction
        self.assertEqual(spacecraft.get_position(), (0, -1, 0))

    def test_turn_left(self):
        # Create a spaceship instance facing 'N' direction and execute the 'l' command
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("l")
        
        # Assert that the spaceship's direction has turned from 'N' to 'W'
        self.assertEqual(spacecraft.get_direction(), "W")

    def test_turn_right(self):
        # Create a spaceship instance facing 'N' direction and execute the 'r' command
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("r")
        
        # Assert that the spaceship's direction has turned from 'N' to 'E'
        self.assertEqual(spacecraft.get_direction(), "E")

    def test_turn_up(self):
        # Create a spaceship instance facing 'N' direction and execute the 'u' command
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("u")
        
        # Assert that the spaceship's direction has turned from 'N' to 'Up'
        self.assertEqual(spacecraft.get_direction(), "Up")

    def test_turn_down(self):
        # Create a spaceship instance facing 'N' direction and execute the 'd' command
        spacecraft = Spaceship(direction="N")
        spacecraft.execute_command("d")
        
        # Assert that the spaceship's direction has turned from 'N' to 'Down'
        self.assertEqual(spacecraft.get_direction(), "Down")

    def test_e2e_scenario(self):
        # Create a spaceship instance and execute a series of commands
        spacecraft = Spaceship()
        commands = ["f", "r", "u", "b", "l"]
        for command in commands:
            spacecraft.execute_command(command)
        
        # Assert that the spaceship's position and direction match the expected final state
        self.assertEqual(spacecraft.get_position(), (0, 1, -1))
        self.assertEqual(spacecraft.get_direction(), "N")

    def test_invalid_command(self):
        # Create a spaceship instance and try to execute an invalid command
        spacecraft = Spaceship()
        
        # Assert that trying to execute an invalid command raises a ValueError
        with self.assertRaises(ValueError):
            spacecraft.execute_command("x")

if __name__ == '__main__':
    unittest.main()
