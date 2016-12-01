import random

y=0
array = []

x = int(input("How many numbers do you want to input? >> "))

while y < x:
    number = int(input("Insert number >> "))
    array.append(number)
    y+=1

backup = array

shufflenum = int(input("How many shuffles do you want to do? >> "))
while shufflenum < len(array):
    shufflenum = int(input("Has to be longer than list of numbers, please insert again >> "))

def shuffleall(value):
    for i in range(0, len(value)):
        numswap = random.randrange(0, len(array))
        while numswap == i:
            numswap = random.randrange(0, len(array))
        numout = value[i]
        value[i] = value[numswap]
        value[numswap] = numout
        print (value)
    return value
     
def shuffler(value):
    numswap1 = random.randrange(0, len(array))
    numswap2 = random.randrange(0, len(array))
    while numswap1==numswap2:
        numswap2 = random.randrange(0, len(array))
    numout = value[numswap1]
    value[numswap1] = value[numswap2]
    value[numswap2] = numout
    print (value)
    return value
    
shuffleall(array)
for i in range(0, shufflenum - len(array)):
    shuffler(array)

if array == backup:
    shuffleall(array)
    for i in range(0, shufflenum - len(array)):
        shuffler(array)

'''
3.a. The algorithm has defined inputs, entered by the user, and defined outputs in print
statements. All of those are clearly defined and labelled to easily ell them
apart from the other variables
3.b. Yes the program terminates after the shuffles are fully completed, showing all
shuffles and the end result.
3.c. Yes it is specifid in a clear and concise manner. all variables are labelled
to make the processes easier to understand too.
3.d. The program shuffles every number. some numbers end up in the same place
in the end, however the end result is never equal to the entered list order.
'''


#O(4N + 2N + 2N + 2N^2 + 4N + 4N + 2N^2 + 5N + 2N + 2N^2 + 4N + 4N + 2N^2 + 5N) = O(36N + 8N^2) = O(N^2)

