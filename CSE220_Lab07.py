#TASK 1
class  KeyIndex:
  def __init__(self,a):
    self.list_1  = a
    max = self.list_1[0]
    min = self.list_1[0]
    for i in self.list_1:
      if i > max:
        max = i
      else:
        pass
    for i in self.list_1:
      if i < min:
        min = i
      else:
        pass
    if min <0:
      min = min* (-1)    
    if max < 0:
      self.list_2 = [0] * min
    else:
      self.list_2 = [0] * (max+min+1)
    self.m = min    
    for i in self.list_1:
      self.list_2[i+min] += 1
      
  def search(self,num):
    exist = False
    for j in range(len(self.list_2)):
      if self.list_2[j]!=0:
        if (j-(self.m)) == num:
          exist = True
          break
    if exist == True:
      print(True)
    else:
      print(False)
      
  def sort(self):
    for i in range(len(self.list_2)):
      while self.list_2[i] > 0:
        print(i - (self.m) , end =" ")
        self.list_2[i] -= 1
        
#Driver code        
test = KeyIndex([-5,-4,-3,-2,-1,-3,-5,-6,0,2,5])
test.search(int(0))
test.sort()

#TASK 2
def hash(arr):
  vowel="AEIOU"
  list_1 = [0] * 9
  for i in arr:
    count= 0
    for j in i:      
      if j not in vowel:
        if ord(j) > ord("A") and ord(j) <= ord("Z"):
          count+= 24
        if ord(j) >= ord("0") and ord(j) <= ord("9"):
          count+= int(j)
    count= count% 9
    if list_1[count] == 0:
      list_1[count] = i
    else:
      for idx in range(count+1, count+len(list_1)):
        if list_1[idx % 9] == 0:
          list_1[idx % 9] = i
          break
  return list_1        
  
#Driver Code  
print(hash(["ST1E89B8A32","ST1E89B8A321","ST1E89B8A32","ST1E89B8A325"]))