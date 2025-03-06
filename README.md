# Tic-Tac-Toe with Minimax Algorithm

## Overview
This is a basic implementation of a Tic-Tac-Toe game where a human player competes against an AI. The AI uses the Minimax algorithm to determine the best move. The game is played on a 3x3 grid, and the first player to align three of their marks horizontally, vertically, or diagonally wins.

## Features
- **Human vs AI**: The human player inputs their moves, and the AI calculates the optimal counter-move using the Minimax algorithm.
- **Minimax Algorithm**: The AI evaluates each possible move and chooses the one that maximizes its chances of winning while minimizing the player's chances.

## Code Breakdown

### TicTacToe Class
- **Board Initialization**: The board is a 3x3 grid initialized with empty spaces.
- **Game Over Check**: The game checks for a win (three marks in a row, column, or diagonal) or a draw (no empty spaces left).
- **Move Making**: Players and AI take turns making moves. Moves are placed on the board only if the space is empty.
- **Minimax Algorithm**: The AI uses the Minimax algorithm to recursively explore all possible moves and select the one that maximizes its chances of winning.
- **Best Move Calculation**: The `find_best_move` method finds the best move for the AI by evaluating all empty spots on the board.

### Minimax Function
- **Maximizing Player (AI)**: When it's the AI's turn, it aims to maximize the score.
- **Minimizing Player (Player)**: When it's the player's turn, the AI aims to minimize the score.
- **Recursion**: The algorithm evaluates every possible game state recursively, considering future moves until the game is over.

## Gameplay Loop
1. The game prints the current board.
2. The player inputs a move (row and column).
3. The AI calculates and places its move.
4. The game continues until there's a winner or a tie.
