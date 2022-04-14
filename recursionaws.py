
import copy
from curses import reset_shell_mode

def splatsit(arr,ff0,res):
  old = copy.deepcopy(arr)
  
  for y in range(len(arr)):
    print(arr[y])
  print(f"-----------{res}--------------")
  ff = copy.deepcopy(ff0)
  m = len(arr)
  n = len(arr[0])
  flag_have_one  = False
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      if arr[i][j] ==2 and ff[i][j] != True:
        if i-1>=0:
            if arr[i-1][j] ==1:
              arr[i-1][j]=2
              ff[i-1][j] = True
        if i+1<m:
            if arr[i+1][j]==1:
              arr[i+1][j] =2
              ff[i+1][j] =True
        if j-1>=0:
            if arr[i][j-1]==1:
              arr[i][j-1]=2
              ff[i][j-1]=True
        if j+1<n:
            if arr[i][j+1]==1:
              arr[i][j+1]=2
              ff[i][j+1]=True
      # print(f"{i} {j}",arr[i][j])
      if arr[i][j] ==1:
        flag_have_one=True
  res+=1
  for x in range(len(arr)):
    print(arr[x])
    print(ff[x])
  if old == arr:
    if flag_have_one:
      return -1
    else:
      return res-1
  
  return splatsit(arr,ff0,res)


input=[
  [2,1,1,0,0,2,1],
  [1,1,0,0,0,1,1],
  [0,0,2,0,0,1,0],
  [0,0,0,0,0,0,1],
  [0,0,1,0,0,2,1],
]
flag = [[False for _ in range(len(input[0]))]]*len(input)
x = splatsit(input,flag,0)

print("x=",x)