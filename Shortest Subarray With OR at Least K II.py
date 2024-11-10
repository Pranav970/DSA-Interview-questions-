class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        # If k is 0, any single element works
        if k == 0:
            return 1
            
        n = len(nums)
        min_len = float('inf')
        
        # Try each possible starting position
        for start in range(n):
            or_value = 0
            # Calculate OR value for each ending position
            for end in range(start, n):
                or_value |= nums[end]
                # If we found a valid subarray
                if or_value >= k:
                    min_len = min(min_len, end - start + 1)
                    break  # No need to check longer subarrays from this start
        
        return -1 if min_len == float('inf') else min_len
