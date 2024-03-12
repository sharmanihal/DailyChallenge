Explanation:

Let's consider an example: [3, 4, 2, -6, 1, 1, 5, -6].

The sequence [4, 2, -6] results in a net sum of 0 (meaning these nodes must be removed from the final list). Similarly, the sequence [1, 5, -6] also results in a net sum of 0 (indicating these nodes must be removed from the final list). After removing these nodes, we are left with [3, 1], which is our final result.

To solve this problem, we use a hashtable and the concept of prefix sum.

The hashtable will keep track of the following items:

The key of the hashtable will be the cumulative sum.
The value of the hashtable will be the node up to which the sum has been accumulated.
Now, let's see what the hashtable stores for us:

List: [3, 4, 2, -6, 1, 1, 5, -6]

The hashtable entries are as follows:

image

The hashtable maintains the cumulative sum and the node up to which the sum has been accumulated.

The basic idea of the solution is:

If, while adding the cumulative sum to the hashtable, we encounter a duplicate of the sum, it means that previously we had a cumulative sum of, let's say, x. Then, the sum went up and down, and eventually reached x again, indicating that the net result of those up and down movements was 0. Therefore, the nodes whose net up and down to x was 0 need to be removed.

image

In the above example, we notice that we encounter 3 two times. The second time we encounter 3, we understand that we previously had a cumulative sum of 3, and whatever was added or subtracted from that 3 resulted in 0, as we again reach 3.

We need to remove the hashtable values that are between the first encounter of 3 and the second encounter of 3. Additionally, we need to create a link from the first encounter of 3 (i.e., the value of hashtable[3], which gives us the link of the node until where the cumulative sum was 3) to the current node's next element, as the current node also needs to be removed.
image
We repeat the above steps until we have traversed the entire list.

Code:

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases where the entire list is removed
        dummy_head = ListNode(0, head)
        # Hashtable to store prefix sums and their corresponding nodes
        prefix_sum_map = {0: dummy_head}
        # Variable to track prefix sum
        current_sum = 0
        
        # Traverse the linked list
        while head:
            # Update prefix sum
            current_sum += head.val
            
            # If prefix sum is found in hashtable, it means there is a subsequence with sum = 0
            if current_sum in prefix_sum_map:
                # Get the node before the subsequence
                node_before_zero_sum = prefix_sum_map[current_sum].next
                
                # Variable to accumulate the prefix sums of nodes to be removed
                sum_to_remove = current_sum
                
                # Traverse the nodes between the prefix_sum_map[current_sum] and head
                while node_before_zero_sum != head:
                    # Update sum_to_remove by adding the value of current node
                    sum_to_remove += node_before_zero_sum.val
                    # Remove accumulated prefix sums from hashtable
                    del prefix_sum_map[sum_to_remove]
                    # Move to the next node to be removed
                    node_before_zero_sum = node_before_zero_sum.next
                
                # Update the next pointer of the node before the subsequence to skip the removed nodes
                previous_node = prefix_sum_map[current_sum]
                previous_node.next = head.next
            else:
                # If prefix sum is not in hashtable, add it along with the current node
                prefix_sum_map[current_sum] = head
            
            # Move to the next node
            head = head.next
        
        # Return the next node after the dummy node which contains the final linked list
        return dummy_head.next
python
python3
inplace swap
