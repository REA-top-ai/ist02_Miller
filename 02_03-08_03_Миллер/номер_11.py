def is_lo_shu(square):

    numbers = []
    for row in square:
        for num in row:
            numbers.append(num)

    if sorted(numbers) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        return False

    for row in square:
        if sum(row) != 15:
            return False

    for col in range(3):
        if square[0][col] + square[1][col] + square[2][col] != 15:
            return False

    if square[0][0] + square[1][1] + square[2][2] != 15:
        return False

    if square[0][2] + square[1][1] + square[2][0] != 15:
        return False

    return True

square = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]

if is_lo_shu(square):
    print("Это магический квадрат Ло Шу")
else:
    print("Это не магический квадрат")