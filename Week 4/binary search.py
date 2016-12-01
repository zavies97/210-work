#function carries out a binary search to find a value between two parameters
#if a value is not found, it us stated and returned as False
#otheriwse the program resets with half of the previous array depending on which
#part of the array midpoint is the lowest and highest parameter.
#this repeats with smaller arrays until a value in the parameter is found.
def BinarySearch(low, high, array):
    if len(array) == 0:
        return False
    else:
        print(array)
        midpoint = len(array)/2
        midpoint = int(midpoint)
        if array[midpoint] < high and array[midpoint] > low:
            return True
        elif array[midpoint] < low:
            del array[0:midpoint]
            return BinarySearch(low, high, array)
        elif array[midpoint] > high:
            del array[midpoint:len(array)]
            return BinarySearch(low, high, array)
        else:
            return False

#setting the valuesand outputting whether the parameters fit a value in the array
low = 10
high = 14
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11]
print(BinarySearch(low, high, array))


#Big(O) = log(n)
