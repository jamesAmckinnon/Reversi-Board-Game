def Stones_Reversed(execute, reversedStones, whosTurn, targetRow, targetCol):
    """This function takes in a list of reversed stones as input and after all directions have been checked the function prints
       the stones that have been flipped, which stone was placed to cause the reversals and which player placed that stone."""

    opponent = 'machine'
    if whosTurn == 'machine': opponent = 'human' # this is used to specify which players stone made the reversals in the print statement
    if execute: # if last direction has been checked
        if len(reversedStones) > 1: # if more than one stone has been reversed 
            print('\n\n{} stone ({},{}) reversed {} {} stones:'.format(whosTurn.capitalize(), targetRow + 1, targetCol + 1, len(reversedStones), opponent))
            for stone in reversedStones: # print stones that have been reversed
                print('{},{}'.format(stone[0] + 1,stone[1] + 1))
            print()
            reversedStones.clear() # clear reversed list for next players turn
        else:
            print('\n\n{} stone ({},{}) reversed {} {} stone:'.format(whosTurn.capitalize(), targetRow + 1, targetCol + 1, len(reversedStones), opponent))
            print('{},{}\n'.format(reversedStones[0][0] + 1, reversedStones[0][1] + 1))
            reversedStones.clear() # clear reversed list for next players turn



