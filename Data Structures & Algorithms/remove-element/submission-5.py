class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # k = Number of elements that do not equal val(user entered value that is desired to be removed
        # from the list of integers)
        k: int = 0
        for i in range(len(nums)):
            if(nums[i] != val):
                nums[k] = nums[i]
                k+=1
                
        return k

