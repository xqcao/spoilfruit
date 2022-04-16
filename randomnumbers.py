import numpy as np

# from thirdaws import Solution 
from queaws import Solution
 
arr=np.random.randint(0, 3, size=(8, 20))
s = Solution().countSpoil(arr)

for x in arr:
  print(x)

print(s)
