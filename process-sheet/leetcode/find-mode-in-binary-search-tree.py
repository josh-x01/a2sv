# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        freq = defaultdict(int)
        max_ = 0
        def traverse(node):
            if not node:
                return None
            traverse(node.left)
            freq[node.val] += 1
            nonlocal max_
            max_ = max(max_,freq[node.val])
            traverse(node.right)
        traverse(root)
        res = []
        for i in freq:
            if freq[i] == max_:
                res.append(i)
        return res
        