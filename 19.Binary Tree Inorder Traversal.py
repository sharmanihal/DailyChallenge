# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.ans=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        #Easy Recusrive Solution
        if not root:
            return
        self.inorderTraversal(root.left)
        self.ans.append(root.val)
        self.inorderTraversal(root.right)
        return self.ans
    
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Check if the root is empty
        if not root:
            return 
        
        # Initialize a stack to keep track of nodes
        stack = []
        
        # Initialize a list to store the traversal result
        ans = []
        
        # Start from the root node
        curr = root
        
        # Loop until all nodes are traversed
        while True:
            # Traverse all the left nodes and push them onto the stack
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                # If the current node is None, we have reached the leftmost node
                # Pop the node from the stack, add its value to the result list,
                # and move to its right child
                if not stack:
                    break
                curr = stack.pop()
                ans.append(curr.val)
                curr = curr.right
        
        # Return the inorder traversal result
        return ans 
"""
Explanation:
- The algorithm uses an iterative approach to perform an inorder traversal of a binary tree.
- It starts from the root node and traverses down to the leftmost node, pushing each node onto a stack along the way.
- Once it reaches a leaf node (where the left child is None), it pops nodes from the stack, adds their values to the result list, and moves to the right child of the popped node.
- This process continues until all nodes are traversed, and the inorder traversal result is returned.
    
"""

"""
Best way to understand this solution:

1. Start from the root: Visualize yourself standing at the root of the binary tree.
2. Go left until you can't: Imagine walking down the left subtree of the root, pushing each node onto a stack as you go.
3. Pop and process: When you can't go left anymore (reached a leaf), backtrack by popping nodes from the stack one by one. As you pop each node, process its value and move to its right child.
4. Repeat until stack is empty: Keep popping nodes and processing their values until the stack is empty.

You can associate each step with a keyword or image to help you remember:

- Start: Think of a starting point, like a footstep at the root of the tree.
- Left: Picture yourself turning left and following a path down the left subtree.
- Pop: Visualize popping a node off the stack, like removing a block from a stack of blocks.
- Process: Imagine doing something with the value of the popped node, like writing it down on a piece of paper.
- Repeat: Think of a loop, like a circle indicating repetition."""

            
