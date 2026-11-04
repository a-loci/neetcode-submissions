class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Bulit-in Solution that creates a new list. Now we solve without creating a new list.
        # return nums + nums
        n: int = len(nums)
        ans = [0] * (2 *n)
        for i in range(n):
            ans[i] = nums[i]
            ans[i + n] = nums[i]
        return ans
        