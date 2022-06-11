import time

# Game board
board = {"R1C1": " ", "R1C2": " ", "R1C3": " ", "R2C1": " ", "R2C2": " ",
         "R2C3": " ", "R3C1": " ", "R3C2": " ", "R3C3": " "}
# game board used when the game resets
new_board = {"R1C1": " ", "R1C2": " ", "R1C3": " ", "R2C1": " ", "R2C2": " ",
             "R2C3": " ", "R3C1": " ", "R3C2": " ", "R3C3": " "}

gamer = "X"
score_board = {"player1": "X", "player2": "O", "X_wins": 0, "O_wins": 0}  # The keys and values of the scoreboard
winner = None  # The game begins without any winners.
playing = True


# This displays the game board
def board_display(board):
    print("{0[R1C1]} | {0[R1C2]} | {0[R1C3]}".format(board))
    print("---------")
    print("{0[R2C1]} | {0[R2C2]} | {0[R2C3]}".format(board))
    print("---------")
    print("{0[R3C1]} | {0[R3C2]} | {0[R3C3]}".format(board))


# This block allows the players to quit the game or pick a spot on the game board
def gamer_input(board):
    global playing
    move = input("Enter Q to quit game OR a RowColumn combination,R1C1 to R3C3: ")
    if move in board and board[move] == " ":
        board[move] = gamer  # The first player is "X", every input on the board places "X" on the chosen spot
    elif move == "Q" or move == "q":
        playing = False
    else:
        print("Pick another spot!")  # Error message displayed when player picks an occupied spot on the board
        return gamer_input(board)  # Gives the player another chance to pick a blank spot


# This block of code displays the scoreboard
def score_board_display(score_board):
    print("{0[player1]} | {0[player2]}".format(score_board))
    print("-" * 9)
    print("{0[X_wins]} | {0[O_wins]}".format(score_board))


# This blocks counts the number of wins of each player
def wins(score_board):
    while winner == "X":
        score_board["X_wins"] = score_board["X_wins"] + 1
        return score_board_display(score_board)
    else:
        score_board["O_wins"] = score_board["O_wins"] + 1
        return score_board_display(score_board)

    # This checks for horizontal possible wins


def horizontal_wins(board):
    global winner
    if board["R1C1"] == board["R1C2"] == board["R1C3"] and board["R1C1"] != " ":
        winner = board["R1C1"]
        return True
    elif board["R2C1"] == board["R2C2"] == board["R2C3"] and board["R2C1"] != " ":
        winner = board["R2C1"]
        return True
    elif board["R3C1"] == board["R3C2"] == board["R3C3"] and board["R3C1"] != " ":
        winner = board["R3C1"]
        return True


# This checks for vertical possible wins
def vertical_wins(board):
    global winner
    if board["R1C1"] == board["R2C1"] == board["R3C1"] and board["R1C1"] != " ":
        winner = board["R1C1"]
        return True
    elif board["R1C2"] == board["R2C2"] == board["R3C2"] and board["R1C2"] != " ":
        winner = board["R1C2"]
        return True
    elif board["R1C3"] == board["R2C3"] == board["R3C3"] and board["R1C3"] != " ":
        winner = board["R1C3"]
        return True


# This checks for diagonal possible wins
def diagonal_wins(board):
    global winner
    if board["R1C1"] == board["R2C2"] == board["R3C3"] and board["R1C1"] != " ":
        winner = board["R1C1"]
        return True
    elif board["R1C3"] == board["R2C2"] == board["R3C1"] and board["R1C3"] != " ":
        winner = board["R1C3"]
        return True


# This checks for draws
def draw_check(board):
    global playing
    if (board["R1C1"] != " " and board["R1C2"] != " " and board["R1C3"] != " "
            and board["R2C1"] != " " and board["R2C2"] != " " and board["R2C3"] != " "
            and board["R3C1"] != " " and board["R3C2"] != " " and board["R3C3"] != " "):
        board_display(board)
        print("We have a draw!")
        return game_replay()


# This allows players to start a new game
def new_game():
    board.update(new_board)  # This line resets the board from the previous game
    time.sleep(2)
    switch_turns()  # These twin methods allow the last player from the previous game to play first
    switch_turns()
    print(f"---------{gamer} goes first!----------")
    board_display(board)
    gamer_input(board)
    get_winner(board)
    draw_check(board)


# This method asks players if they would like to continue playing
def game_replay():
    global playing
    print("Replay game?")
    replay = input("Type Y to continue playing or N to quit: ")
    if replay == "Y" or replay == "y":
        return new_game()
    elif replay == "N" or replay == "n":
        playing = False


# This method states the winner
def get_winner(board):
    global playing
    if horizontal_wins(board):
        board_display(board)
        print(f"------{winner} WINS!------")
        wins(score_board)
        return game_replay()
    elif vertical_wins(board):
        board_display(board)
        print(f"------{winner} WINS!------")
        wins(score_board)
        return game_replay()
    elif diagonal_wins(board):
        board_display(board)
        print(f"------{winner} WINS!------")
        wins(score_board)
        return game_replay()


# This method switches gamers
def switch_turns():
    global gamer
    if gamer == "X":
        gamer = "O"
    else:
        gamer = "X"


# This is the game loop
while playing:
    board_display(board)
    gamer_input(board)
    get_winner(board)
    draw_check(board)
    switch_turns()




