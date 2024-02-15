class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()  # Sort the input array nums in non-decreasing order
        prefix = [nums[0]]  # Initialize a prefix array with the first element of nums
        # Calculate the prefix sum of the sorted nums array
        for i in range(1, len(nums)):
            prefix.append(nums[i] + prefix[i-1])
        ans = -1  # Initialize the answer variable with -1
        # Iterate through the sorted nums array starting from index 2
        for i in range(2, len(nums)):
            # If the current element is less than the sum of the previous elements (excluding itself)
            if nums[i] < prefix[i-1]:
                ans = prefix[i]  # Update the answer with the sum of the current prefix
        return ans  # Return the largest possible perimeter of a polygon or -1 if not possible
"""
Explanation:
1. We start by sorting the input array `nums` in non-decreasing order.
2. We initialize a prefix array `prefix` with the first element of `nums`.
3. We then calculate the prefix sum of the sorted `nums` array and store it in `prefix`.
4. Next, we initialize the answer variable `ans` with -1.
5. We iterate through the sorted `nums` array starting from index 2, as the polygon must have at least three sides.
6. For each element at index `i`, we check if it satisfies the condition for forming a polygon, i.e., if it is less than the sum of the previous elements (excluding itself).
7. If the condition is met, we update the answer `ans` with the sum of the current prefix, which represents the largest possible perimeter.
8. Finally, we return the `ans`, which represents the largest possible perimeter of a polygon that can be formed from `nums`, or -1 if it is not possible to create a polygon.
"""

