from src.command_parser import CommandParser
from src.spaceship import Spaceship

def main():
    # Define the starting position and direction for the spaceship
    start_position = (0, 0, 0)
    start_direction = "N"
    
    # Prompt the user to enter a series of commands
    commands = input("Enter commands: ")
    
    # Parse the entered commands using the CommandParser class
    parsed_commands = CommandParser.parse_commands(commands)

    # Create an instance of the Spaceship class
    spaceship = Spaceship()
    
    # Execute each parsed command using the spaceship instance
    for command in parsed_commands:
        spaceship.execute_command(command)
    
    # Get the final position and direction of the spaceship
    final_position = spaceship.get_position()
    final_direction = spaceship.get_direction()
    
    # Print the starting position, initial direction, final position, and final direction
    print("Starting Position:", start_position)
    print("Initial Direction:", start_direction)
    print("Final Position:", final_position)
    print("Final Direction:", final_direction)

if __name__ == "__main__":
    # Call the main function when the script is executed
    main()
