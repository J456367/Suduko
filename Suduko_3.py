import copy
import time
from collections import Counter


class Puzzles:

    Suduko_Input_Matrix_0 = [[0, 0, 0, 2, 6, 0, 7, 0, 1],
                           [6, 8, 0, 0, 7, 0, 0, 9, 0],
                           [1, 9, 0, 0, 0, 4, 5, 0, 0],
                           [8, 2, 0, 1, 0, 0, 0, 4, 0],
                           [0, 0, 4, 6, 0, 2, 9, 0, 0],
                           [0, 5, 0, 0, 0, 3, 0, 2, 8],
                           [0, 0, 9, 3, 0, 0, 0, 7, 4],
                           [0, 4, 0, 0, 5, 0, 0, 3, 6],
                           [7, 0, 3, 0, 1, 8, 0, 0, 0]]

    Suduko_Input_Matrix_1 = [[0, 0, 0, 6, 0, 0, 4, 0, 0],
                           [7, 0, 0, 0, 0, 3, 6, 0, 0],
                           [0, 0, 0, 0, 9, 1, 0, 8, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 5, 0, 1, 8, 0, 0, 0, 3],
                           [0, 0, 0, 3, 0, 6, 0, 4, 5],
                           [0, 4, 0, 2, 0, 0, 0, 6, 0],
                           [9, 0, 3, 0, 0, 0, 0, 0, 0],
                           [0, 2, 0, 0, 0, 0, 1, 0, 0]]

    Suduko_Input_Matrix_2 = [[0, 2, 0, 6, 0, 8, 0, 0, 0],
                           [5, 8, 0, 0, 0, 9, 7, 0, 0],
                           [0, 0, 0, 0, 4, 0, 0, 0, 0],
                           [3, 7, 0, 0, 0, 0, 5, 0, 0],
                           [6, 0, 0, 0, 0, 0, 0, 0, 4],
                           [0, 0, 8, 0, 0, 0, 0, 1, 3],
                           [0, 0, 0, 0, 2, 0, 0, 0, 0],
                           [0, 0, 9, 8, 0, 0, 0, 3, 6],
                           [0, 0, 0, 3, 0, 6, 0, 9, 0]
                           ]


def cubic_array():
    """
    Creates a 9x9x9 array

    :return:            suduko_cube == 9x9x9 array
    """
    suduko_cube = []
    for y in range(9):
        suduko_cube.append([])
        for x in range(9):
            suduko_cube[y].append([])
            for z in range(9):
                suduko_cube[y][x].append(0)
    return suduko_cube

Suduko_Cube = cubic_array()
Suduko_Resulting_Matrix = copy.deepcopy(Puzzles.Suduko_Input_Matrix_0)


def print_suduko(array_2d):
    """
    Print 2D array line by line

    :param array_2d:    Array 2D
    :return:            None
    """
    for col in range(9):
        print(array_2d[col])
    print()


def print_cube(array_3d):
    """
    Print 3D array array by array

    :param array_3d:    Array 3D
    :return:            None
    """
    for col in range(9):
        print(array_3d[col])
    print()


def fill_known_values(array_2d, array_3d):
    """
    Iterates through each column and row, if a values besides 0 is found in the array_2d it is then in the coordinate
    space with array_3d all values are changed to a list of 1 through 9, reflecting that no other value can be entered.

    :param array_2d:
    :param array_3d:
    :return:
    """
    for y in range(9):
        for x in range(9):
            if array_2d[y][x] != 0:
                array_3d[y][x] = [x for x in range(1, 10)]

    return array_3d

Suduko_Cube = fill_known_values(Suduko_Resulting_Matrix, Suduko_Cube)


def print_cube_2(array_3d):
    """
    Print 3D array, array by array

    :param array_3d:    Array 3D
    :return:            None
    """
    line = '\t' + "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"*2
    for col in range(9):
        print(line, '\n' + line if col % 3 == 0 else '')
        print('\t┃ ┃' +
              ''.join(map(str, array_3d[col][0])) + '┃' +
              ''.join(map(str, array_3d[col][1])) + '┃' +
              ''.join(map(str, array_3d[col][2])) +
              '┃ ┃' +
              ''.join(map(str, array_3d[col][3])) + '┃' +
              ''.join(map(str, array_3d[col][4])) + '┃' +
              ''.join(map(str, array_3d[col][5])) +
              '┃ ┃' +
              ''.join(map(str, array_3d[col][6])) + '┃' +
              ''.join(map(str, array_3d[col][7])) + '┃' +
              ''.join(map(str, array_3d[col][8])) + '┃ ┃')

    print(line, '\n' + line, '\n')


