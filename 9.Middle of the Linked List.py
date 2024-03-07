"""
Explanation:
- Both solutions aim to find the middle node of a linked list.
- The first solution calculates the length of the linked list in the first pass, then iterates to the middle node in the second pass.
- The second solution uses the two-pointer technique, where one pointer (slow) moves one step at a time while the other pointer (fast) moves two steps at a time. When the fast pointer reaches the end of the list, the slow pointer will be at the middle of the list.
- The second solution is more efficient as it only requires one pass through the list.
"""
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This solution calculates the length of the linked list in the first pass,
        then iterates to the middle node in the second pass.
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        half = length // 2
        curr = head
        while half:
            curr = curr.next
            half -= 1
        return curr

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        This solution uses the two-pointer technique, where one pointer (slow)
        moves one step at a time while the other pointer (fast) moves two steps at a time.
        When the fast pointer reaches the end of the list, the slow pointer will be at
        the middle of the list.
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