def Row_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    'This function checks each row within the same column above the target stone to see if there are one or more stones that can be reversed.'

    print('\n(1) Checking rows in decreasing order on the same column....', end=' ')    
    stonesToFlip = []
    stoneOrder = [' X ', ' O '] 
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this

    for row in range(targetRow - 1, -1, -1): # loops through a range equal to the amount of spots above target stone
        if board[row][targetCol] == '   ': break 
        elif board[row][targetCol] == stoneOrder[0]: # if spot has an opponents stone on it
            stonesToFlip.append([row,targetCol]) # adds spots with opponent stones to stonesToFlip list
            continue
        elif stonesToFlip == []: break # this will break the function if the first stone above the target stone is a current player's stone
        for stone in stonesToFlip: 
            board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
            print()
            print("""
--------------
{},{} reversed 
--------------
            """.format(stone[0]+1,stone[1]+1))
            Print_Board()
            reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
        print()
        return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Row_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    'This function checks each row within the same column below the target stone to see if there are one or more stones that can be reversed.'

    print('(2) Checking rows in increasing order on the same column....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this

    for row in range(targetRow +1, rows): # loops through a range equal to the amount of spots below target stone
        if board[row][targetCol] == '   ': break
        elif board[row][targetCol] == stoneOrder[0]: # if spot has an opponents stone on it
            stonesToFlip.append([row, targetCol]) # adds coordinates of stone to stonesToFlip list
            continue
        elif stonesToFlip == []: break # this will break the function if the first stone below the target stone is a current player's stone
        for stone in stonesToFlip:
            board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
            print()
            print("""
--------------
{},{} reversed 
--------------
        """.format(stone[0]+1,stone[1]+1))
            Print_Board()
            reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
        print()
        return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Col_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones): 
    'This function checks each column within the same row to the left of the target stone to see if there are one or more stones that can be reversed.'

    print('(3) Checking cols in decreasing order on the same row....', end=' ')    
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this

    for col in range(targetCol- 1, -1, -1): # loops through a range equal to the amount of spots to the left of target stone
        if board[targetRow][col] == '   ': break
        elif board[targetRow][col] == stoneOrder[0]: # if spot has an opponents stone on it
            stonesToFlip.append([targetRow, col]) # adds coordinates of stone to stonesToFlip list
            continue
        elif stonesToFlip == []: break # this will break the function if the first stone beside the target stone is a current player's stone
        for stone in stonesToFlip:
            board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
            print("""

--------------
{},{} reversed 
--------------
            """.format(stone[0]+1,stone[1]+1))
            Print_Board()
            reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
        print()
        return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Col_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    'This function checks each column within the same row to the right of the target stone to see if there are one or more stones that can be reversed.'

    print('(4) Checking cols in increasing order on the same row....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this

    for col in range(targetCol +1, cols): # loops through a range equal to the amount of spots to the right of target stone
        if board[targetRow][col] == '   ': break
        elif board[targetRow][col] == stoneOrder[0]: # if spot has an opponents stone on it
            stonesToFlip.append([targetRow, col]) # adds coordinates of stone to stonesToFlip list
            continue
        elif stonesToFlip == []: break # this will break the function if the first stone beside the target stone is a current player's stone
        for stone in stonesToFlip:
            board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
            print("""

--------------
{},{} reversed 
--------------
        """.format(stone[0]+1,stone[1]+1))
            Print_Board()
            reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
        print()
        return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Diag_Decreasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    """This function checks each spot on the board that is diagonal from the target stone. The function checks in the diagonal direction that is up and to the 
       left starting at the target stone to see if there are one or more stones that can be reversed."""

    print('(5) Checking diagonally rows and cols in decreasing order....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this
    rowIndex = targetRow # this keeps track of which row value the loop is on

    for col in range(targetCol- 1, -1, -1): # loops through a range equal to the amount of spots diagonal (up and to the left) of target stone
        rowIndex -= 1 
        if rowIndex >= 0: # if loop is at a row index greater than or equal to the first row on the board
            if board[rowIndex][col] == '   ': break
            elif board[rowIndex][col] == stoneOrder[0]: # if spot has an opponents stone on it
                stonesToFlip.append([rowIndex, col]) # adds coordinates of stone to stonesToFlip list
                continue
            elif stonesToFlip == []: break # this will break the function if the first stone diagonal to the target stone is a current player's stone
            for stone in stonesToFlip: 
                board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
                print("""

--------------
{},{} reversed 
--------------
            """.format(stone[0]+1,stone[1]+1))
                Print_Board()
                reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
            print()
            return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Diag_Increasing(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    """This function checks each spot on the board that is diagonal from the target stone. The function checks in the diagonal direction that is down and to the 
       right starting at the target stone to see if there are one or more stones that can be reversed."""

    print('(6) Checking diagonally rows and cols in increasing order....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this
    rowIndex = targetRow # this keeps track of which row value the loop is on

    for col in range(targetCol +1, cols): # loops through a range equal to the amount of spots diagonal (down and to the right) of target stone
        rowIndex += 1
        if rowIndex <= (rows - 1): # if loop is at a row index less than or equal to the last row on the board
            if board[rowIndex][col] == '   ': break
            elif board[rowIndex][col] == stoneOrder[0]: # if spot has an opponents stone on it
                stonesToFlip.append([rowIndex, col]) # adds coordinates of stone to stonesToFlip list
                continue
            elif stonesToFlip == []: break # this will break the function if the first stone diagonal to the target stone is a current player's stone
            for stone in stonesToFlip:
                board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
                print("""

--------------
{},{} reversed 
--------------
            """.format(stone[0] + 1, stone[1] + 1))
                Print_Board()
                reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
            print()
            return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Diag_Rows_Dec_Cols_Inc(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    """This function checks each spot on the board that is diagonal from the target stone. The function checks in the diagonal direction that is up and to the 
       right starting at the target stone to see if there are one or more stones that can be reversed."""

    print('(7) Checking diagonally rows in increasing order and cols in decreasing order....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this
    rowIndex = targetRow # this keeps track of which row value the loop is on

    for col in range(targetCol + 1, cols): # loops through a range equal to the amount of spots diagonal (up and to the right) of target stone
        rowIndex -= 1
        if rowIndex >= 0: # if loop is at a row index greater than or equal to the first row on the board
            if board[rowIndex][col] == '   ': break
            elif board[rowIndex][col] == stoneOrder[0]: # if spot has an opponents stone on it
                stonesToFlip.append([rowIndex, col]) # adds coordinates of stone to stonesToFlip list
                continue
            elif stonesToFlip == []: break # this will break the function if the first stone diagonal to the target stone is a current player's stone
            for stone in stonesToFlip:
                board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
                print("""

--------------
{},{} reversed 
--------------
            """.format(stone[0]+1,stone[1]+1))
                Print_Board()
                reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
            print()
            return board, reversedStones # the reversedStones list needs to be returned because stones from multiple functions need to be able to add to the list
    print('NOTHING REVERSED')
    return board, reversedStones



def Diag_Rows_Inc_Cols_Dec(targetRow, targetCol, board, Print_Board, rows, cols, whosTurn, reversedStones):
    """This function checks each spot on the board that is diagonal from the target stone. The function checks in the diagonal direction that is down and to the 
       left starting at the target stone to see if there are one or more stones that can be reversed."""

    print('(8) Checking diagonally rows in decreasing order and cols in increasing order....', end=' ')
    stonesToFlip = []
    stoneOrder = [' X ', ' O ']
    if whosTurn == 'machine': stoneOrder = [' O ', ' X '] # depending on which player has just placed a stone the stone values used below will change based on this
    rowIndex = targetRow # this keeps track of which row value the loop is on

    for col in range(targetCol - 1, -1, -1): # loops through a range equal to the amount of spots diagonal (down and to the left) of target stone
        rowIndex += 1
        if rowIndex <= (rows - 1): # if loop is at a row index less than or equal to the last row on the board
            if board[rowIndex][col] == '   ': break
            elif board[rowIndex][col] == stoneOrder[0]: # if spot has an opponents stone on it
                stonesToFlip.append([rowIndex, col]) # adds coordinates of stone to stonesToFlip list
                continue
            elif stonesToFlip == []: break # this will break the function if the first stone diagonal to the target stone is a current player's stone
            for stone in stonesToFlip:
                board[stone[0]][stone[1]] = stoneOrder[1] # changes spot to current player's stone
                print("""

--------------
{},{} reversed 
--------------
            """.format(stone[0]+1,stone[1]+1))
                Print_Board()
                reversedStones.append(stone) # stones that have been reversed are added to this list and then used in the reversedStones function
            print()
            Stones_Reversed(True, reversedStones, whosTurn, targetRow, targetCol) # values needed for the Stones_Reversed function are set as parameters and the function is called
            return board, reversedStones # the reversedStones list and the board are returned
    print('NOTHING REVERSED')
    if reversedStones != []: Stones_Reversed(True, reversedStones, whosTurn, targetRow, targetCol) # this checks to see if there were any stones reversed in the other directions and if there was Stones_Reversed is called
    return board, reversedStones
    
