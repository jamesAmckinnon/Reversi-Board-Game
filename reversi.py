""" James McKinnon

    This is a console board game called reversi. The objective of the game is to have the most stones on the board. You are playing against 
    "machine". You and machine take turns placing stones on the board and you can reverse stones by placing stones on both sides of one or 
    more machine stones in any direction. Machine can do the same thing to your stones. Multiple stones can be reversed at once in multiple 
    directions. Only a newly placed stone can reverse opponent stones. When there are no more spots left on the board the game is over and 
    a winner is named. If there is a tie the winner can be decided by playing rock, paper, scissors against machine."""



import random
from reverseFunctions import Row_Decreasing, Row_Increasing, Col_Decreasing, Col_Increasing, Diag_Decreasing, Diag_Increasing, Diag_Rows_Dec_Cols_Inc, Diag_Rows_Inc_Cols_Dec


# allows user to specify the board size they want to play with 
while True:
    # This while loop makes sure that the user enters a valid input for the number of rows in the board.
    try:
        rows = eval(input('Input the rows that you want as the board size (1-9): '))
        if rows in range(1,10):
            break
        print('\n*** The row size should be an integer between 1 and 9 ***\n')
    except:
        print('\n*** The row size should be an integer between 1 and 9 ***\n')

while True:
    # This while loop makes sure that the user enters a valid input for the number of columns in the board
    try:
        cols = eval(input('Input the cols that you want as the board size (1-9): '))
        if cols in range(1,10):
            print()
            break
        print('\n*** The col size should be an integer between 1 and 9 ***\n')
    except:
        print('\n*** The col size should be an integer between 1 and 9 ***\n')



board = [["   "]*cols for i in range(rows)] # this initializes the board as a 2D list with the number of rows and columns that the user specifies 



def Print_Board():
    'This function prints the board with the specified number of rows and columns'

    rowNums = 0
    print("     ", end="")
    for c in range(cols):
        print(c+1, end="   ") # this creates the column numbers on top of the board
    print()
    print("   " + ("+---"*cols) + "+") # this creates a dividing line between column numbers and the board

    for row in board:
        rowNums = rowNums + 1 
        print(" " + str(rowNums), end=" ") # this creates the row numbers on the left side of the board
        for spaces in row:
            print("|" + spaces, end="") # this puts dividers between each column in each row
        print("|") # placed at the end of the row
        print("   " + ("+---"*cols) + "+") # this creates the dividing line between rows
    Live_Score()



targetRow = 0
targetCol = 0
reversedStones = []



