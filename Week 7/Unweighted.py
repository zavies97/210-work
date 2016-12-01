#global is here to make sure the visited is used in every array without stating it
#every time wihtout the risk of rewriting it during recursions.
global visited 

#This is a class. it contains one dictionary to store every connection between
#nodes. The node connection type is multidirectional as this is in my opinion
#a nicer way to create an unweighted data type.
class Unweighted:
    def __init__(self):
        self.connect = {}

    #the key and values refer to the initial connections that are being added.
    #this function is only run for the first entered values as an easier way
    #to carry out the addEdges function.
    def insert(self, key, values):
        self.connect[key] = values

    #This outputs all the data in a neat and tidy format, clearly stating what
    #each node is and what connections said node/s have
    def output(self):
        for i in range(1, len(self.connect)+1):
            print(i, ": ", self.connect[i])

    #This is the more complex insert function. It is used for new connections as
    #they are not added via a key but instead as a connection between two nodes.
    #It is stored for each key as a new connection node at the end of the
    #keys in the dictionary (e.g addeing 2, 3 adds 3 to the end of key 2 and vice versa
    def addEdge(self, value1, value2):
        self.connect[value1].append(value2)
        self.connect[value2].append(value1)

    #Breadth First Search function. It is not he most efficient program ever
    #as it is resting on the n^4 runtime however it works as it should.
    #The global variable visited is stated before calling this function and the
    #new and existing array are set to the start value initially.
    #the first check is whether a node has been visited. If it has, the function
    #breaks and moves on to the next for loop. otherwise if the relevant node is found
    #the program prints the list of visited nodes and the function ends.
    #however if the end node is not found, the node is added to the visited list
    #Before this process repeats, there is another process to check whether any node
    #is used as a start node already. When a new start value is found it is used as
    #the new start value, which should be the next value in the list visited
    #the new start is added to the list of previous start values and the process repeats
    #until the BFS is complete
    def BFS(self, start, value):
        global visited
        startvals = []
        visited.append(start)
        startvals.append(start)
        
        while 1:
            
            for i in range(1, len(self.connect[start])+1):
                for j in range(0, len(visited)):
                    if visited[j] == start:
                        break
                    
                if self.connect[start][i-1] == value:
                    visited.append(value)
                    print(visited)
                    return
                else:
                    if self.connect[start][i-1] not in visited:
                        visited.append(self.connect[start][i-1])
                    
            for i in range(0, len(visited)):
                for j in range(0, len(startvals)):
                    if visited[i] != startvals[j]:
                        break
                    
            start = visited[i]
            startvals.append(start)


    #Depth First Search (as opposed to BFS) was nicer to create but required
    #Recursion to do efficiently, so the global visited was needed here the most.
    #The function when initiated sets the value of current to start. Start is only used
    #to initialise the program, current is the real variable used.
    #Current is added to the visited list to keep track of all nodes visited, befire
    #checking whether the desired node is found or not. if it is found the function ends
    #otherwise if a new connection is found from the current node that hasnt been
    #visited or mentioned, it is used in the next runthrough. if after that recursion
    #the final value still isnt found, the next item in the list at the time is used.
    def DFS(self, start, value, current = None):

        global visited
        if current == None:
            current = start

        visited.append(current)
        
        if current == value:
            print("Found")
            print(visited)
            return
        

        for vertex in self.connect[current]:
            if vertex not in visited:
                self.DFS(start, value, vertex)      

#Caling the different class functions and sectipons of the code.
#Visited is stated before each function as it is global.
if __name__ == '__main__':
    data = Unweighted()
    data.insert(1, [3])
    data.insert(2, [4, 5])
    data.insert(3, [1])
    data.insert(4, [2, 5])
    data.insert(5, [2, 4])
    data.output()
    data.addEdge(2, 3)
    data.output()
    visited = []
    data.BFS(1, 2)
    visited = []
    data.DFS(5, 1)

        
