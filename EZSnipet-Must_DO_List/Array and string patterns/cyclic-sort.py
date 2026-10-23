from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # Step 1: Cyclic sort
        # Place each number x in index x - 1 if possible
        i = 0
        while i < n:
            x = nums[i]

            # Only care about numbers in range [1, n]
            if 1 <= x <= n and nums[x - 1] != x:
                nums[i], nums[x - 1] = nums[x - 1], nums[i]
            else:
                i += 1

        # Step 2: Find first index where value != index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all positions are correct, answer is n + 1
        return n + 1
