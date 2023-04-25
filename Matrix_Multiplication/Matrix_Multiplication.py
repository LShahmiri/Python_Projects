# Function to multiply two matricses
def multiply_matrics(a, b):
    # Get the dimention of matrix
    m = len(a)
    n = len(b[0])
    p = len(b)

    # Create a new matrix to store  the result
    result = [[0]*n for i in range(m)]

    # Multiply the matrices
    for i in range(m):
        for j in range(n):
            for k in range(p):
                result[i][j] += a[i][k]*b[k][j]

    return result


print('Enter matrix A: ')
# Get matrix A
a = []
for i in range(3):
    row = input().split()
    a.append([int(x) for x in row])
# Get matrix B
print("Enter matrix B:")
b = []
for i in range(3):
    row = input().split()
    b.append([int(x) for x in row])

# Multiply the matrices and print the result
result = multiply_matrics(a, b)
print(' Result: ')
for row in result:
    print(''.join([str(elem) for elem in row]))
