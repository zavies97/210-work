#IMPLEMENTATION IS THE NODE DELETE FUNCTION

class Node(object):
      def __init__(self, value):
            self.value=value
            self.next=None
            self.prev=None

class List(object):
      def __init__(self):
            self.head=None
            self.tail=None
      def insert(self,n,x):
    #Not actually perfect: how do we prepend to an existing list?
            if n!=None:
                  x.next=n.next
                  n.next=x
                  x.prev=n
            if x.next!=None:
                  x.next.prev=x              
            if self.head==None:
                  self.head=self.tail=x
                  x.prev=x.next=None
            elif self.tail==n:
                  self.tail=x
                  
#function tests whether the requested list index is in the list. if there is
#nothing in the list, the function ends.
#if the value is the beginning of the list (the head) then t is removed and the
#function ends
#if the value is not at the beginning of the list, the for loop specifies whether
#the node is correct. if it is, the value is replaced by the next node in the list
#and the function ends. otherwise the value of n increases and tests the next node
#if no index is found an error occurs as the index is greater than the length of the list
      def delete(self, n, x):
            if self.head == None:
                  return
            if x == 0:
                  self.head = n.next
                  n = None
                  return
            
            for i in range(x):
                  if i == x-1:
                        if n.next.next != None:
                              n.next.next.prev = n
                              n.next = n.next.next
                              return
                        else:
                              n.next = None

                              
      def display(self):
            values=[]
            n=self.head
            while n!=None:
                  values.append(str(n.value))
                  n=n.next
            print("List: " , ",".join(values))
    
if __name__ == '__main__':
    l=List()
    l.insert(None, Node(4))
    l.insert(l.head,Node(6))
    l.insert(l.head,Node(8))
    l.display()
    #calls the function with a specified index (in this case, the head of the list)
    l.delete(l.head, 0)
    l.display()
