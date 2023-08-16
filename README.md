# Chandrayaan 3 Lunar Craft Control

Welcome to the Chandrayaan 3 Lunar Craft Control repository! This repository contains code for a program that simulates controlling a lunar spacecraft using galactic coordinates.

## Introduction

In this project, we've implemented a program to control a spacecraft's movement and orientation in the galaxy using galactic coordinates. The program uses a test-driven approach and is modularized for better readability and maintainability.

The core components of the project include:
- `spaceship.py`: Contains the `Spaceship` class that models the spacecraft's behavior and properties.
- `command_parser.py`: Contains the `CommandParser` class responsible for parsing and validating commands.

## Getting Started

### Prerequisites

- Python 3.x
- Git (optional but recommended)

### Installation

1. Clone this repository to your local machine:
git clone https://github.com/your-username/chandrayaan-3-lunar-craft-control.git


2. Navigate to the repository directory:
cd chandrayaan-3-lunar-craft-control


3. Install required dependencies:
pip install -r requirements.txt

## Usage

1. Run the main program:


python main.py

2. Enter a series of commands (e.g., `f`, `r`, `u`, etc.) to control the spacecraft.

3. The program will display the starting position, initial direction, final position, and final direction of the spacecraft.

## Testing

1. Navigate to the `tests` directory:
cd tests


2. Run the test suite:

python -m unittest test_spaceship.py


## Contributing

Contributions are welcome! If you find issues or have improvement ideas, open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
