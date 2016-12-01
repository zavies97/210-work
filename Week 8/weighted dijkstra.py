#The weighted class
class weighted:
    def __init__(self):
        self.connect = {}
        self.weight = {}
        self.edge = {}
        self.list = []

    #this inserts an existing conenction at the beginning of the program 
    def insertconnect(self, key, values):
        self.connect[key] = values

    #this adds weights and edges to two new dictionaries which are used
    #to reference each connection to its relevant weight via using the same key
    def insertedge(self, value1, value2, size):
        self.list.append(size)
        self.edge[len(self.list)] = [value1, value2]
        self.weight[len(self.list)] = size

    #this prints out every connection per node, then every weight per connection
    #The extra created list(self.list) is used to keep track of the connections and their
    #weights, as an index list.
    def output(self):
        for i in range(1, len(self.connect)+1):
            print(i, ": ", self.connect[i])
        print("\n")
        print("Weights:\n")
        for i in range(1, len(self.weight)+1):
            print("Connection", self.edge[i], ":", self.weight[i])

    #adds a new connection and weight for said connection after the program has added its initial connections
    def addEdge(self, value1, value2, size):
        self.list.append(size)
        self.connect[value1].append(value2)
        self.connect[value2].append(value1)
        self.edge[len(self.list)] = [value1, value2]
        self.weight[len(self.list)] = size

#Theoretically this should work, however python wont let me use the class lists and
#dictionaries for this function, so it wont run and i cant test it.
#However the function is supposed to run so that the first time it is run each array and dictionary
#is created. The counter is created too. After this, the start value is added to the visited list
#If the connections from the start node is equal to 1 then the counter is set to the weight of the connection.
#If the destination is found the weight as counter is returnedand, otherwise the program continues with the
#new start point set as the new node. the previous node now should not be called again.
#If the node has more than one connection however, the function checks whether a connection has been previously visited,
#if it has and there are still more unvisited nodes, the remaining connections are found and added to
#the toVisit list. Here the weights of these connections are checked to make sure the smallest one is collected.
#Theoretically the lmarger node/s should still be stored just in case however the way the algorithm is set up
#in this program means that that is not necessary.
#Whichever node is smaller is used as the next start node and the program continuesuntil the smallest path is found.        
def Dijkstra(start, destination, first):

    test = weighted()
    if first == True:
        visited = []
        toVisit = []
        dictSizes = {}
        counter = 0
        first = False
    visited.append(start)
    if len(test.connect[start])+1 == 1:
        toVisit.append(test.connect[start][i])
        temp = toVisit.pop(0)
        visited.append(temp)
        for i in range(0, len(test.list)):
            if start in test.edge[i]:
                dictSizes[test.weight[i]] = test.edge[i]
                counter+= test.weight[i]
                if temp == destination:
                    break
                Dijkstra(temp, destination, first)
        
    else:
        for i in range(1, len(test.connect[start])+1):
            counter2 = 0
            for j in range(0, i):
                temp = toVisit.pop(j)
                for k in range(1, len(test.connect[temp]) + 1):
                    if test.connect[temp][k] not in visited or test.connect[temp][k] not in toVisit:
                        toVisit.append(test.connect[temp][k])
                        for l in range(0, weighted.list):
                            if test.connect[temp][k] in test.edge[l]:
                                if counter2 < test.weight[l]:
                                    storage = l
                                    counter2 = test.weight[l]
                        
                        dictSizes[test.weight[storage]] = test.edge[storage]
                        counter+=test.weight[storage]
                        if temp == destination:
                            break
                        Dijkstra(temp, destination, first)
                    
        
    
    return counter

#The values to be entered into the weighted structure and to start off each function
if __name__ == '__main__':
    data = weighted()
    data.insertconnect(1, [3])
    data.insertconnect(2, [4, 5])
    data.insertconnect(3, [1])
    data.insertconnect(4, [2, 5])
    data.insertconnect(5, [2, 4])
    data.insertedge(1, 3, 7)
    data.insertedge(2, 4, 9)
    data.insertedge(2, 5, 4)
    data.insertedge(4, 5, 2)
    data.addEdge(2, 3, 6)
    data.output()

    Dijkstra(1, 4, first = True)
