matrix = [
    [1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0],
    [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]
    ]

matrix = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0]
    ]

for x in range(len(matrix)):
    print(matrix[x])

print()

def test(position, end, passed, not_passed):
    
    x, y = position[0], position[1]
    new_position = tuple()
    
    xup = position[0] + 1; xdn = 0
    yup = position[1] + 1; ydn = 0

    if xup > 1:
        xdn = position[0] - 1
    if yup > 1:
        ydn = position[1] - 1

    if xup > len(matrix) - 1:
        xup = len(matrix) - 1
        xdn = xup - 2

    if yup > len(matrix[0]) - 1:
        yup = len(matrix[0]) - 1
        ydn = yup - 2

    if matrix[position[0]][position[1]] and (position[0], position[1]) not in passed:
        passed.append((position[0], position[1]))

    if matrix[x][yup] and (x, yup) not in not_passed and (x, yup) not in passed:
        not_passed.append((x, yup))

    if matrix[x][ydn] and (x, ydn) not in not_passed and (x, ydn) not in passed:
        not_passed.append((x, ydn))

    if matrix[xup][y] and (xup, y) not in not_passed and (xup, y) not in passed:
        not_passed.append((xup, y))

    if matrix[xdn][y] and (xdn, y) not in not_passed and (xdn, y) not in passed:
        not_passed.append((xdn, y))

    if len(not_passed) and end not in passed:
        new_position = not_passed.pop()
        test(new_position, end, passed, not_passed)
    else:
        return tuple()

    return passed

passed = test((3, 3), (3, 5), [], [])
print(passed)
