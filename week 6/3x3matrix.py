# this code is 3x3 matrix game

def printMatrix(mtx):
    for row in mtx:
        print(row)
def play_game():
    matrix = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    isGameRunning = True
    alreadyChosen = []
    printMatrix(matrix)
    while isGameRunning:
        choice = input("Enter row and column in matrix: ")
        if choice in alreadyChosen:
            print("Already Chosen")
            continue
        elif choice not in ["11", "12", "13", "21", "22", "23", "31", "32", "33"]:
            print("Please choose a number in 3x3 matrix only")
            continue
        else:
            alreadyChosen.append(choice)
            choiceRow = int(choice[0])
            choiceColumn = int(choice[1])
            matrix[choiceRow-1][choiceColumn-1] = "X"
            printMatrix(matrix)
        if matrix == [['X', 'X', 'X'], ['X', 'X', 'X'], ['X', 'X', 'X']]:
            isGameRunning = False
play_game()