#!/urs/bin/python3
"""Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """Function to rotate the matrix"""
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return matrix


result = rotate_2d_matrix(matrix)

# Print the result
for row in result:
    print(row)
