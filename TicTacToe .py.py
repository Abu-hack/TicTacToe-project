import random

def display_board(board):
    print('   |    |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |    |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |    |')
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |    |')

def player_input():
    marker = ''
    while marker not in ['O', 'X']:
        marker = input('Player 1: Do you want to be X or O? ').upper()
    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, position, marker):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or
            (board[4] == mark and board[5] == mark and board[6] == mark) or
            (board[1] == mark and board[2] == mark and board[3] == mark) or
            (board[7] == mark and board[4] == mark and board[1] == mark) or
            (board[8] == mark and board[5] == mark and board[2] == mark) or
            (board[9] == mark and board[6] == mark and board[3] == mark) or
            (board[7] == mark and board[5] == mark and board[3] == mark) or
            (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    return 'Player 1' if random.randint(0, 1) == 0 else 'Player 2'

def space_check(board, position):
    return board[position] == '' 

def full_board_check(board):
    return not any(space_check(board, i) for i in range(1, 10))

def player_choice(board):
    position = ''
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

print("Welcome to Tic Tac Toe!")
while True:
    theboard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first!')

    game_on = True

    while game_on:
        if turn == "Player 1":
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, position, player1_marker)

            if win_check(theboard, player1_marker):
                display_board(theboard)
                print("Congratulations Player 1! You've won the game!")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("The game is a draw!")
                    break
                else:
                    turn = "Player 2"
        else:
            # Player 2's turn
            display_board(theboard)
            position = player_choice(theboard)
            place_marker(theboard, position, player2_marker)

            if win_check(theboard, player2_marker):
                display_board(theboard)
                print("Congratulations Player 2! You've won the game!")
                game_on = False
            else:
                if full_board_check(theboard):
                    display_board(theboard)
                    print("The game is a draw!")
                    break
                else:
                    turn = 'Player 1'
    
    if not replay():
        break

