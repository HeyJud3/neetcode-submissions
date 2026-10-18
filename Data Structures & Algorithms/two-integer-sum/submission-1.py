class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = {}

        for i, n in enumerate(nums):
            x[n] = i

        for i, n in enumerate(nums):
            difference = target - n
            if difference in x and x[difference] != i:
                return [i, x[difference]]

        return []