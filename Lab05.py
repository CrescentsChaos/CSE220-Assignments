#STACK USING LINKED LIST

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class stackUsingLinkedList:
    cap = 999
    head = None
    rear = -1
#Push    
    def push(self, data):
        if self.rear < self.cap-1:
            self.rear += 1
            n = Node(data)
            if self.head == None:
                self.head = n
            else:
                n.next = self.head
                self.head = n
        else:
            print("stack overflow.")
#Top/Peek         
    def top(self):
        if self.rear == -1:
            return "stack underflow."
        if self.head == None:
            return None
        else:
            return self.head.data
#Pop            
    def pop(self):
        if self.rear == -1:
            return "stack underflow."       
        x = self.head
        next = self.head.next
        self.head = next
        self.rear -= 1
        return x.data
def ExpressionCheck(expression):
    element = stackUsingLinkedList()
    rearElement = stackUsingLinkedList()
    count = 1
    openingbracket = ["(", "[", "{"]
    closingbracket = [")", "]", "}"]
    for x in expression:
        if x in openingbracket:
            element.push(x)
            rearElement.push(count)
        elif x in closingbracket:
            if element.top() == "stack underflow.":
                return f"{expression} \nThis expression is NOT correct. \nError at character # {count}. '{x}'- not openingbracketed."
            if element.top()=="(" and x==")" or element.top()=="[" and x=="]" or element.top()=="{" and x=="}":
                element.pop()
                rearElement.pop()
            else:
                break    
        count += 1
    if element.top() == "stack underflow.":
        return f'{expression} \nThis expression is correct.'
    else:
        return f"{expression} \nThis expression is NOT correct. \nError at character # {rearElement.top()}. '{element.top()}'- not closingbracketd."
#DRIVER CODE        
expression= input()        
print(ExpressionCheck(expression))



#STACK USING ARRAY

class stackUsingArray:
  rear = -1
  def __init__(self):
      self.capacity = 999
      self.stack = [None]*self.capacity
#Push      
  def push(self, element):
      if self.rear < self.capacity-1:
          self.rear += 1
          self.stack[self.rear]= element
      else:
          print("stack overflow.")     
#Pop           
  def pop(self):
      if self.rear==-1:
          return "stack underflow."
      else:
          popped = self.stack[self.rear]
          self.stack[self.rear] = None
          self.rear -= 1
          return popped
#Top/Peek
  def top(self):
      if self.rear==-1:
          return "stack underflow."
      return self.stack[self.rear]
#Bracket Check      
def ExpressionCheck(expression):
    openingbracket = ["(", "[", "{"]
    closingbracket = [")", "]", "}"]
    element = stackUsingArray()
    rearElement = stackUsingArray()
    x = 1
    for i in expression:
        if element.top()=="stack underflow." and i in closingbracket:
            return f"{expression} \nThis expression is NOT correct. \nError at character # {x}. '{i}'- not openingbracketed."
        if element.top() == 'stack underflow.' and i in openingbracket:
            element.push(i)
            rearElement.push(x)
        elif element.top() in openingbracket and i in openingbracket:
            element.push(i)
            rearElement.push(x)       
        if element.top() =="(" and i == ")" or element.top() =="[" and i == "]" or element.top() =="{" and i == "}":
            element.pop()
            rearElement.pop()
        x+= 1
    if element.top() == "stack underflow.": 
        return f"{expression} \nThis expression is correct."
    else: 
        return f"{expression} \nThis expression is NOT correct. \nError at character # {rearElement.top()}. '{element.top()}'- not closingbracketd."
#DRIVER CODE        
expression= input()         
print(ExpressionCheck(expression))
