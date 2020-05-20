matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    ]

#Just a starting demo.
def demo_1():
    print("Note: At the final result 5 is the cordinate you selected or a starting point to finding the path it can go is represented as 2 and finally terminates its walk at 6.")
    print("Initial matrix:")
    for x in range(len(matrix)):
        print(matrix[x])
    return 0

#Make the matrix as it before.
def refresh(matrix):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 5 or matrix[x][y] == 2 or matrix[x][y] == 6:
                matrix[x][y] = 1
    return 0

#Make a cordinate for a matrix where 1 is present.
def cordinate_1(matrix):
    ones = []
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if matrix[x][y] == 1:
                ones.append((x, y))
    return ones

#Main function to note.
def cordinate_cango(Tuple, matrix):
    val = [(Tuple)]
    for x, y in val:
        if x <= len(matrix) and y <= len(matrix[0]) and x > -1 and y > -1:
            matrix[x][y] = 5
    test = []
    cordinate_one = cordinate_1(matrix)
    matrixd = matrix
    for x in range(len(cordinate_one)):
        for x, y in val:
            if (x, y) in cordinate_one and (x, y) not in test:
                test.append((x, y))
            if (x + 1, y) in cordinate_one and (x + 1, y) not in test:
                test.append((x + 1, y))
            if (x - 1, y) in cordinate_one and (x - 1, y) not in test:
                test.append((x - 1, y))
            if (x, y + 1) in cordinate_one and (x, y + 1) not in test:
                test.append((x, y + 1))
            if (x, y - 1) in cordinate_one and (x, y - 1) not in test:
                test.append((x, y - 1))
        #To find again the sub cordinate.
        val = test
    return val, matrixd


def demo(Tuple):
    starting_point = Tuple
    path, matrixd = cordinate_cango(starting_point, matrix)
    for x, y in path:
        matrixd[x][y] = 2
    matrixd[path[-1][0]][path[-1][1]] = 6
    print("---------------------")
    print("You selected starting point as {}.".format(starting_point))
    print("Cordinate passed: ", path, sep = "\n")
    print("Final matrix: ")
    for x in range(len(matrix)):
        print(matrixd[x])
    return 1

condition = True

while condition:
    demo_1()
    print("Selected the starting point: ")
    x, y = input().split()
    demo((int(x), int(y)))
    condition = input("Do you want to execute again(y): ") == "y"
    refresh(matrix)
