from random import randint

scores = {"computer": 0, "player" : 0}


class Board:
    """
    Main board class. Sets board size , the number of ships, the player's name and board type (player board or computer)
    has methods for adding ships and guesses and printing the board
    """

    def __init__(self, size, num_ships, name, type):
        self.size = size
        self.board = [["." for x in range(size)] for y in range(size)]
        self.num_ships = num_ships
        self.name = name
        self.type = type
        self.guesses = []
        self.ships = []

    def print(self):
        for row in self.board:
            print(" ".join(row))

        if (x, y) in self.ships:
            self.board[x] [y] = "*"
            return "Hit"
        else:
            return "Miss"

    
    def add_ship(self, x, y, type="computer"):
        if len(self.ships) >= self.num_ships:
            print("Error: you cannot add more ships!")
        else:
            self.ships.append((x, y))
            if self.type == "player":
                self.board[x] [y] = "@"


def random_point(size):
    """
    helper function to return to a random integer between 0 and size
    """
    return randint(0, size - 1)



def populate_board(board):
    """
    for future refrense
    """




def make_guess(board):
    """
    for future refrense
    """


def play_game(computer_board, player_board):
    """
    for future refrense
    """


