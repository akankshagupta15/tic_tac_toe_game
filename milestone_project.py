def display_board(board):
#modified comment
    #print('   |   |')
    print(' ' + board[7] + ' | '  + board[8] + ' | ' + board[9])
    #print('   |   |')
    print('----------')
    #print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6]) 
    #print('   |   |')
    print('----------')
    #print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('   |   |')

test_board = ['#','X','O','X','O','X','O','X','O','X']
display_board(test_board)

def player_input():
    '''
    OUTPUT = (player 1 marker, player 2 maker)
    '''
    marker = ' '
    while marker != 'X' and marker != 'O':
        marker = input ('player1: choose X or O: ').upper()

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

player1_marker , player2_marker = player_input()

def place_marker(board,marker,position):
    board[position] = marker

test_board
place_marker(test_board, '$' , 8)
display_board(test_board)

def win_check(board, mark):
    # win tic ta toe?
    #all rows  and check to see if they all share the same marker?
    ((board[7] == mark and board[8] == mark and board[9] == mark ) or # across the upper line
    (board[4] == mark and board[5] == mark and board[6] == mark ) or  # across the middle line
    (board[1] == mark and board[2] == mark and board[3] == mark ) or  # across the bottom line
    (board[7] == mark and board[4] == mark and board[1] == mark ) or  # down the middle line
    (board[8] == mark and board[5] == mark and board[2] == mark ) or  # down the middle line
    (board[9] == mark and board[6] == mark and board[3] == mark ) or  # down the right side line
    (board[7] == mark and board[5] == mark and board[3] == mark ) or  # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark ))    # diagonal
     
    
    # all colums, check to see if marker matches
    #2 diagonois, check to see match

display_board(test_board)
win_check(test_board,'X')

import random
def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'

def space_check(board,position):
    return board[position] == ' '

def full_board_check(board):
     
    for i in range(1,10):
        if space_check(board,i):
         return False
    #board is full if we return true 
    return True


def player_choice(board):

    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not  space_check(board,position):
        position = int(input("choose a position: (1-9)  "))
    return position


def replay():
    choice = input("play again?  enter Yes or No ")
    return choice == 'Yes'

#while loop to keep running the gAME 
print ('Welcome to the tic tac toe')

while True:

    #play the game 

    ## set everything up (board, whos first, choose markers X,O)
    the_board = [' ']*10
    player1_marker,player2_marker = player_input()

    turn = choose_first()
    print( turn  +  ' will go first')
    play_game = input('ready to play? y or n? ')
    
    if play_game == 'y':
        game_on = True
    else:
        game_on = False
    
    ### game play

    while game_on:
        if turn == 'player 1':

            #show the board
            display_board(the_board)

            #choose the position
            position = player_choice(the_board)
             
            #place the marker on the position
            place_marker(the_board,player1_marker,position)

            #check if they won
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('player 1 has won! !')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ("tie game!")
                    game_on = False
                else:
                    turn = 'player 2'

        else :
            #show the board
            display_board(the_board)

            #choose the position
            position = player_choice(the_board)
             
            #place the marker on the position
            place_marker(the_board,player2_marker,position)

            #check if hey won
            if win_check(the_board,player2_marker):
                display_board(the_board)
                print('player 2 has won! !')
                game_on = False
                
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print ("tie game!")
                    game_on = False
                else:
                    turn = 'player 1'


    if not replay():
     break

            












 