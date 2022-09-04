#versus the computer
#will never be defeated 

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

current_player = "X"

winner = None

import random

#function for the tic-tac-toe board
def print_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#function for the player input 
def player_input(board):
    player = int(input("Enter a number (1-9) : "))
    while True: 
        if player >= 1 and player <= 9 and board[player - 1] == "-":           
            board[player - 1] = current_player 
            break

        else: 
            print("Invalid. Please retry again")
            player = int(input("Enter a number (1-9)"))

#function for winning horizontal condition 
def check_horizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True 
    
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True

    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#function for winning vertical condition
def check_vertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True 

    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#function for winning diagonal condition
def check_diagonal(board):
    global winner 
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True 
        
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 

#function to switch players
def switch_player():
    global current_player
    if current_player == "X":
        current_player = "O"

    else:
        current_player = "X"

#function for the computer input to stop player from winning horizontally  
def horizontal_counter(board):
    if current_player == "O":
        #first line of horizontal
        if board[0] == "X" and board[1] == "X" and board[2] == "-":
            board[2] = "O"
            return True

        elif board[0] == "X" and board[2] == "X" and board[1] == "-":
            board[1] = "O"
            return True

        elif board[1] == "X" and board[2] == "X" and board[0] == "-":
            board[0] = "O"
            return True

        #second line of horizontal
        elif board[3] == "X" and board[4] == "X" and board[5] == "-":
            board[5] = "O"
            return True

        elif board[4] == "X" and board[5] == "X" and board[3] == "-":
            board[3] = "O"
            return True

        elif board[3] == "X" and board[5] == "X" and board[4] == "-":
            board[4] = "O"
            return True

        #third line of horizontal 
        elif board[6] == "X" and board[7] == "X" and board[8] == "-":
            board[8] = "O"
            return True

        elif board[7] == "X" and board[8] =="X" and board[6] == "-":
            board[6] = "O"
            return True

        elif board[6] == "X" and board[8] == "X" and board[7] == "-":
            board[7] = "O"
            return True

#function for the computer input to stop player from winning vertically 
def vertical_counter(board):
    if current_player == "O":
        #first vertical line
        if board[0] == "X" and board[3] == "X" and board[6] == "-":
            board[6] = "O"
            return True
 
        elif board[0] == "X" and board[6] == "X " and board[3] == "-":
            board[3] = "O"
            return True

        elif board[3] == "X" and board[6] == "X" and board[0] == "-":
            board[0] = "O"
            return True

        #second vertical line 
        elif board[1] == "X" and board[4] == "X" and board[7] == "-":
            board[7] = "O"
            return True

        elif board[1] == "X" and board[7] == "X" and board[4] == "-":
            board[4] = "O"
            return True

        elif board[4] == "X" and board[7] == "X" and board[1] == "-":
            board[1] = "O"
            return True

        #third vertical line
        elif board[2] == "X" and board[5] == "X" and board[8] == "-":
            board[8] = "O"
            return True

        elif board[2] == "X" and board[8] == "X" and board[5] == "-":
            board[5] = "O"
            return True

        elif board[5] == "X" and board[8] == "x" and board[2] == "-":
            board[2] = "O"
            return True

#function for the computer input to stop player from winning diagonally
def diagonal_counter(board):
    if current_player == "O":
        #to the right 
        if board[0] == "X" and board[4] == "X" and board[8] == "-":
            board[8] = "O"
            return True

        elif board[0] == "X" and board[8] == "X" and board[4] == "-":
            board[4] = "O"
            return True

        elif board[4] == "X" and board[8] == "X" and board[0] == "-":
            board[0] = "O"
            return True

        #to the left 
        elif board[2] == "X" and board[4] == "X" and board[6] == "-":
            board[6] = "O"
            return True

        elif board[2] == "X" and board[6] == "X" and board[4] == "-":
            board[4] = "O"
            return True

        elif board[4] == "X" and board[6] == "X" and board[2] == "-":
            board[2] = "O"
            return True

#function for the computer to randomly choose the position of the board 
def computer_input(board):
    while current_player == "O":
        comp_position = random.randint(0, 8) #computer randomly choose a position (0-8)
        if board[comp_position] == "-":
            board[comp_position] = "O"
            switch_player()

#function for winning the game
def win_game(board):
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print_board(board)
        print("Congratulation! The winner is : " + winner)

#function for tie game
def tie_game(board):
    if "-" not in board:
        print_board(board)
        print("We have a tie!")

        
while True:
    while True:
        print("\n")
        print_board(board)
        player_input(board)
        
        #check when player inputs, condition for winning or tie game
        if win_game(board):
            break

        elif tie_game(board):
            break

        #switch to computer's turn
        switch_player()

        #computer check if there's a counter first 
        if horizontal_counter(board) or vertical_counter(board) or diagonal_counter(board):
            if win_game(board):
                break
            if tie_game(board):
                break

            switch_player() #switch to player's turn if there's no winner or tie 

        else:
            computer_input(board) #if there isn't a counter needed, computer randomly select and check winning or tie condition 
            if win_game(board):
                break

            elif tie_game(board):
                break

    again = input("Do you still want to play again ? [y/n] : ")
    if again == "y":
        for i in range (9): #in range means 0-n, excluding n
            board[i] = "-" 
            continue 
    
    elif again =="n":
        print("Thank you for playing :)")
        break 



