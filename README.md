# Tic Tac Toe

## About the game
- It is basic TicTacToe written in library Pygame
- Player has blue crosses, Bot has red circles
- To make a move, click on an empty cell
- Winner is highlighted with green line
- After end of a game you can click "NEW GAME" to play again
- It alternates who starts after every game - at first you, than Bot, than you, ...

## Installation and Startup
- You need to have Python installed 
- In command line enter "pip install pygame"
- Then type "python main.py" - make sure to be in the project folder where file main.py is located

## Project structure
This project uses the MVC Architecture.
- In view.py is everything that communitaces with pygame and with the user
- In controller.py is the game logic
- In model.py is the simple AI playing against you and state representation of the game
- In settings.py are some constants used within the project
- In main.py I just call the controller

## How the Bot works
- it is basic Minimax algorithm without any improvements like alpha-beta pruning, heuristics, iterative deepening or so.