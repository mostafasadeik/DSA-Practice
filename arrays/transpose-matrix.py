# Arrays (Transpose Matrix)
# Given a matrix, the task is to find the transpose of the matrix. 
# The transpose of a matrix is obtained by swapping the rows and columns of the matrix.
# The function transposeMatrix takes a matrix as input and returns its transpose.
# The time complexity of this solution is O(n * m), where n is the number of rows and m is the number of columns in the matrix.
# The space complexity is O(n * m) as well, since we are creating a new matrix to store the transposed values.
# Approach:
# 1. Initialize an empty list to store the transposed matrix.
# 2. Iterate through the columns of the original matrix.
# 3. For each column, create a new row in the transposed matrix.
# 4. Iterate through the rows of the original matrix and append the corresponding element to the new row.
# 5. Append the new row to the transposed matrix.
# 6. Return the transposed matrix.


def transposeMatrix(matrix):
  transposedMatrix = []
  for col in range(len(matrix[0])):
        newRow =[]
        for row in range(len(matrix)):
            newRow.append(matrix[row][col])
        transposedMatrix.append(newRow)
        
  return transposedMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transposeMatrix(matrix))