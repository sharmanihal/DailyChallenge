class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1  # Base case: If n is 1, return 1 as it's the only element
        prefix_sums = []  # Store prefix sums
        current_sum = 1  # Initialize current_sum to 1
        # Calculate prefix sums for integers from 2 to n+1
        for i in range(2, n + 2):
            prefix_sums.append(current_sum)
            current_sum += i
        # Check for pivot integer
        for i in range(len(prefix_sums) - 1):
            if prefix_sums[i] == prefix_sums[-1] - prefix_sums[i + 1]:
                return i + 2  # Return pivot integer
        return -1  # Return -1 if no pivot integer found


class Solution:
    def pivotInteger(self, n: int) -> int:
        if n == 1:
            return 1  # Base case: If n is 1, return 1 as it's the only element
        total_sum = (n * (n + 1)) // 2  # Calculate total sum of integers from 1 to n
        # Check for pivot integer
        for i in range(1, n + 1):
            sum_till_i = (i * (i + 1)) // 2  # Calculate sum of integers from 1 to i
            next_sum = i + 1
            sum_till_i_next = (next_sum * (next_sum + 1)) // 2  # Calculate sum of integers from 1 to i+1
            if sum_till_i == total_sum - sum_till_i_next:
                return i + 1  # Return pivot integer
        return -1  # Return -1 if no pivot integer found
		
		
class Solution:
    def pivotInteger(self, n: int) -> int:
        # Base case: If n is 1, the only possible pivot integer is 1
        if n == 1:
            return 1
        
        # Initialize start and end pointers for binary search
        start = 1
        end = n
        
        # Calculate the total sum of elements from 1 to n using arithmetic series formula
        total_sum = (n * (n + 1)) // 2
        
        # Binary search to find the pivot integer
        while start < end:
            # Calculate the mid point
            mid = (start + end) // 2
            
            # Calculate the sum of elements from 1 to mid
            sum_till_mid = (mid * (mid + 1)) // 2
            
            # Calculate the sum of elements from mid+1 to n
            next_sum = mid + 1
            sum_till_mid_next = (next_sum * (next_sum + 1)) // 2
            
            # Check if the sum of elements from 1 to mid equals the sum of elements from mid+1 to n
            if sum_till_mid == total_sum - sum_till_mid_next:
                # If true, mid is the pivot integer, return mid + 1
                return mid + 1
            elif sum_till_mid > total_sum - sum_till_mid_next:
                # If the sum till mid is greater, search in the left half
                end = mid
            else:
                # If the sum till mid is smaller, search in the right half
                start = mid + 1
        
        # If no pivot integer is found, return -1
        return -1
