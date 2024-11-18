class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0] * n
        
        # If k is 0, return array of zeros
        if k == 0:
            return result
            
        # Create an extended array to handle circular nature
        # Double the array to make circular access easier
        extended_code = code + code
        
        for i in range(n):
            # If k is positive, sum next k elements
            if k > 0:
                start = i + 1  # Start from next element
                end = i + k + 1  # Include k elements
            # If k is negative, sum previous k elements
            else:
                start = i + n + k  # Start from k elements before (in extended array)
                end = i + n  # Up to current element
            
            # Calculate sum of the required range
            result[i] = sum(extended_code[start:end])
            
        return result

# Test cases
def test_solution():
    sol = Solution()
    
    # Test case 1
    assert sol.decrypt([5,7,1,4], 3) == [12,10,16,13], "Test case 1 failed"
    
    # Test case 2
    assert sol.decrypt([1,2,3,4], 0) == [0,0,0,0], "Test case 2 failed"
    
    # Test case 3
    assert sol.decrypt([2,4,9,3], -2) == [12,5,6,13], "Test case 3 failed"
    
    print("All test cases passed!")

# Run the tests
if __name__ == "__main__":
    test_solution()
