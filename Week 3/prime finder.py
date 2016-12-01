#checks whether the requested value is prime or not with base cases to
#recursively continue the program if needed.
#if a result is not found, the program continues until x == counter (recursively)
#and then states that the user entered value is not prime, else it is stated as prime
def primeCheck(counter, x):

    if x > 1:
        if x == counter:
            return "is prime"
        elif (x % counter) == 0:
            return "is not prime"
        else:
            return (primeCheck(counter+1, x))
    else:
        return "is not prime"

#initial setup and requesting a value to test from the user
counter = 2

check = int(input("Number"))
answer = primeCheck(counter, check)
print(answer)
