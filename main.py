#here we define the game we want to solute
sudoku = [
    [3,4,1,9,6,7,2,5,8],
    [0,0,0,0,0,0,0,6,0],
    [0,8,0,1,0,0,0,9,0],
    [0,0,8,0,0,0,0,3,2],
    [6,1,9,0,0,0,0,0,0],
    [0,0,2,0,0,0,0,0,4],
    [0,0,0,0,0,3,5,0,7],
    [1,0,0,0,0,8,0,0,0],
    [0,5,0,0,2,0,0,0,0]
        ]

def numberZeroExist():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

#looking in the board
#l --> line col--> column
def possibleNumber(l,col,number):
    global sudoku
    #line
    for i in range(0,9):
        if(sudoku[l][i] == number):
            return False
    #column
    for i in range(0,9):
        if(sudoku[i][col] == number):
            return False
    #the square
    l0 = (l//3)*3
    col0 = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if(sudoku[i+l0][j+col0] == number):
                return False

    return True

def solve():
    global cont
    cont+=1
    global sudoku
    for i in range(0,9):
        for j in range(0,9):
            if(sudoku[i][j] == 0):#space with sudoku is empty >>zero<<
                for n in range(1, 10):
                    if(possibleNumber(i,j,n)):
                        sudoku[i][j] = n
                        solve()
                        if(not numberZeroExist()):
                            sudoku[i][j] = 0
                return


def printSudoku():
    for i in range(0,9):
        print()
        for j in range(0,9):
            print(sudoku[i][j],end=" ")
            if((j+1)%3 == 0):
                print(end=" ")
        if((i+1)%3 == 0):
            print()

#code call
printSudoku()
cont = 0
solve()
print()
print("***************************")
printSudoku()

print("\n\nCalls of solve function: "+ str(cont))
