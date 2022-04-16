import random

m,n =5,10
arr = [[random.randint(0,2) for _ in range(n)] for _ in range(m)]
for x in arr:
  print(x)