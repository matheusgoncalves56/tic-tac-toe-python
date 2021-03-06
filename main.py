game_board = []
n = 3
end_game = False
player1 = True

def create_game_board():
    for i in range(n):
       tmp = []

       for j in range(n):
           tmp.append(" ")

       game_board.append(tmp[:])

def print_game_board():
    for i in range(0, 3):
        print("          {0} | {1} | {2}".format(game_board[i][0], game_board[i][1], game_board[i][2]))
        if i != 2:
            print('          ---------')

def input_player():
    global player1

    move = input("Player {0}: Please, make your move (x, y): ".format(1 if player1 else 2))
    xy = move.split(",")

    x = int(xy[0])
    y = int(xy[1])

    if x > 2 or y > 2:
        print("Invalid  position!")
    elif game_board[x][y] == " ":
        game_board[x][y] = "X" if player1 else "O"
        player1 = not player1
    else:
        print("This position has already been fill")

def player_win():
    for i in range(0,3):
        if game_board[i][0] == game_board[i][1] and game_board[i][1] == game_board[i][2]:
            return game_board[i][0] == "X" or game_board[i][0] == "O";
    for i in range(0,3):
        if game_board[0][i] == game_board[1][i] and game_board[1][i] == game_board[2][i]:
            return game_board[0][i] == "X" or game_board[0][i] == "O";

    return False

def main():
    global end_game
    create_game_board()

    while not end_game:
        print()
        print_game_board()
        print()
        input_player()
        if player_win():
            end_game = True

    print_game_board()
    print("Player {0} win!".format("1" if not player1 else "2"))

main()
