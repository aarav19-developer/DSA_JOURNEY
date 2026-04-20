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
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n


    def insert_at_last(self,data):
        n = Node(data)
        if self.is_empty():
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n


    def search(self,data):
        if self.is_empty():
            return None
        temp = self.last.next
        while temp != self.last:
            if temp.item == data:
                return temp
            temp = temp.next
        if temp.item == data:
            return temp
        return None
    

    def insert_after(self,temp,data):
        if temp is not None:
            n =Node(data,temp.next)
            temp.next = n
            if temp == self.last:
                self.last = n



               