print("Suduko".upper())
print("Start")
print_suduko(Suduko_Resulting_Matrix)
input("Enter to Start:")


def by_row(array_2d, array_3d):
    """
    Iterates through each row filling in values from the 2d array to the 3d array

    :param array_2d:    2D Array 9x9
    :param array_3d:    3D Array 9x9x9
    :return:            array_3d
    """
    for col in range(9):
        for row in range(9):
            value = array_2d[col][row]
            if value == 0:
                pass
            else:
                for depth in range(9):
                    array_3d[col][depth][value-1] = value

    return array_3d


def by_column(array_2d, array_3d):
    """
    Iterates through each column filling in values from the 2d array to the 3d array

    :param array_2d:    2D Array 9x9
    :param array_3d:    3D Array 9x9x9
    :return:            array_3d
    """
    for col in range(0, 9):
        for row in range(0, 9):
            value = array_2d[col][row]
            if value == 0:
                pass
            else:
                for depth in range(9):
                    array_3d[depth][row][value-1] = value

    return array_3d


def by_square(array_2d, array_3d):
    """
    Iterates through each 3x3 square filling in values from the 2d array to the 3d array

    :param array_2d:    2D Array 9x9
    :param array_3d:    3D Array 9x9x9
    :return:            array_3d
    """
    for y in range(0, 3):
        for x in range(0, 3):
            for sub_y in range(3):
                for sub_x in range(3):
                    coordinate_y = y*3 + sub_y
                    coordinate_x = x*3 + sub_x
                    value = array_2d[coordinate_y][coordinate_x]
                    if value == 0:
                        pass
                    else:
                        for sub_y_placement in range(3):
                            for sub_x_placement in range(3):
                                array_3d[y*3 + sub_y_placement][x*3 + sub_x_placement][value-1] = value

    return array_3d


def isolate_zeros(array_2d, array_3d):
    """
    Finds Zeros in each array within each column and row of the 3D array, if  1 zero is found in each while the value
    in the 2D array is equal to 0 that value is added to the 2d array based on the index + 1

    :param array_2d:    2D Array 9x9
    :param array_3d:    3D Array 9x9x9
    :return:            array_3d
    """
    for y in range(9):
        for x in range(9):
            zero_count = array_3d[y][x].count(0)
            if array_2d[y][x] == 0 and zero_count == 1:
                value = array_3d[y][x].index(0) + 1
                array_2d[y][x] = value
    print()
    return array_2d


def isolate_double_by_row(array_3d):
    """
    This function will iterate through each column, then row, then take each value of that row and find if any have two
    zeros and cross reference it against all other number sets in that row. If a row has a matching pair or multiple
    matching pair it is then passed to the next part of the function that basically iterates through all values in that
    row besides the indexes the doubles were found and removes the zeros from the other values.

    :param array_3d:    3D Array 9x9x9
    :return:            array_3d
    """

    for col in range(9):
        # print('\nColumn', col)
        double_index = []
        suduko_y = []
        suduko_x = []
        for row in range(9):
            if array_3d[col][row].count(0) == 2:
                for double_validation in range(9):
                    if double_validation == row:
                        pass
                    elif array_3d[col][row] == array_3d[col][double_validation]:
                        double_index += [[i for i, x in enumerate(array_3d[col][row]) if x == 0]]
                        suduko_y += [col]
                        suduko_x += [row]
                    else:
                        continue
            else:
                continue

        if len(double_index) == 0:
            # print('\t No Values to adjust')
            pass

        # todo i might want to bring to my attention the number of values.
        # todo move the zip function here, then count in 2's to see if there are matching pairs, if not delete index 1
        # If the value error occurs when there is only one option you will need to add a condition to work through
            #each list to make sure that the conditions are met. aka there are two indexs with the same value.

        else:

            double_index, suduko_y, suduko_x = zip(*sorted(zip(double_index, suduko_y, suduko_x)))

            print('\t0 Index:   ', double_index)
            print('\tCol Index: ', suduko_y)
            print('\tRow Index: ', suduko_x)

            for value in range(len(double_index)):
                print('\t', array_3d[suduko_y[value]][suduko_x[value]])

            print('\tBefore - ┃ ┃' +
                  ''.join(map(str, array_3d[col][0])) + '┃' +
                  ''.join(map(str, array_3d[col][1])) + '┃' +
                  ''.join(map(str, array_3d[col][2])) +
                  '┃ ┃' +
                  ''.join(map(str, array_3d[col][3])) + '┃' +
                  ''.join(map(str, array_3d[col][4])) + '┃' +
                  ''.join(map(str, array_3d[col][5])) +
                  '┃ ┃' +
                  ''.join(map(str, array_3d[col][6])) + '┃' +
                  ''.join(map(str, array_3d[col][7])) + '┃' +
                  ''.join(map(str, array_3d[col][8])) + '┃ ┃')

            for value_removal in range(0, len(double_index), 2):

                for row in range(9):

                    if row == suduko_x[value_removal] or row == suduko_x[value_removal + 1]:
                        pass

                    else:
                        array_3d[col][row][double_index[value_removal][0]] = double_index[value_removal][0] + 1
                        array_3d[col][row][double_index[value_removal][1]] = double_index[value_removal][1] + 1

                        continue

            print('\tAfter  - ┃ ┃' +
                  ''.join(map(str, array_3d[col][0])) + '┃' +
                  ''.join(map(str, array_3d[col][1])) + '┃' +
                  ''.join(map(str, array_3d[col][2])) +
                  '┃ ┃' +
                  ''.join(map(str, array_3d[col][3])) + '┃' +
                  ''.join(map(str, array_3d[col][4])) + '┃' +
                  ''.join(map(str, array_3d[col][5])) +
                  '┃ ┃' +
                  ''.join(map(str, array_3d[col][6])) + '┃' +
                  ''.join(map(str, array_3d[col][7])) + '┃' +
                  ''.join(map(str, array_3d[col][8])) + '┃ ┃')
    print()
    return array_3d


