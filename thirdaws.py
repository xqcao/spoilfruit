

class Solution:
  def checkAround2(self,arr,m,n,it,obj):
    i,j,f =it[0],it[1],obj[it]
    print("i,j,f:",i,j,f)
    if i-1>=0 and arr[i-1][j]==2:
      if (i-1,j) in obj and obj[(i-1, j)] !=True:
        return True
      elif (i-1,j) not in obj:
        return True
    elif i+1<m and arr[i+1][j]==2:
      if (i+1, j) in obj and  obj[(i+1, j)]  !=True:
        return True
      elif (i+1, j) not in obj:
        return True
    elif j-1>=0 and arr[i][j-1]==2:
      if (i, j-1) in obj and obj[(i, j-1)] !=True:
        return True
      elif (i, j-1) not in obj:
        return True
    elif j+1<n and arr[i][j+1]==2:
      if (i, j+1) in obj and obj[(i, j+1)]  !=True:
        return True
      elif (i, j+1) not in obj:
        return True
    return False
  def countSpoil(self,arr):
    m = len(arr)
    n = len(arr[0])
    q_1 = {(i,j):False for i in range(m) for j in range(n) if arr[i][j]==1}
    # False = init
    # True = from 1 change to 2
    count =1
    d1=0
    while count<=m*n:
      print("len=>",len(q_1))
      d1=len(q_1)
      for x in [y for y in q_1 if q_1[y] ==False]:
        flag =self.checkAround2(arr,m,n,x,q_1)
        if flag:
          arr[x[0]][x[1]]=2
          q_1[x]=True
      print("q_1 before pop ",q_1)
      for aa in q_1.copy():
        if q_1[aa]==True:
          # remove new 2
          q_1.pop(aa)
      if len(q_1)==0:
        break
      if d1==len(q_1):
        count =-1
        break
      count+=1
      
      print("q_1",count,q_1)
      print("updated==>",arr)
    print("count",count)
    return count
    







input=[
  [2,1,1,0,0,2,1],
  [1,1,0,0,0,1,1],
  [0,0,2,0,0,1,0],
  [1,1,0,0,0,0,1],
  [1,0,0,0,0,2,1],
  [2,0,0,0,0,2,1],
]

# input=[
#   [1],
#   [1],
#   [1],
#   [1],
#   [2],
# ]
# input=[
#   [1],
#   [0],
#   [1],
#   [1],
#   [2],
# ]
input=[
  [1],
  [0],
  [1],
  [1],
  [2],
]
for x in input:
  print(x)
s = Solution().countSpoil(input)
print("result===>",input)
print("result",s)