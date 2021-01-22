import random
import math


def counterRow(square):
    rows = 0

    for row in square:
        count = 0
        for cube in row:
            if cube == 1:
                count += 1
            else:
                count = 0

            if  count >= 4:
                rows += 1

    return rows


def counterColumn(square):
    columns = 0

    for column in range(inpt):
        count = 0
        for cube in range(inpt):
            if square[cube][column] == 1:
                count += 1
            else:
                count = 0

            if  count >= 4:
                columns += 1

    return columns


def counterDiagonal(square):
    diagonals = 0
    temp = 0
    for i in range(inpt - 3):
        count = 0
        for diagonal in range(inpt - i):
            for cube in range(inpt):
                if diagonal == cube:
                    if square[cube + temp][diagonal] == 1:
                        count += 1
                    else:
                        count = 0

                    if count >= 4:
                        diagonals += 1
        temp += 1

    temp = 1
    for i in range(inpt - 3):
        count = 0
        for diagonal in range(inpt - i - 1):
            for cube in range(inpt):
                if diagonal == cube:
                    if square[cube][diagonal + temp] == 1:
                        count += 1
                    else:
                        count = 0

                    if count >= 4:
                        diagonals += 1
        temp += 1
    return diagonals


def counterDiagonalReverse(square):
    diagonals = 0
    temp = 0
    for i in range(inpt - 3):
        count = 0
        for diagonal in range(inpt - i - 1, -1, -1):
            for cube in range(inpt):
                if diagonal + cube == inpt -1:
                    if square[cube][diagonal + temp] == 1:
                        count += 1
                    else:
                        count = 0

                    if count >= 4:
                        diagonals += 1
        temp += 1

    temp = -1
    for i in range(inpt - 3):
        count = 0
        for diagonal in range(inpt - i - 2, -1, -1):
            for cube in range(inpt):
                if diagonal + cube == inpt - 1:
                    if square[cube + temp][diagonal] == 1:
                        count += 1
                    else:
                        count = 0

                    if count >= 4:
                        diagonals += 1
        temp -= 1
    return diagonals


def fillList(square):
    temp = []
    for i in range(size):
        if (i%2 == 0):
            temp.append(0)
        else:
            temp.append(1)

    random.shuffle(temp)
    for i in range(inpt):
        row = []
        for j in range(inpt):
            row.append(temp[i*inpt+j])
            
        square.append(row)


#checking if the input is a size that it is possible to create 4 (1s) in row.
inpt = int(input("Insert square's side size: "))
while inpt < 4:
    inpt = int(input("Insert square's side size(must be greater than 3): "))


size = inpt * inpt
print("The size of the square is: ", size)

square = []

fillList(square)

ones = counterRow(square) + counterColumn(square) + counterDiagonal(square) + counterDiagonalReverse(square)
print("The amount of 1s is: ", ones)