#function to add matrices together and return result
def matrixAdd(one, two, x):
    result = []
    for i in range(0, x):
        result.append([])
        for j in range(1, x+1):
            result[i].append([0])

        
    for i in range(0, x):
        for j in range(0, x):
            result[i][j] = one[i][j] + two[i][j]
    return result

#function to subtract one matrices from the other and return result
def matrixSubtract(one, two, x):
    result = []
    for i in range(0, x):
        result.append([])
        for j in range(1, x+1):
            result[i].append([0])
        
    for i in range(0, x):
        for j in range(0, x):
            result[i][j] = one[i][j] - two[i][j]
    return result

#function to multiply matrices and return a result
def matrixMultiply(one, two, x):
    result = []
    
    for i in range(0, x):
        result.append([])
        for j in range(1, x+1):
            result[i].append(0)

    for i in range(0, x):
        for j in range(0, x):
            for k in range(0, x):
                result[i][j] += one[i][j] * two[i][k]
            
    return result

#generated matrices created in an n*n form where the user specifies n.
#all values are 1-n for each row
x = int(input("matrices 1 length/width >> "))
matrixOne = []
for i in range(0, x):
    matrixOne.append([])
    for j in range(1, x+1):
        matrixOne[i].append(j)

#second matrix generated in the same way as the first
x = int(input("matrices 2 length/width >> "))
matrixTwo = []
for i in range(0, x):
    matrixTwo.append([])
    for j in range(1, x+1):
        matrixTwo[i].append(j)

#matrices calculation as requested carried out in several steps to simplify
#the complex calculation. The result is output afterwards
A = matrixAdd(matrixOne, matrixTwo, x)
B = matrixSubtract(matrixOne, matrixTwo, x)
C = matrixMultiply(matrixOne, matrixTwo, x)
D = matrixAdd(A, A, x)
result = matrixSubtract(C, D, x)

print(result)

    
