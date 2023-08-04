# link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# status: Accepted
# Runtime: 124ms Beats 91.50%of users with Python3
# Memory: 17.14mb Beats 94.20%of users with Python3
# Algorithm: Two Pointers

from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j=0,len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]==target:
                return [i+1,j+1]
            if numbers[i]+numbers[j]>target:
                j-=1
                continue
            i+=1