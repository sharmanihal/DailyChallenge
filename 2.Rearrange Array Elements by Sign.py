class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        arr1=[]  # Initialize an empty list to store positive integers
        arr2=[]  # Initialize an empty list to store negative integers
        for i in nums:  # Iterate through each element in the input array
            if i>=0:  # If the element is non-negative
                arr1.append(i)  # Append it to the list of positive integers
            else:  # If the element is negative
                arr2.append(i)  # Append it to the list of negative integers
                
        x,y=0,0  # Initialize two pointers to keep track of the current index in arr1 and arr2
        for i in range(len(nums)):  # Iterate through each index in the original array
            if i%2==0:  # If the index is even
                nums[i]=arr1[x]  # Assign the current positive integer from arr1 to the current index in nums
                x+=1  # Move the pointer for positive integers to the next position
            else:  # If the index is odd
                nums[i]=arr2[y]  # Assign the current negative integer from arr2 to the current index in nums
                y+=1  # Move the pointer for negative integers to the next position
        return nums  # Return the modified array satisfying the conditions
"""
Explanation:
1. We start by separating the positive and negative integers into two separate arrays, arr1 and arr2.
2. We then iterate through the original array, nums, and fill it with alternating positive and negative integers.
3. We maintain two pointers, x and y, which keep track of the current position in arr1 and arr2, respectively.
4. We alternate between assigning elements from arr1 and arr2 to the positions in nums, ensuring that each consecutive pair of integers has opposite signs.
5. Finally, we return the modified array nums.
"""




class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # Initialize a result array with the same length as nums, filled with zeros
        res = [0] * len(nums)
        # Initialize an index variable to keep track of the current position in res
        index = 0
        # Initialize two pointers, i and j, to keep track of the current position in nums for positive and negative integers respectively
        i, j = 0, 0
        # Iterate until all positions in res are filled
        while index < len(res):
            # If the current index in res is even
            if index % 2 == 0:
                # Find the next positive integer in nums and assign it to the current position in res
                while i < len(nums) and nums[i] < 0:
                    i += 1
                res[index] = nums[i]
                i += 1  # Move the pointer for positive integers to the next position
            else:  # If the current index in res is odd
                # Find the next negative integer in nums and assign it to the current position in res
                while j < len(nums) and nums[j] >= 0:
                    j += 1
                res[index] = nums[j]
                j += 1  # Move the pointer for negative integers to the next position
            index += 1  # Move to the next position in res
        return res  # Return the modified array satisfying the conditions
"""
Explanation:
1. We initialize a result array `res` with the same length as the input array `nums`, filled with zeros.
2. We initialize an `index` variable to keep track of the current position in `res`.
3. We initialize two pointers, `i` and `j`, to keep track of the current position in `nums` for positive and negative integers respectively.
4. We iterate until all positions in `res` are filled.
5. If the current index in `res` is even, we find the next positive integer in `nums` and assign it to the current position in `res`.
6. If the current index in `res` is odd, we find the next negative integer in `nums` and assign it to the current position in `res`.
7. We move the respective pointers `i` or `j` to the next position as needed.
8. We increment the `index` to move to the next position in `res`.
9. Finally, we return the modified array `res` satisfying the conditions.
"""
