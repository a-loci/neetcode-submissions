class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOne = 0
        maxBeforeZero= 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                countOne +=1
                if(countOne > maxBeforeZero):
                    maxBeforeZero = countOne
            else:
                countOne = 0
        return maxBeforeZero
            