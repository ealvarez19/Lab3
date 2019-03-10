# Author: Emmanuel Alvarez 
# Instructor: Olac Fuentes
# Last modified March 10, 2019
# The objective of this lab is to make different operations using a binary tree like
# create a balaced binary tree from a ordered list and viceversa, find a number in a 
# binary tree without using recursion calls, and print a binary tree level by level
class BST(object):

    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right      
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T

def Delete(T,del_item):
    if T is not None:
        if del_item < T.item:
            T.left = Delete(T.left,del_item)
        elif del_item > T.item:
            T.right = Delete(T.right,del_item)
        else:  # del_item == T.item
            if T.left is None and T.right is None: # T is a leaf, just remove it
                T = None
            elif T.left is None: # T has one child, replace it by existing child
                T = T.right
            elif T.right is None:
                T = T.left    
            else: # T has two chldren. Replace T by its successor, delete successor
                m = Smallest(T.right)
                T.item = m.item
                T.right = Delete(T.right,m.item)
    return T
         
def InOrder(T):
    # Prints items in BST in ascending order
    if T is not None:
        InOrder(T.left)
        print(T.item,end = ' ')
        InOrder(T.right)
  
def InOrderD(T,space):
    # Prints items and structure of BST
    if T is not None:
        InOrderD(T.right,space+'   ')
        print(space,T.item)
        InOrderD(T.left,space+'   ')
  
def SmallestL(T):
    # Returns smallest item in BST. Returns None if T is None
    if T is None:
        return None
    while T.left is not None:
        T = T.left
    return T   
 
def Smallest(T):
    # Returns smallest item in BST. Error if T is None
    if T.left is None:
        return T
    else:
        return Smallest(T.left)

def Largest(T):
    if T.right is None:
        return T
    else:
        return Largest(T.right)   

def Find(T,k):
    # Returns the address of k in BST, or None if k is not in the tree
    if T is None or T.item == k:
        return T
    if T.item<k:
        return Find(T.right,k)
    return Find(T.left,k)
    
def FindAndPrint(T,k):
    f = Find(T,k)
    if f is not None:
        print(f.item,'found')
    else:
        print(k,'not found')
        
def sumTree(T):
    if T is not None:
        return T.item + sumTree(T.left) + sumTree(T.right)
    if T is None:
        return 0
    
def findDepth(T,k):
    if T is None or T.item == k:
        return 0
    if T.item<k:
        return 1 + findDepth(T.right,k)
    return 1 + findDepth(T.left,k)
    #if T.left
    
def Search(T,k): ################################## Search method without recursion calls
    temp = T
    while temp is not None:
        if k == temp.item:
            return True
        elif k < temp.item:
            temp = temp.left # search on the left side of the tree
        elif k > temp.item:
            temp = temp.right # search on the right side of the tree
    return False
    
def BuildBalancedTree(B): ######################## Build a Tree from an ordered list
    if not B:
        return None
    middle = len(B)//2
    T = BST(B[middle]) #Creates the root node
    leftTree = B[:middle] # splits the list and takes as value the first half
    rightTree = B[middle+1:] # takes the values of the second half of the list
    #print(T.item)
    #print(leftTree)
    T.left = BuildBalancedTree(leftTree)
    T.right = BuildBalancedTree(rightTree)
    return T
    
def CreateSortedList(T):######################### Creates a list with ordered elements from a BT
    if T is None:
        return []
    return CreateSortedList(T.left) + [T.item] + CreateSortedList(T.right)
    
def findHeight(T): # Method that calculates the height of the binary tree 
    if T is None:
        return 0
    else:
        #finds the largest path
        left = findHeight(T.left)
        right = findHeight(T.right)
        print('left',left)
        print ('right',right)
        #returns the longest path's length
        if left > right:
            return left + 1 
        else:
            return right + 1

def printByDepth(T): # Prints integers level by level
    if T is None:
        return
    queue = []
    queue.append(T)
    while len(queue) > 0: # Until it is empty
        print(queue[0].item)      
        temp = queue.pop(0) # takes the root and remove it from the queue
        #print('temp ', temp.item)        
        if temp.left is not None:
            #print('left', temp.left.item)
            queue.append(temp.left)# enqueue if it has left child
        if temp.right is not None:
            queue.append(temp.right)#enqueue if it has right child
            #print('right',temp.right.item)
        
        
  
# Code to test the functions above
T = None
A = [70, 50, 90, 130, 150, 40, 10, 30, 100, 180, 45, 60, 140, 42,190]
#A = [70,50,90,130,150]
for a in A:
    T = Insert(T,a)
    
InOrder(T)
print()
InOrderD(T,'')
print()

print('Is integer in the tree?')
print(Search(T,180))

B = [10,20,30,40,50,60,70,80,90,100]
C = []
B = B + C
print('List ordered: ',B)
print('Balanced binary tree created from ordered list: ')
InOrderD(BuildBalancedTree(B), ' ') # draws the sorted tree created previously
print('List created from a ordered binary tree:')
print(CreateSortedList(T))
print('Print integers level by level from binary tree: ')
#print('height:',findHeight(T))
printByDepth(T)
#print(ListByDepth(T))



