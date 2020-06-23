board = [' ']*10


def display_board(board):
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])


print("Player1, please select X or O ?: ")
player1 = input()
cnt = 0
for attempt in range(0, 2):
    if player1 not in ['X', 'O']:
        print('Please enter valid input. X or O ?: ')
        player1 = input()
        cnt = cnt + 1
        if cnt == 2:
            print("Thank you for enough invalid attempt. Improve your English")
    else:
        break

display_board(board)
print("Player1, please enter your move: ")
move = int(input())
for attempt in range(0, 2):
    if move not in range(1, 10):
        print('Please enter valid input. ?: ')
        move = int(input())
        cnt = cnt + 1
        if cnt == 2:
            print("Thank you for enough invalid attempt. Improve your English")
    else:
        board[move] = player1

display_board(board)
