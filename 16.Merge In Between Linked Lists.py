class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        gap = b - a
        current_node = list1
        prev_node = None
        
        # Traverse list1 to reach the ath node
        while a:
            prev_node = current_node
            current_node = current_node.next
            a -= 1
        
        # Reach the bth node
        merge_point = current_node
        
        # Traverse list1 to reach the bth node
        while gap:
            merge_point = merge_point.next
            gap -= 1
        
        # Connect list1 to list2
        prev_node.next = list2
        
        # Find the end of list2
        last_node = list1
        while last_node.next:
            last_node = last_node.next
        
        # Connect the end of list2 to the node after bth node
        last_node.next = merge_point.next
        
        return list1
