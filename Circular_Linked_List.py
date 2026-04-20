# CIRCULAR LINKED LIST:-
                # Linear data structure in which the next of last node point the reference of first node in the linked list.


# PRACTICE:

# 1. Define a class Node to describe a  node of a circular linked list.

class Node:
    def __init__(self,item =None, next=None):
        self.item = item 
        self.next = next

# Define a class CLL to impliment Circular List with __init__() method to create and initrialize last refrence variable.

class CLL:
    def __init__(self,last = None):
        self.last = last

# 3. Define a method is_empty() to check if the linked list is empty in CLL class.

    def is_empty(self):
        return self.last == None
    
    def insert_at_start(self,data):
        