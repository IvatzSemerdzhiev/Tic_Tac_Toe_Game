from colorama import Fore
from collections import deque
from pyfiglet import Figlet

numeration_board = [[str(1 + i), str(2 + i), str(3 + i)] for i in range(0, 9, 3)]
board = [[" "," "," "], [" "," "," "],[" "," "," "]]

def print_board():
    for el in board:
        print(f"| {' | '.join(el)} |")



def choose_move():
    try:
        move = int(input(f"{turns[0][0]}, choose your move: "))
    except ValueError:
        move = int(input(f"{turns[0][0]}, choose valid move: "))

    r = (move-1)//3
    c = (move-1)%3
    return [r,c]

def check_win():
    diagobal_lr = all(board[i][i] == turns[0][1] for i in range(3))
    diagobal_rl = all(board[i][-i-1] == turns[0][1] for i in range(3))
    row1_win = all(board[0][j] == turns[0][1] for j in range(3))
    row2_win = all(board[1][j] == turns[0][1] for j in range(3))
    row3_win = all(board[2][j] == turns[0][1] for j in range(3))
    col1_win = all((board[i][0]) == turns[0][1] for i in range(3))
    col2_win = all((board[i][1]) == turns[0][1] for i in range(3))
    col3_win = all((board[i][2]) == turns[0][1] for i in range(3))


    if any([diagobal_lr, diagobal_rl, row1_win, row2_win, row3_win, col1_win, col2_win, col3_win]):
        figlet = Figlet(font="roman")
        print(figlet.renderText(f"{turns[0][0]} wins the game!!!"))
        raise SystemExit()



figlet = Figlet(font="doom")
print(figlet.renderText("Tic-Tac-Toe"))


player_one = input(Fore.BLUE+ "PLAYER_1, please enter your name! " + Fore.RESET)
player_two = input(Fore.YELLOW + "PLAYER_2, please enter your name! " + Fore.RESET)

print(Fore.BLUE + "This is the numeration of the play-board!" + Fore.RESET)
print(*numeration_board, sep="\n")
symb1 = "X"
symb2 = "O"
counter = 0
turns = deque([(player_one, symb1), (player_two, symb2)])

print(Fore.GREEN + "Great, let's play!" + Fore.RESET)

r, c = choose_move()
while True:
    try:
        if board[r][c] == " ":
            board[r][c] = turns[0][1]
            check_win()
            counter += 1
            if counter == 9:
                figlet = Figlet(font="doom")
                print(figlet.renderText("GAME-OVER"))

            turns.rotate()
            print_board()

    except IndexError:
        pass



    r, c = choose_move()




