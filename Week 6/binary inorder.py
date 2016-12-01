#FUNCTION CREATED WAS THE IN_ORDER FUNCTION ITERATIVELY, WHICH IS NOT AS EFFICIENT
#AS RECURSIVELY
class BinTreeNode(object):
 
    def __init__(self, value):
        self.value=value
        self.left=None
        self.right=None
        
def tree_insert(tree, item):
    if tree==None:
        tree=BinTreeNode(item)
    else:
        if item < tree.value:
            if tree.left==None:
                tree.left=BinTreeNode(item)
            else:
                tree_insert(tree.left,item)
        else:
            if tree.right==None:
                tree.right=BinTreeNode(item)
            else:
                tree_insert(tree.right,item)
    return tree
 
def postorder(tree):
    if tree.left!=None:
        postorder(tree.left)
    if tree.right!=None:
        postorder(tree.right)
    print(tree.value)
 
#The function caries out the in_order function iteratively (without recursion)
#This is carried out to sort the random tree from smallest value to largest
# The function checks whether the tree is empty. if it is, the process ends.
#If it is not empty and there are values on the tree they are added to a stack
#and then the values on the left side fo the tree are added to the stack until
#the tree is empty. At this pointif the current stack of values is not none,
#the function outputs the smallest value and removes it from the stack.
#this repeats until all valuesa are removed.
def in_order(tree):

##    if tree.left!=None:
##        in_order(tree.left)
##    print(tree.value)
##    if tree.right!=None:
##        in_order(tree.right)

#Above is the recursive version of the following function. This does not run as
#this is not the iterative function i created.
    stack = []
    empty = 0

    while empty == 0:
        if tree is not None:
            stack.append(tree)
            tree = tree.left

        else:
            if len(stack) > 0:
                tree = stack.pop()
                print(tree.value)
                tree = tree.right
                
            else:
                empty = 1


 
if __name__ == '__main__':
   
    t = tree_insert(None,6)
    tree_insert(t,10)
    tree_insert(t,5)
    tree_insert(t,2)
    tree_insert(t,3)
    tree_insert(t,4)
    tree_insert(t,11)
#this calls the function to order the tree specified
    in_order(t)
