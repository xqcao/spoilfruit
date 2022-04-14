
class Solution:
  def checkAround2(self,arr,m,n,i,j,obj):
    if i-1>=0 and arr[i-1][j]==2 and obj[(i-1, j)]  ==False:
        return True
    elif i+1<m and arr[i+1][j]==2 and obj[(i+1, j)]  ==False:
        return True
    elif j-1>=0 and arr[i][j-1]==2 and obj[(i, j-1)] ==False:
        return True
    elif j+1<n and arr[i][j+1]==2 and obj[(i, j+1)]  ==False:
        return True
    return False
  def countSpoil(self,arr):
    res=0
    m = len(arr)
    n = len(arr[0])
    q_1=[[i,j] for i in range(m) for j in range(n) if arr[i][j]==1]
    obj_new_2 ={(i,j):False for i in range(m) for j in range(n)}
    q_2=[]
    count=0
    while len(q_1)>0 or len(q_2)>0:
      y = q_1.pop(0)
      print('y===>',y)
      changeOrNot=self.checkAround2(arr,m,n,y[0],y[1],obj_new_2)
      if changeOrNot != True:
        q_2.append(y)
      else:
        arr[y[0]][y[1]]=2
        obj_new_2[(y[0],y[1])]=True
      print("arr[i][j]",(y[0],y[1]),arr[y[0]][y[1]])
      if len(q_1)==0:
        res = res+1
        q_1 +=q_2
        q_2=[]
        obj_new_2 ={(i,j):False for i in range(m) for j in range(n)}
      if count>m*n:
        return -1
      print("count",count)
      count=count+1
      
    return res
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
# input=[
#   [0],
#   [1],
#   [1],
#   [1],
#   [2],
# ]
for x in input:
  print(x)
s = Solution().countSpoil(input)
print(input)
print("result",s)