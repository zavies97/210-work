#function to find the longest sequence in an array.
#the stated values are set to null as the program starts. the program then
#searches through the requested sequence until a value smaller than the previous
#value is found (in this case, if i+1 < i). When this happens, the new sub sequence
#is stored temporarily along with the new length (BUT ONLY IF IT IS LARGER THAN THE
#PREVIOUS SUBSEQUENCE)
#Once the sequence is fully checked, the largest subsequence is returned along with
#the length of the sequence
def sequenceFinder(array):
    sequence = []
    counter = 0
    sequence.append(array[0])
    
    for i in range(0, len(array)):
        print(sequence)
        
        if i == len(array)-1:
            return counter, longestSequence
        
        elif array[i+1]> array[i]:
            sequence.append(array[i+1])
            
        else:
            if counter < len(sequence):
                counter = len(sequence)
                longestSequence = []
                for i in range(0, len(sequence)):
                    longestSequence.append(sequence[i])
                sequence =[]
                sequence.append(array[i+1])

#stating the sequence to test and calling the result fo the function
array = [1, 3, 4, 6, 2, 4, 7, 9, 11, 2, 3, 5]

print(sequenceFinder(array))
                
            
