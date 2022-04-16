class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_copy=copy.deepcopy(nums)
        arr=sorted(nums)

        i,j =0,len(nums)-1
        while arr[i]+arr[j]!=target:
          if arr[i]+arr[j]>target:
            j-=1
          else:
            i+=1
        res=[]

        for idx,x in enumerate(nums_copy):
          if x==arr[i] or x == arr[j]:
            res.append(idx)
        return res
        