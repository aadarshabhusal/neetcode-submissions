class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        arr = []
        for index in range(len(nums)):
            element = nums[index]
            if element == 1:
                count += 1
            if element == 0:
                arr.append(count)
                count = 0
        arr.append(count)
        return max(arr)