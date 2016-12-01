#importing allows random shuffling of list
import random

#initial set up of list andcounter to make sure all requested values can be
#entered by user. Entry of values is in a closed loop specified by the user
y=0
array = []

x = int(input("How many numbers do you want to input? >> "))

while y < x:
    number = int(input("Insert number >> "))
    array.append(number)
    y+=1

#the backup is used to compare to the initial array in case the result is in
#the same order as the initial list
backup = array

#user specifies the amount of shuffles, this has to be longer than the list of values
#so every value is shuffled at least once
shufflenum = int(input("How many shuffles do you want to do? >> "))
while shufflenum < len(array):
    shufflenum = int(input("Has to be longer than list of numbers, please insert again >> "))

#shuffle function. all values are shuffled once with a random value specified by the result of numswap
#(numswap is set to a random list index thatis not equal to the current value to be swapped, and continues
#to produce values until a new value is chosen). 
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

#second shuffle. This will shuffle random values in the list after the previous function is run until
#the requested number of shuffles are reached
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

#calls both functions shuffling the requested amoutn of times
shuffleall(array)
for i in range(0, shufflenum - len(array)):
    shuffler(array)

#if the shuffled list is identical to before shuffling, the process is repeated until a new list is produced
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

