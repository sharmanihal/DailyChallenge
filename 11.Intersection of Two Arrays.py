# Solution 1: Using set operations
class Solution1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert nums1 to a set for O(1) lookup
        hashset = set(nums1)
        # Initialize a set to store the intersection elements
        res = set()
        # Iterate through nums2
        for i in nums2:
            # If an element from nums2 exists in hashset (nums1), add it to the result set
            if i in hashset:
                res.add(i)
        # Return the result set
        return res

# Solution 2: Using two-pointer technique after sorting arrays
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort both arrays
        nums1.sort()
        nums2.sort()
        # Initialize an empty set to store intersection elements
        res = set()
        # Initialize pointers for nums1 and nums2
        i, j = 0, 0
        # Iterate through both arrays
        while i < len(nums1) and j < len(nums2):
            # If the elements at pointers match, add to result set and move both pointers
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            # If element in nums1 is greater, move pointer for nums2
            elif nums1[i] > nums2[j]:
                j += 1
            # If element in nums2 is greater, move pointer for nums1
            else:
                i += 1
        # Return the result set
        return res

# Solution 3: Using binary search after sorting one array
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Sort nums2
        nums2.sort()
        # Initialize an empty set for the result
        res = set()
        # Iterate through nums1
        for i in nums1:
            # If the element is not already in res and it's found in nums2 using binary search, add to res
            if i not in res and self.binarySearch(nums2, i):
                res.add(i)
        # Return the result set
        return res

    # Binary search function
    def binarySearch(self, nums, target):
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False
