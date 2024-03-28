class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # Initialize a dictionary to store the frequency of elements
        freq = {}
        # Initialize two pointers: i and a variable to keep track of the maximum size
        i = maxSize = 0
        
        # Iterate through the array using pointer j
        for j in range(len(nums)):
            # Update the frequency of the current element
            freq[nums[j]] = freq.get(nums[j], 0) + 1
            
            # If the frequency of the current element exceeds k, adjust the window by moving pointer i
            while freq[nums[j]] > k:
                freq[nums[i]] -= 1
                i += 1
            
            # Update the maximum size of the good subarray
            maxSize = max(maxSize, j - i + 1)
        
        # Return the maximum size of the good subarray
        return maxSize
"""
Explanation:

1. We use a sliding window approach with two pointers, `i` and `j`, to iterate through the array.
2. The `freq` dictionary keeps track of the frequency of elements within the current window.
3. We update the frequency of the current element (`nums[j]`) and check if it exceeds `k`.
4. If the frequency exceeds `k`, we move the window by incrementing `i` and decrementing the frequency of the element at `nums[i]` until the frequency becomes less than or equal to `k`.
5. We update the maximum size of the good subarray (`maxSize`) by comparing it with the current window size (`j - i + 1`).
6. Finally, we return the maximum size of the good subarray.
"""
