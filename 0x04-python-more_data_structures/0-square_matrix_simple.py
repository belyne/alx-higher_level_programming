#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            # Compute the square of each element and append it to the new row
            new_row.append(element ** 2)
        # Append the new row to the new matrix
        new_matrix.append(new_row)

    return new_matrix