def isolate_double_by_column(array_3d):
    """

    :param array_3d:
    :return:
    """

    for row in range(9):
        # print('\nRow', row)
        double_index = []
        suduko_y = []
        suduko_x = []
        for col in range(9):
            if array_3d[col][row].count(0) == 2:
                for double_validation in range(9):
                    if double_validation == col:
                        pass
                    elif array_3d[col][row] == array_3d[double_validation][row]:
                        double_index += [[i for i, x in enumerate(array_3d[col][row]) if x == 0]]
                        suduko_y += [col]
                        suduko_x += [row]
                    else:
                        continue

        # print(len(double_index))

        if len(double_index) == 0 or len(double_index) % 2 != 0:
            # print('\t No Values to adjust')

            # todo move the zip function here, then count in 2's to see if there are matching pairs, if not delete index 1
            # If the value error occurs when there is only one option you will need to add a condition to work through
            # each list to make sure that the conditions are met. aka there are two indexs with the same value.

            pass

        else:
            pass
            double_index, suduko_y, suduko_x = zip(*sorted(zip(double_index, suduko_y, suduko_x)))

            print('\t0 Index:   ', double_index)
            print('\tCol Index: ', suduko_y)
            print('\tRow Index: ', suduko_x)

            for value in range(len(double_index)):
                print('\t', array_3d[suduko_y[value]][suduko_x[value]])

            print('\n\tBefore - |')
            for col_i in range(9):
                print('\t', ''.join(map(str, array_3d[col_i][row])))

            for value_removal in range(0, len(double_index), 2):

                for col in range(9):

                    if col == suduko_y[value_removal] or col == suduko_y[value_removal + 1]:
                        pass

                    else:
                        array_3d[col][row][double_index[value_removal][0]] = double_index[value_removal][0] + 1
                        array_3d[col][row][double_index[value_removal][1]] = double_index[value_removal][1] + 1

                        continue

            print('\n\tAfter - |')
            for col_i in range(9):
                print('\t', ''.join(map(str, array_3d[col_i][row])))
    print()
    return array_3d


