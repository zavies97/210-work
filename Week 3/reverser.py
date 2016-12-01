#function reverses a user enetered sentence. the sentence is stored in an array
#which is sent to the function.
#the array is reversed by storing each value in a secind array, adding the next
#value from the initial array before the rest of the existing reversed array
def reverser(array):
    reverse = []
    for i in range(0, len(array)):
        reverse = [array[i]] + reverse
    return reverse
        

#user entered sentence to split into its individual words. this is stored as an
#array to pass to the function
string = str(input("Sentence: "))
array = string.split(" ")

reverse = reverser(array)

#prints sentence backwards
for i in range(0, len(reverse)):
    print(reverse[i], end =" ")


# BigO = 2n + 5 + 2n = 4n = n
