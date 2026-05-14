class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr) - 1):
            arr[i] = self.findMax(arr, i)
        arr[-1] = -1
        return arr
    
    def findMax(self, arr: List[int], index: int) -> int:
        max = arr[index + 1]
        for i in range(index + 2, len(arr)):
            if max < arr[i]:
                max = arr[i]
        return max