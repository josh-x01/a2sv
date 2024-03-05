# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        _sum = 0
        def tree(root):
            nonlocal _sum
            if not root:
                return
            if low <= root.val <= high:
                _sum += root.val
            tree(root.left)
            tree(root.right)
        tree(root)
        return _sum