def isolate_double_by_square(array_3d):
    """

    :param array_3d:
    :return:
    """

    for y in range(0, 3):
        for x in range(0, 3):

            double_index = []
            suduko_y = []
            suduko_x = []

            for sub_y in range(3):
                for sub_x in range(3):

                    coordinate_y = y * 3 + sub_y
                    coordinate_x = x * 3 + sub_x
                    # print('\n\tStart Calculations for', coordinate_y, coordinate_x)
                    # print('\t\ty:', coordinate_y, 'x:', coordinate_x, '==',  array_3d[coordinate_y][coordinate_x])

                    if array_3d[coordinate_y][coordinate_x].count(0) == 2:

                        # print('\t\t\tMatch value contains two zeros')
                        # print('\t\t\t\tchecking sub_coordinates')

                        for double_validation_sub_y in range(3):
                            for double_validation_sub_x in range(3):
                                sub_coordinate_y = y * 3 + double_validation_sub_y
                                sub_coordinate_x = x * 3 + double_validation_sub_x

                                if coordinate_y == sub_coordinate_y and coordinate_x == sub_coordinate_x:
                                    pass

                                elif array_3d[coordinate_y][coordinate_x] == \
                                        array_3d[sub_coordinate_y][sub_coordinate_x]:
                                    # print("\t\t\t\t\tMatch =", sub_coordinate_y, sub_coordinate_x,
                                    #       array_3d[sub_coordinate_y][sub_coordinate_x])

                                    double_index += [[i for i, x in enumerate(array_3d[coordinate_y][coordinate_x])
                                                      if x == 0]]

                                    suduko_y += [coordinate_y]

                                    suduko_x += [coordinate_x]

                                else:
                                    continue

            if len(double_index) == 0 or len(double_index) % 2 != 0:
                # print('\n\n\n HERE \n\n\n')
                # print('\t No Values to adjust')

                # todo move the zip function here, then count in 2's to see if there are matching pairs, if not delete index 1
                # If the value error occurs when there is only one option you will need to add a condition to work through
                # each list to make sure that the conditions are met. aka there are two indexs with the same value.

                pass

            else:
                # print('\n\n\n True \n\n\n')

                double_index, suduko_y, suduko_x = zip(*sorted(zip(double_index, suduko_y, suduko_x)))

                # print('\n\t0 Index:   ', double_index)
                # print('\tCol Index: ', suduko_y)
                # print('\tRow Index: ', suduko_x)

                for value_removal in range(0, len(double_index), 2):

                    for sub_y_2 in range(3):
                        for sub_x_2 in range(3):
                            coordinate_y = y * 3 + sub_y_2
                            coordinate_x = x * 3 + sub_x_2

                            if coordinate_y == suduko_y[value_removal] and \
                                    coordinate_x == suduko_x[value_removal]:
                                    pass

                            elif coordinate_y == suduko_y[value_removal + 1] and \
                                    coordinate_x == suduko_x[value_removal + 1]:
                                    pass

                            else:
                                # print('\n\t\tStart Calculations for', coordinate_y, coordinate_x)
                                # print('\t\t\ty:', coordinate_y, 'x:', coordinate_x, '==',
                                #       array_3d[coordinate_y][coordinate_x])

                                array_3d[coordinate_y][coordinate_x][double_index[value_removal][0]] = \
                                    double_index[value_removal][0] + 1

                                array_3d[coordinate_y][coordinate_x][double_index[value_removal][1]] = \
                                    double_index[value_removal][1] + 1

                                continue


instance_count = 1
while True:
    print("===================================================================================================")
    print("STARTING INSTANCE", instance_count)
    # store_suduko = copy.deepcopy(Suduko_Resulting_Matrix)

    """=============================================================================================================="""

    print("ROWS")
    Suduko_Cube = by_row(Suduko_Resulting_Matrix, Suduko_Cube)
    print_cube_2(Suduko_Cube)

    print("Columns")
    Suduko_Cube = by_column(Suduko_Resulting_Matrix, Suduko_Cube)
    print_cube_2(Suduko_Cube)

    print("Squares")
    Suduko_Cube = by_square(Suduko_Resulting_Matrix, Suduko_Cube)
    print_cube_2(Suduko_Cube)

    """=============================================================================================================="""

    print("Isolating Doubles by row")
    Suduko_Cube = isolate_double_by_row(Suduko_Cube)
    print_cube_2(Suduko_Cube)

    print("Isolating Doubles by column")
    Suduko_Cube = isolate_double_by_column(Suduko_Cube)
    print_cube_2(Suduko_Cube)

    print("Isolating Doubles by square")
    isolate_double_by_square(Suduko_Cube)
    print_cube_2(Suduko_Cube)
    isolate_double_by_square(Suduko_Cube)

    input('Enter to Continue')

    """=============================================================================================================="""

    print("Isolate Zeros")
    isolate_zeros(Suduko_Resulting_Matrix, Suduko_Cube)
    print_suduko(Suduko_Resulting_Matrix)

    # input('pause')

    """=============================================================================================================="""

    """=============================================================================================================="""

    count = 0
    for y in range(9):
        if Suduko_Resulting_Matrix[y].count(0) == 0:
            count += 1
        else:
            continue
    if count == 9:
        print("Computation Completed")
        break
    print("===================================================================================================")
    time.sleep(0.5)
    instance_count += 1





print("===================================================================================================")
print("\nResult!".upper())

for y in range(9):
    print(Puzzles.Suduko_Input_Matrix_1[y], '  >  ', Suduko_Resulting_Matrix[y])

input("Enter to Exit:")