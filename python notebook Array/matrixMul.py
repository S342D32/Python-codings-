# Function to get matrix input from the user
def get_matrix(rows, cols):
    matrix = []
    print(f"Enter the elements of a {rows}x{cols} matrix row-wise:")
    for i in range(rows):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

# Function to multiply two matrices
def multiply_matrices(X, Y):
    result = [[0 for _ in range(len(Y[0]))] for _ in range(len(X))]
    for i in range(len(X)):
        for j in range(len(Y[0])):
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

# Input dimensions for the first matrix
rows_X = int(input("Enter the number of rows for the first matrix: "))
cols_X = int(input("Enter the number of columns for the first matrix: "))

# Input dimensions for the second matrix
rows_Y = int(input("Enter the number of rows for the second matrix: "))
cols_Y = int(input("Enter the number of columns for the second matrix: "))

# Ensure the matrices can be multiplied
if cols_X != rows_Y:
    print("Error: The number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    # Get the matrices from the user
    X = get_matrix(rows_X, cols_X)
    Y = get_matrix(rows_Y, cols_Y)

    # Multiply the matrices
    result = multiply_matrices(X, Y)

    # Print the result
    print("The resulting matrix is:")
    for row in result:
        print(row)
