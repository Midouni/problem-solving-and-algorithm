# link: https://leetcode.com/problems/3sum/
# status: Accepted
# Algorithm: Two Pointers

from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for ele in range(len(nums)-2):
            i,j=ele+1,len(nums)-1
            while i < j:
                if nums[i]+nums[j]+nums[ele]==0:
                    if sorted([nums[i],nums[j],nums[ele]]) not in res:
                        res.append(sorted([nums[i],nums[j],nums[ele]]))
                    i+=1
                    j-=1
                    continue
                if nums[i]+nums[j]+nums[ele]>0:
                    j-=1
                    continue
                i+=1
                continue
        return res
                


l=Solution()
print(l.threeSum([-1,0,1,2,-1,-4]))