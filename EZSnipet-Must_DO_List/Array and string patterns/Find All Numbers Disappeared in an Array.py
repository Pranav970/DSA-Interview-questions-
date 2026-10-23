from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        i = 0
        n = len(nums)

        while i < n:
            correct_index = nums[i] - 1

            if nums[correct_index] != nums[i]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        result = []

        for i in range(n):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result
