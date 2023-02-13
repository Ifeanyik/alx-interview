#!/usr/bin/python3
'''this script totates a 2d matrix'''


def rotate_2d_matrix(matrix):
    '''This function rotates a 2d matrix'''
    temp_matrix = [[el for el in row] for row in matrix]
    len_matrix = len(matrix)
    for i in range(0, len_matrix):
        for j in range(len_matrix - 1, -1, -1):
            matrix[j][i] = temp_matrix[i][j]
    for i in range(len_matrix):
        temp_list = []
        for j in range(len_matrix - 1, -1, -1):
            temp_list.append(matrix[i][j])
        for j in range(len_matrix):
            matrix[i][j] = temp_list[j]
