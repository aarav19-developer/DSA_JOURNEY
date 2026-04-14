# DOUBLY LINKED LIST:-
                 # Doubly linked list is a linear data structure.

# ELEMENTARY OPERATIONS:
                # Insertion
                # Deletion
                # Traversing
                # Searching
                # Checking for empty list

# PRACTICE:

# Define a class Node to describe a node of a doubly linked list.

# class Node:
#     def __init__(self,prev=None,item= None,next=None):
#         self.prev = prev
#         self.item = item
#         self.next = next

# Define a class DLL to impliment Doubly Linked List with __init__( )method to create and initialize start refrence variable.

class DLL:
    def __init__(self,start = None):
        self.start = start

# In class DLL, define a method is_empty() to check if the lined list is empty in DLL class.

    def is_empty(self):
        return self.start == None
    
# In class DLL, define a method insert_at_start() to insert an element at the starting of the list.

    def insert_at_start(self,data):
        


    
