# Tic Tac Toe Game

Welcome to the Tic Tac Toe Game! This project implements a simple Tic Tac Toe game using Python and Object-Oriented Programming (OOP) principles.

## Project Overview

This project consists of three main components:
1. **TicTacToe Class**: Manages the game board, assigns markers, checks for available positions, and determines the winner.
2. **Player Class**: Represents a player in the game, allowing them to choose a spot and return their marker and name.
3. **Main Script**: Runs the game, allowing two players to play against each other by taking turns.

## Setup Instructions

To set up this project, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/tic-tac-toe.git
    cd tic-tac-toe
    ```

2. **Ensure you have Python installed**:
    You can download Python from [python.org](https://www.python.org/).

3. **Run the Game**:
    Execute the main script to start playing:
    ```bash
    python main.py
    ```
    
## Usage Instructions

### Running the Game

1. When you start the game, you will be greeted with a welcome message and a display of the board positions.
2. Player 1 will be prompted to choose a marker (X or O).
3. Player 2 will automatically be assigned the other marker.
4. Players will take turns to choose a spot on the board by entering the number corresponding to the position they want to mark.
5. The game will continue until there is a winner or a draw.

### Game Controls

- **Choose a Spot**: Enter a number between 1 and 9 corresponding to the position on the board.

### Example

```bash
Welcome to Tic Tac Toe

| 1 | 2 | 3 |
| 4 | 5 | 6 |
| 7 | 8 | 9 |

Player 1: Choose a marker X or O: X

Player 1 marker: X
Player 2 marker: O

Player 1: Choose a spot from [1, 2, 3, 4, 5, 6, 7, 8, 9]: 5
|   |   |   |
|   | X |   |
|   |   |   |

Player 2: Choose a spot from [1, 2, 3, 4, 6, 7, 8, 9]: 1
| O |   |   |
|   | X |   |
|   |   |   |

...