def Reverse_Neighbours(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    """This function checks 8 directions on the board to see if there are stones that can be reversed. One or more stones will be reversed if they are in between
       an existing opponent stone and the stone that was just placed on the board. The function calls 8 other functions that each check one direction. The output
       of each function is an updated copy of the board and reversedStones list and these are passed on to the next function each time a function is called."""

    board, reversedStones = Row_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each row within the same column above the target stone
    board, reversedStones = Row_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each row within the same column below the target stone
    board, reversedStones = Col_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each column within the same row to the left of the target stone
    board, reversedStones = Col_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each column within the same row to the right of the target stone
    board, reversedStones = Diag_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each spot on the board that is diagonal from the target stone. Up and to the left.
    board, reversedStones = Diag_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each spot on the board that is diagonal from the target stone. Down and to the right.
    board, reversedStones = Diag_Rows_Dec_Cols_Inc(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each spot on the board that is diagonal from the target stone. Up and to the right.
    board, reversedStones = Diag_Rows_Inc_Cols_Dec(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones) # this function checks each spot on the board that is diagonal from the target stone. Down and to the left.
 


def Human_Turn():
    """This function asks the user to specify the spot on the board where they would like to place 
       a stone. It will then place the stone in that location in the 2D list and then print the board."""
    
    while True:
        'This makes sure the user imputs a valid row value'
        try:
            humanRow = eval(input('\nINPUT THE ROW WHERE YOU WANT TO PUT YOUR STONE BETWEEN 1 and {}: '.format(rows))) - 1
            if (humanRow+1) in range(1,(rows+1)):
                break
            print('\n*** The row should be an integer between 1 and {} ***'.format(rows))
        except:
            print('\n*** The row should be an integer between 1 and {} ***'.format(rows))

    while True:
        'This makes sure the user inputs a valid column value'
        try:
            humanCol = eval(input('INPUT THE COL WHERE YOU WANT TO PUT YOUR STONE BETWEEN 1 and {}: '.format(cols))) - 1
            if (humanCol+1) in range(1,(cols+1)):
                break
            print('\n*** The col should be an integer between 1 and {} ***\n'.format(cols))
        except:
            print('\n*** The col should be an integer between 1 and {} ***\n'.format(cols))

    if board[humanRow][humanCol] != "   ": # if the spot that the user chose already has a stone on it this will make them go back and choose a new spot
        print('\n*** The chosen spot is not empty, please choose another spot ***')
        Human_Turn()
    else: # if the spot that the user chose does not already have a stone on it then this will place the stone in the chosen spot and then print the board
        print("""
----------------------
Human's Choice is {},{}
----------------------
        """.format(humanRow+1,humanCol+1))
        board[humanRow][humanCol] = " O "
        Print_Board()
        Reverse_Neighbours(humanRow, humanCol, board, Print_Board, rows, cols, 'human', reversedStones)



def Press_C():
    "This function asks the user to enter the letter c in order to move on to the machine's turn. It will not let the user advance until the right key is entered."
    
    pressC = input('\nPress "c" to continue for machines turn: ')
    if pressC == "c": # this makes sure that the user enters 'c' before moving on
        return True
    else: # if the key that is entered is not valid the following error message will be printed and the function will start again
        print(""" 
        -------------------
            Invalid Key
        -------------------""") 
    Press_C()



def Machine_Turn():
    """This function is used to place a machine stone on the board. A random spot adjacent to a human stone is targetted and a stone is placed there. If there are no
       spots open beside any human stones the function will place a stone beside an existing machine stone. The function returns if no spots are left on the board."""

    rowIndex = -1
    colIndex = -1
    humanStones = []
    machineStones = []
    openSpots = []

    for row in board:
        rowIndex += 1 
        colIndex = -1 
        for col in row:
            colIndex += 1   
            if " O " in col: # this appends the positions of all human stones on the board to the humanStones list
                humanStones.append([rowIndex,colIndex]) 
            if " X " in col: # this appends the positions of all machine stones on the board to the machineStones list
                machineStones.append([rowIndex,colIndex])
            if "   " in col: # this appends the positions of all open spots on the board to the openSpots list
                openSpots.append([rowIndex,colIndex])


    adjacentSpots = [] # this stores the positions of all open spots on the board that are adjacent to a human stone
    for stones in humanStones:
        'This loop finds open spots on the board that are adjacent to human stones and appends their positions to the adjacentSpots list.'

        targetRow = stones[0]
        targetCol = stones[1]
        for i in [1,-1]: 
            """This loops through the i value of 1 and -1. 1 and -1 are used to either add or subtract 1 from the row or column value of the current stone in 
               the humanStones list. This will allow the spots that are adjacent to the human stones to be targeted. Once targetted, the loop will check
               to see if the spot is empty. If it is empty, the position of this empty adjacent spot is appended to the adjacentStones list."""

            if (targetRow + i) in range(0, rows): # this checks the rows that are (+) or (-) 1 row away from the target in the same column while making sure it is not out of bounds
                if board[targetRow + i][targetCol] == '   ': # if the adjacent spot is open it's board position is appended to the adjacentSpots list
                    adjacentSpots.append([targetRow + i,targetCol])
            if (targetCol + i) in range(0, cols): # this checks the columns that are (+) or (-) 1 column away from the target in the same row while making sure it is not out of bounds
                if board[targetRow][targetCol + i ] == '   ': # if the adjacent spot is open it's board position is appended to the adjacentSpots list
                    adjacentSpots.append([targetRow,targetCol + i])


    if adjacentSpots == []: 
        if openSpots == []: # if there are no adjacent spots open beside human stones this checks to see if there are any spots open at all
            return # if there are no open spots on the board the function returns and the game will end
        else: # if there are still open spots then a machine stone is randomly placed in an open spot
            randomSpot = random.choice(openSpots) 
            targetRow = randomSpot[0]
            targetCol = randomSpot[1]
            board[targetRow][targetCol] = " X " # a machine stone is placed in an open spot on the board
    else:    
        randomSpot = random.choice(adjacentSpots)  
        targetRow = randomSpot[0]
        targetCol = randomSpot[1]
        board[targetRow][targetCol] = " X " # if there are open spots adjacent to human stones a machine stone is placed next to a random human stone         


    if len(openSpots) >= 1: # if there are still open spots on the board after the machine places its stone:
        print("""
-----------------------
Machine's Choice is {},{}
-----------------------
    """.format(targetRow + 1, targetCol + 1))
        Print_Board()
        Reverse_Neighbours(targetRow, targetCol, board, Print_Board, rows, cols, 'machine', reversedStones)
    else: # if there are no open spots on the board after machine places stone:
        return



def No_Spots_Left(dashes):
    'This function prints who won the game if there are no spots left on the board'

    if rows==1 and cols==1: # if the user enters a board size that guarantees they will win:
        print("\n\nGood strategy, you win!")
    else:
        print("""

        ------------------{}
        Game over, {}!
        ------------------{}
        """.format("-"*dashes,count[2], "-"*dashes)) # this tells the user the game is over and says who won



def Count():
    'This function counts the total score for each player and decides a winner based on which player had more stones on the board'
    
    humanStones = 0
    machineStones = 0

    for row in board: # this loop counts how many stones each player has
        for col in row:
            if " O " in col: 
                humanStones += 1
            if " X " in col:
                machineStones += 1

    winner = "" # a winner is decided based on which player had the most stones on the board
    if humanStones > machineStones:
        winner = "you win"
        dashes = 1
    elif machineStones > humanStones:
        winner = "machine wins"
        dashes = 6
    else: 
        winner = "it's a tie"
        dashes = 4

    return [humanStones, machineStones, winner, dashes] # scores, winner and a number for formatting is returned 



def Score_Board():
    'This function prints a score count when there is a winner or a tie game.'

    print("""

Final score
Human: {}  Machine: {}

    """.format(count[0], count[1]))



def Tie_Breaker():
    'This function is a tie-breaker game of rock, paper, scissors to decide the winner if it is a tie game.'

    tieBreaker = input('Would you like to play rock, paper, scissors to decide a winner (y/n)? ')
    if tieBreaker in "nN":
        print('Thanks for playing!')
        return 

    elif tieBreaker in "yY":
        rounds = 1
        humanScore = 0
        machineScore = 0
        while True: # if the score for either player is equal to 2 then they win the tie-breaker and the function returns
            if humanScore == 2:
                print('\nCongratulations, you won the tie-breaker!\n')
                return
            elif machineScore == 2:
                print('\nThe machine won the tie-breaker!\n')
                return 
                
            choices = ["rock", "paper", "scissors"]
            toWin = {1: "scissors", 2: "rock", 3: "paper"} # this dictionary holds keys that represent rock (1), paper(2) and scissors(3) and values that represent the choice that each key will win against
            machineChoice = random.choice(choices)
            print("""\nROUND {} (first one to 2 points wins)
1) Rock
2) Paper
3) Scissors
        """.format(rounds))

            while True:
                try:
                    humanChoice = eval(input("Make a selection (1-3): "))
                    if humanChoice in range(1,4): # this makes sure humans choice is a valid integer
                        break
                    print('\n*** Your selection should be either 1, 2 or 3 ***\n')
                except: # this will keep the while loop going if there is an error because the human enters something that isn't able to be converted to an integer
                    print('\n*** Your selection should be either 1, 2 or 3 ***\n')
                    
            print('\nYour choice: {}'.format(choices[humanChoice - 1]))
            print("Machine's choice: {}".format(machineChoice))
            if toWin[humanChoice] == machineChoice: # if machineChoice matches the value that cooresponds to the humanChoice key in the toWin list then the machine looses the round
                rounds += 1
                humanScore += 1
                if humanScore < 2: # if human wins the round and hasn't got to 2 points yet the game continues and the human gets a point for the current round
                    print('\nYou are the winner of round {}!'.format(rounds-1))
            elif toWin[choices.index(machineChoice) + 1] == choices[humanChoice - 1]: 
                """choices.index(machineChoice) finds the value of the machineChoice variable inside the choices list and returns the index of where it 
                   is in the list. This allows the (index of machineChoice + 1) to be used as a key in the toWin dictionary. (humanChoice - 1) represents the 
                   index value that humanChoice is at in the choices list. Now if the toWin key matches up with the humanChoice value the machine wins the round."""

                rounds += 1
                machineScore += 1
                if machineScore < 2: # if machine wins the round but hasn't got to 2 points yet the game continues and they get a point for the current round
                    print('\nThe machine is the winner of round {}!'.format(rounds-1))

            else: # if neither statement's conditions are satisfied then the machine and human chose the same thing and they go again
                print('\nYou and the machine chose the same thing, choose again')

    else:
        print('\n*** Please enter y or n ***\n')
        Tie_Breaker()
    


def Live_Score():
    'This function is called every time the board is printed. It creates a live update of the score for the user to see while playing'

    humanStones = 0
    machineStones = 0

    for row in board: # this loop counts how many stones each player has
        for col in row:
            if " O " in col: 
                humanStones += 1
            if " X " in col:
                machineStones += 1
 
    print('   H: {}   M: {}'.format(humanStones,machineStones)) # this is printed under the board


Print_Board()

while True:
    count = Count()
    if count[0] + count[1] == (rows * cols):
        No_Spots_Left(count[3])
        Score_Board()
        if count[2] == "it's a tie":
            Tie_Breaker()
            break
        break
    else:
        Human_Turn()
        count = Count() 
        if count[0] + count[1] == (rows * cols):
            No_Spots_Left(count[3])
            Score_Board()
            break
        while Press_C() == False:
            Press_C()
        Machine_Turn()
