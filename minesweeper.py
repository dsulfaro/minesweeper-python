from random import randint

# create the board and mines
board = [["-" for x in range(5)] for x in range(5)]
mines = set()

# randomly sets position of mines
def load_mines(mines):
    a = (randint(0,4),randint(0,4))
    b = (randint(0,4),randint(0,4))
    c = (randint(0,4),randint(0,4))
    mines.add(a)
    mines.add(b)
    mines.add(c)

# finds surrounding mines and changes the current space's number to that number
def surround(board, x, y):
    numMines = 0
    #top-left
    if (x > 0 and y > 0):
        c = (x-1, y-1)
        if c in mines:
            numMines += 1
    #top
    if (x > 0):
        c = (x-1, y)
        if c in mines:
            numMines += 1
    #top-right
    if (x > 0 and y < 4):
        c = (x-1, y+1)
        if c in mines:
            numMines += 1
    #left
    if (y > 0):
        c = (x, y-1)
        if c in mines:
            numMines += 1
    #right
    if (y < 4):
        c = (x, y+1)
        if c in mines:
            numMines += 1
    #bottom-left
    if (x < 4 and y > 0):
        c = (x+1, y-1)
        if c in mines:
            numMines += 1
    #bottom
    if (x < 4):
        c = (x+1, y)
        if c in mines:
            numMines += 1
    #bottom-right
    if (x < 4 and y < 4):
        c = (x+1, y+1)
        if c in mines:
            numMines += 1
    board[x][y] = str(numMines)



def print_board(x):
    for row in x:
        print " ".join(row)

# main function for playing the game
def play():

    # instructions are printed
    print """Clear the board without hitting the mines
Only enter values between 0 - 4
There are three mines total
May the odds be ever in your favor"""
    print_board(board)
    found = False #variable to see if a mine was hit
    load_mines(mines)
    count = 1 # number of spaces visited; game is ended once it hits 23

    # loop to execute the game
    # ends if all non-mine spaces are visited OR
    # if the player hits a mine
    while (not found):

        # game ends if player hits all non-mine spaces
        if count == 23:
            print "You won!!!"
            for (m, n) in mines:
                board[m][n] = "X"
            exit(0)

        # gets user input for x and y coordinates
        x = raw_input("x coordinate: ")
        y = raw_input("y coordinate: ")

        x = int(x)
        y = int(y)

        # end game if player hits mine
        coord = (x, y)
        if (coord in mines):
            print "You lose"
            board[x][y] = "X"
            for (m, n) in mines:
                board[m][n] = "X"
            print_board(board)
            found = True

        # else mark space as visited
        # find number of surrounding mines
        # and print the board
        else:
            count += 1
            surround(board, x, y)
            print_board(board)

# execute game
play()





