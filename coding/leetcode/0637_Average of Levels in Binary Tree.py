# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return result
        from collections import deque
        que = deque([root])
        while que:
            res = []
            size = len(que)
            for _ in range(size):
                cur = que.popleft()
                res.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            result.append(sum(res)/size)
        return result

class Solution:
    """二叉树层平均值迭代解法"""

    def averageOfLevels(self, root: TreeNode) -> List[float]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            length = len(que)
            sum_ = 0
            for _ in range(length):
                cur = que.popleft()
                sum_ += cur.val
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(sum_ / length)

        return results
