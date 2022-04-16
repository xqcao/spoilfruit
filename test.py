import random

m,n = 5,10
fruit =[2,0,0,0,0,0,1,1,1,2]*5*10
arr=[[0]*m]*n
print(arr)
random.shuffle(fruit)

random.shuffle(fruit)
print(fruit)
count=0
for i in range(m):
  for j in range(n):
    arr[j][i] =fruit[count]
    
    count+=1
for x in arr: 
  print(x)
                