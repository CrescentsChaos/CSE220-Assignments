#pylint:disable=C0303
#pylint:disable=C0301
#pylint:disable=C0116
#pylint:disable=C0115
#pylint:disable=C0103
#pylint:disable=W0613
#pylint:disable=W0107
class Node:
    def __init__(self, e, n, p):
        self.element = e
        self.next = n
        self.prev = p

class DoublyList:  
    def __init__(self, a):
        self.head=None
        if self.head is None:
            self.head=Node(None,None,None)
        self.head.next=self.head
        self.head.prev=self.head
        for element in a:
            node=Node(element , None,None)
            if self.head.prev==self.head:
                node.next=self.head.next
                node.prev=self.head
                self.head.next=node
                self.head.prev=node
            else:
                tail = self.head.next
                while tail.next is not self.head:
                    tail = tail.next
                tail.next=node
                node.next=self.head
                node.prev=tail
                self.head.prev=node
  
  # Counts the number of Nodes in the list
    def countNode(self):
        n=self.head.next
        i=0
        while n is not self.head:
            n = n.next
            i+=1
        return i
  
  # prints the elements in the list
    def forwardprint(self):
        n = self.head.next
        if n==None:
            print("Empty List")
        else:
            while n is not self.head:
                if n.next.element!=None:
                    print(n.element,end=",")
                if n.next.element==None:
                    print(n.element)
                n = n.next

  # prints the elements in the list backward
    def backwardprint(self):
        n = self.head.next
        if n==None:
            print("Empty List")
        else:
            n = self.head.prev
            while n is not self.head:
                if n.prev.element!=None:
                    print(n.element,end=",")
                if n.prev.element==None:
                    print(n.element)
                n = n.prev

  # returns the reference of the at the given index. For invalid index return None.
    def nodeAt(self, idx):
        if idx<0:
            print("Index Error")
            return None
        else:
            n=self.head.next
            i=0
            while i!=idx:
                n = n.next
                i+=1
            return n
  
  # returns the index of the containing the given element. if the element does not exist in the List, return -1.
    def indexOf(self, elem):
        n=self.head.next
        idx=1
        while elem!=n.element:
            n = n.next
            idx+=1
            if idx>=self.countNode():
                break
        if idx>self.countNode()-1:
            return -1
        else:
            return idx

 # inserts containing the given element at the given index Check validity of index. 
    def insert(self, elem, idx):
        if idx>self.countNode():
            print("Invalid Index")
        else:
            n = self.head.next
            i = 0
            newNode = Node(elem,None,None)
            while n != self.head:
                if i == idx:
                    prevNode = n.prev
                    prevNode.next = newNode
                    newNode.next = n
                    n.prev = newNode
                    newNode.prev = prevNode      
                i += 1
                n = n.next
            if i == idx:
                prevNode = n.prev
                prevNode.next = newNode
                newNode.prev = prevNode
                newNode.next = self.head
                self.head.prev = newNode
  # removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
    def remove(self, idx):
        if idx<0 or idx>(self.countNode()-1):
            print("Invalid index")
        elif idx==0:
            removed=self.nodeAt(idx).element
            self.head.next=self.head.next.next
            self.head.next.prev=self.head
        elif idx==(self.countNode()-1):
            removed=self.nodeAt(idx).element
            prev_tail=self.nodeAt(idx-1)
            prev_tail.next=self.head
            self.head.prev=prev_tail
        else:
            removed=self.nodeAt(idx).element
            remove_prev=self.nodeAt(idx-1)
            remove_next=self.nodeAt(idx+1)
            remove_prev.next=remove_next
            remove_next.prev=remove_prev
        return str(removed)
print("///  Test 01  ///")
a1 = [10, 20, 30, 40]
h1 = DoublyList(a1) # Creates a linked list using the values from the array

h1.forwardprint() # This should print: 10,20,30,40. 
h1.backwardprint() # This should print: 40,30,20,10. 
print(h1.countNode()) # This should print: 4

print("///  Test 02  ///")
# returns the reference of the at the given index. For invalid idx return None.
myNode = h1.nodeAt(2)
print(myNode.element) # This should print: 30. In case of invalid index This will print "index error"

print("///  Test 03  ///")
# returns the index of the containing the given element. if the element does not exist in the List, return -1.
index = h1.indexOf(30)
print(index) # This should print: 3. In case of element that 
#doesn't exists in the list this will print -1.

print("///  Test 04  ///")

a2 = [10, 20, 30, 40]
h2 = DoublyList(a2) # uses the  constructor
h2.forwardprint() # This should print: 10,20,30,40.  

# inserts containing the given element at the given index. Check validity of index.
h2.insert(85,0)
h2.forwardprint() # This should print: 85,10,20,30,40. 
h2.backwardprint() # This should print: 40,30,20,10,85.
print()
h2.insert(95,3)
h2.forwardprint() # This should print: 85,10,20,95,30,40.  
h2.backwardprint() # This should print: 40,30,95,20,10,80.
print()
h2.insert(75,6)
h2.forwardprint() # This should print: 85,10,20,95,30,40,75. 
h2.backwardprint() # This should print: 75,40,30,95,20,10,85.
print("///  Test 05  ///")
a3 = [10, 20, 30, 40, 50, 60, 70]
h3 = DoublyList(a3) # uses the constructor
h3.forwardprint() # This should print: 10,20,30,40,50,60,70.  

# removes at the given index. returns element of the removed node. Check validity of index. return None if index is invalid.
print("Removed element: "+ h3.remove(0)) # This should print: Removed element: 10
h3.forwardprint() # This should print: 20,30,40,50,60,70.  
h3.backwardprint() # This should print: 70,60,50,40,30,20.  
print("Removed element: "+ h3.remove(3)) # This should print: Removed element: 50
h3.forwardprint() # This should print: 20,30,40,60,70.  
h3.backwardprint() # This should print: 70,60,40,30,20.  
print("Removed element: "+ h3.remove(4)) # This should print: Removed element: 70
h3.forwardprint() # This should print: 20,30,40,60. 
h3.backwardprint() # This should print: 60,40,30,20.