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

# In class CLL, define a method to print all the elements of the list.

    def print_list(self):
        if not self.is_empty():
            temp = self.last.next
            while temp != self.last:
                print(temp.item,end=" ")
                temp = temp.next
            print(temp.item)

    def delete_first(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                self.last.next = self.last.next.next

    def delete_last(self):
        if not self.is_empty():
            if self.last.next == self.last:
                self.last = None
            else:
                temp = self.last.next
                while temp.next != self.last:
                    temp = temp.next
                temp.next = self.last.next
                self.last = temp

    def delete_item(self,data):
        if not self.is_empty():
            if self.last.next == self.last:
                if self.last.item == data:
                    self.last = None
            else:
                if self.last.next.item ==  data:
                    self.delete_first()
                else:
                    temp = self.last.next

                    while temp != self.last:
                        if temp.next == self.last:
                            if self.last.item == data:
                                self.delete_last()
                                break
                        if temp.next.item == data:
                            temp.next = temp.next.next
                            break
                        temp = temp.next

# In class CLL, implement iterator for CLL to access all the elements of the list in a sequence.

    def __iter__(self):
        if self.last == None:
            return CLLIterator(None)
        else:
            return CLLIterator(self.last.next)
         
class CLLIterator:
    def __init__(self,start):
        self.current = start
        self.start = start
        self.count = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.start and self.count == 1:
            raise StopIteration
        else:
            self.count=1
        data = self.current.item
        self.current = self.current.next
        
        return data

cll = CLL()
cll.insert_at_start(10)
cll.insert_at_start(20)
cll.insert_at_last(0)
cll.insert_at_last(100)
cll.insert_after(cll.search(10),13)
for x in cll:
    print(x,end=" ")
print()
                                






               