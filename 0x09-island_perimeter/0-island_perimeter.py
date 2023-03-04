#!/usr/bin/python3
'''This script finds the perimeter of
   a given island with its shape represented by
   1's in a list'''


def island_perimeter(grid):
    '''This function finds the perimeter of
       a given island with its shape represented by 1's
       in a list'''
    if grid == [] or type(grid) != list:
        return 0
    list_len = len(grid)
    row_len = len(grid[0])
    perimeter = 0
    for row in range(list_len):
        for elem in range(row_len):
            if grid[row][elem]:
                try:
                    if not grid[row - 1][elem]:
                        perimeter += 1
                    if not grid[row][elem - 1]:
                        perimeter += 1
                    if not grid[row][elem + 1]:
                        perimeter += 1
                    if not grid[row + 1][elem]:
                        perimeter += 1
                except IndexError:
                    pass
    return perimeter
