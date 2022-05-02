#espaco para definir o jogo que sera inserido

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

def numerZeroExiste():
    global sudoku
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                return False
    return True

#percorrer o tabuleiro
#l --> linha col--> coluna
def possivelNumero(l,col,number):
    #print(number, end=" ")
    global sudoku
    #linha
    for i in range(0,9):
        if(sudoku[l][i] == number):
            return False
    #coluna
    for i in range(0,9):
        if(sudoku[i][col] == number):
            return False
    #quadrado
    l0 = (l//3)*3
    col0 = (col//3)*3
    for i in range(0,3):
        for j in range(0,3):
            if(sudoku[i+l0][j+col0] == number):
                return False

    return True

def resolve():
    global cont
    cont+=1
    global sudoku
    for i in range(0,9):
        for j in range(0,9):
            if(sudoku[i][j] == 0):#espaço do sudoku vazio
                for n in range(1, 10):
                    if(possivelNumero(i,j,n)):
                        sudoku[i][j] = n
                        resolve()
                        if(not numerZeroExiste()):
                            sudoku[i][j] = 0
                return


def imprimeSudoku():
    for i in range(0,9):
        print()
        for j in range(0,9):
            print(sudoku[i][j],end=" ")
            if((j+1)%3 == 0):
                print(end=" ")
        if((i+1)%3 == 0):
            print()

#chamda do codigo
imprimeSudoku()
cont = 0
resolve()
print()
print("***************************")
imprimeSudoku()

print("\n\nNúmero de chamada da função: "+ str(cont))











