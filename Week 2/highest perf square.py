#function calculates the highest perfect square number within a user defined
#parameter (0 to whatever the user specifies)
def highestPerfSquare(Value):
    counter = 1
    square = counter*counter
    while square <= Value:
        if square == Value:
            return counter
        counter+=1
        square = counter*counter
    return counter

parameter = int(input("Enter parameter >> "))
print(highestPerfSquare(parameter)-1)
        
        
