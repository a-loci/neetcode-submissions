class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        look_right: int = -1
        answer = [0] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            answer[i] = look_right
            look_right = max(arr[i],look_right)
        return answer

        
