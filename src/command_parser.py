class CommandParser:
    @staticmethod
    def parse_commands(commands):
        # Create an empty list to store parsed valid commands
        parsed_commands = []

        # Iterate through each command in the input list
        for cmd in commands:
            # Check if the command is one of the valid options
            if cmd in ["f", "b", "l", "r", "u", "d"]:
                # If valid, add it to the parsed_commands list
                parsed_commands.append(cmd)
            else:
                # If not valid, raise an error indicating the invalid command
                raise ValueError(f"Invalid command: {cmd}")

        # Return the list of parsed and valid commands
        return parsed_commands
