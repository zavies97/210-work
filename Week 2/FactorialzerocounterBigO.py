def factorial(factor):
    i=5
    counter = 0
    while i<=factor:
        counter = counter + factor//i
        i = i*5
    return counter

def factorialValue(factor):
    if factor == 0:
        return 1
    
    elif factor>0:
        return factor *(factorialValue(factor-1))


number = int(input("Enter number >> "))

result = factorialValue(number)
solution = factorial(number)

print("The factorial of", number, "is", result)
print("The number of trailing zeroes from the factorial of", number, "is", solution)


#O(3N+N) = O(4N)

    
    
'''
3.a. The algorithm has defined inputs and outputs, each unique and labelled to easily
tell them apart from the rest of the code.
3.b. Yes, after extensive errors. The recursiive function eneded a base statement
which had caused errors, and the program still breaks if you try to exceed the maximum
recursion capacity
3.c. yes it is specified in a clear and precise manner, all variables and functions are
labelled in a manner to make it easier to understand
3.d. yes unless you reach the recursion limit of 993 (unless you state a larger limit).
The program wont work for anything smaller than 4, as there are no trailing 0's for 4!,
3!, 2! or 1.
'''

