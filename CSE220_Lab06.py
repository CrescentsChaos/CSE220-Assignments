print("=====Task 1=====")
#a
def factorial(n):
  if n==0:
    return 1
  else:
    return n*factorial(n-1)
#b
def fibonacci(n):
  if n <= 1:
    return n
  else:  
    return fibonacci(n-1)+fibonacci(n-2)
#c
def printarray(arr,idx):
  if idx>=len(arr):
    return
  else:
    print(arr[idx])
    printarray(arr,idx+1)
#d
def powerN(num,pw):
  if pw==0:
    return 1
  else:  
    return num*powerN(num,pw-1)

#drivercode 
print("1.a)")
print(factorial(6))
print("1.b)")
print(fibonacci(6))
print("1.c)")
printarray([1,2,3],0)
print("1.d)")
print(powerN(3,1))
print(powerN(3,2))     
print(powerN(3,3))

print("=====Task 2=====")

#a
def dec2bin(n):
  if n==0:
      return 0
  else:
    return (n % 2 + 10 * dec2bin(int(n // 2)))
#Driver Code    
print("2.a)")
print(dec2bin(200))

#b
class Node:
  def __init__(self, e, n):
    self.elem = e
    self.next = n
class LinkedList:
  def __init__(self, a):
    if type(a) == list:
      self.head = Node(a[0], None)
      tail = self.head
      for i in range(1, len(a)):
        new_node = Node(a[i], None)
        tail.next = new_node
        tail = new_node
    else:
      self.head = a
list1 = [10, 20, 30, 40]
L1 = LinkedList(list1)
x = L1.head
def sumOfLinkedList(head):
  if head!= None:
    return head.elem + sumOfLinkedList(head.next)
  else:
    return 0
print("2.b)")    
print("Sum Of LinkedList:")
print(sumOfLinkedList(L1.head))

#c
def printReverse(head):
  if head == None:
    return 0
  else:
    printReverse(head.next)
    print(head.elem)
print("2.c)")    
print("Reverse:")    
printReverse(x)
print("=====Task 3=====")
def hocBuilder(n):
  if n==0:
    return 0
  if n==1:
    return 8
  else:
    return hocBuilder(n-1) + 5
print("Number of cards needed:" )  
print(hocBuilder(5))

print("=====Task 4=====")

#a
print("4.a)")
def left_pattern(n):
  if n==1:
    print(1)
  else:
    left_pattern(n-1)
    for i in range(1,n+1):
      print(i,end=" ")
    print()    
n=5
left_pattern(n)

#b
print("4.b)")
def right_pattern(a,i=0):
  x=" "*i*2
  y=""
  for j in range(1,a+1):
    y+=str(j)+" "
  if a==1:
    print(x+y)
  else:
    right_pattern(a-1,i+1)
    print(x+y)
right_pattern(5)

print("=====Task 5=====")
class FinalQ:
  def print(self,array,idx):
    if(idx<len(array)):
      profit = self.calcProfit(array[idx])  
      print(profit)
      self.print(array,idx+1)
  def calcProfit(self,investment):
    if investment<=25000:
      p=0
    elif investment<100000:
      p=(investment-25000)/(100/4.5)
    elif investment==100000:
      p=75000/(100/4.5)
    elif investment>100000:
      sub=investment-100000
      p=(75000/(100/4.5))+(sub/(100/8))
    return p

#Tester
array=[25000,100000,250000,350000]
f = FinalQ()
f.print(array,0)
