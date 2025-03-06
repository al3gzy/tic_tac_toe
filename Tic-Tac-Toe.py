import tkinter as tk
from tkinter import messagebox, simpledialog
class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def print_board(self):
        for row in self.board:
            print('|'.join(row))
            print('-' * 5)

    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = ' '

    def game_over(self):
        for row in self.board:
            if row.count('Player') == 3 or row.count('AI') == 3:
                return True
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count('Player') == 3 \
                    or [self.board[row][col] for row in range(3)].count('AI') == 3:
                return True
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ') \
                or (self.board[0][2] == self.board[1][1] == self.board[2][0] != ' '):
            return True
        if all(cell != ' ' for row in self.board for cell in row):
            return True
        return False

    def evaluate(self):
        for row in self.board:
            if row.count('AI') == 3:
                return 1
            elif row.count('Player') == 3:
                return -1
        for col in range(3):
            if [self.board[row][col] for row in range(3)].count('AI') == 3:
                return 1
            elif [self.board[row][col] for row in range(3)].count('Player') == 3:
                return -1
        if (self.board[0][0] == self.board[1][1] == self.board[2][2] == 'AI') \
                or (self.board[0][2] == self.board[1][1] == self.board[2][0] == 'AI'):
            return 1
        elif (self.board[0][0] == self.board[1][1] == self.board[2][2] == 'Player') \
                or (self.board[0][2] == self.board[1][1] == self.board[2][0] == 'Player'):
            return -1
        return 0

    def minimax(self, depth, is_maximizing):
        if self.game_over():
            return self.evaluate()
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.make_move(i, j, 'AI')
                        score = self.minimax(depth + 1, False)
                        self.undo_move(i, j)
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == ' ':
                        self.make_move(i, j, 'Player')
                        score = self.minimax(depth + 1, True)
                        self.undo_move(i, j)
                        best_score = min(score, best_score)
            return best_score

    def find_best_move(self):
        best_score = -float('inf')
        best_move = (-1, -1)
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.make_move(i, j, 'AI')
                    score = self.minimax(0, False)
                    self.undo_move(i, j)
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        return best_move

game = TicTacToe()
while not game.game_over():
    game.print_board()
    player_row = int(input("Enter row (0-2): "))
    player_col = int(input("Enter column (0-2): "))
    if game.make_move(player_row, player_col, 'Player'):
        if game.game_over():
            break
        ai_row, ai_col = game.find_best_move()
        game.make_move(ai_row, ai_col, 'AI')
game.print_board()
print("Game Over")