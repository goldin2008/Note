# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        count = 0
        if not root:
            return count
        que = [root]
        while que:
            size = len(que)
            for _ in range(size):
                cur = que.pop(0)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            count +=1
        return count
