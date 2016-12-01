#function to remove vowels from a string. counte ris passed as it increases
#depending on whether the previous letter is removed or not.
#if value is removed, counte ris unchanged in the recursion.
#otherwise it is increased by 1 and the process continues until string is voweless
def vowelRemove(string, counter):
    if counter == len(string):
        return string
    else:
        if string[counter] == "a" or string[counter] == "e" or string[counter] == "i" or string[counter] == "o" or string[counter] == "u":
            string = string.replace(string[counter], "")
            return(vowelRemove(string, counter))
        else:
            return(vowelRemove(string, counter+1))

#user requested string to remove vowels from. result of recursion is printed out
string = str(input("word"))
string = string.lower()

answer = vowelRemove(string, 0)

print(answer)
