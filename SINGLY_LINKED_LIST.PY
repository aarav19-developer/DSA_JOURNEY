# LIST:-
#      Is a linear combination of data items also knwom as List Items.
#      Ex- list of marks (13,22,8,7,19)

# NODE:
      #  - A node is a container that holds data and one or more links/pointers to other nodes.

class Node:
    def __init__(self,item = None,next = None):
        self.item = item
        self.next = next

# SINGLY LINKED LIST:
              #   Singly linkd list is a linear data structure.
              # It can grow and shrink.
              # It is known as singly linked because each node has single linked with next node.

# OPERATIONS ON SLL:

# 1.) Insertion
# 2.) Deletion
# 3.) Is_empty
# 4.) traverse

# PRACTICE:-

# 1. What is class node to describe of a singly linked list.

class Node:
    def __init__(self, item=None,next = None):
        self.item = item
        self.next = next
# 2. Define a class SLL to impliment Singly Linked List with __init__() method to create and initialise stat reference variable.

class SLL:
    def __init__(self,start = None):
        self.start = start

# 3. Define a method is _empty() to check if the linked list is empty in SLL class.


    def is_empty(self):
        return self.start == None
    
# 4. In class SLL, define a method insert_at_start() to insert an element at the starting of the list.
    def insert_at_start(self,data):
        n = Node(data,self.start)
        self.start = n

# 5.  In class SLL, define a method insert_at_last() to insert an element at the starting of the list.

    def insert_at_last(self,data):
        n1 = Node(data)
        if not self.is_empty():
            temp = self.start
            while temp.next is not None:
                temp = temp.next
            temp.next = n1

        else:
            self.start = n1

# 6. In class SLL, define a method search() to find the node with specified element value.

    def search(self,data):
        temp = self.start
        while temp is not None:
            if temp.item == data:
                return temp
            temp = temp.next

# 7.  In class SLL, define a method insert_after() to insert a new code after a given node in a list.

    def insert_after(self, temp, data):
        if temp is not None:
            s = Node(data,temp.next)
            temp.next = s

# 8.  In class SLL, define a method to print all the elements of the list.

    def print_list(self):
        temp = self.start
        while temp is not None:
            print(temp.item,end=" ")
            temp=temp.next


# 9.  In class SLL, define a method delete_first() / delete_last / delete_item to delete first element from the list.

    def delete_first(self):
        if self.start is not None:
            self.start = self.start.next
    
    def delete_last(self):
        if self.start is None:
            pass
        elif self.start.next is None:
            self.start = None
        else:
            temp = self.start
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
    
    def delete_item(self,data):
        if self.start is None:
            pass

        elif self.start.next is None:
            if self.start.item == data:
                self.start = None

        else:
            temp = self.start
            if temp.item == data:
                self.start = temp.next
            else:
                while temp.next is not None:
                    if temp.next.item == data:
                        temp.next = temp.next.next
                        break
                    temp = temp.next

    def __iter__(self):
        return SLLIterator(self.start)

# 10. In a class SLL, implement iterator for SLL to access all the elements of the list in a sequence.

class SLLIterator:
    def __init__(self, start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data
        

myList = SLL()
myList.insert_at_start(20)
myList.insert_at_start(100)
myList.insert_at_last(10)
myList.insert_after(myList.search(20),25)
myList.print_list()
myList.delete_item(20)
print()
myList.delete_first()
print()

for x in myList:
    print(x,end=" ")
    
print()


# LIMITATION OF SINGLY LINKED LIST:

# You can not go instantly to the previous node. You have to start from the beginning to go to the particular node.
# There is a need of traversing if we have to add a node at the last.


    







