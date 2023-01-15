"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """二叉树层序遍历迭代解法"""

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            length = len(que)
            result = []
            for _ in range(length):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results


# 递归法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(cur, depth):
            if not cur: return []
            if len(res) == depth: res.append([]) # start the current depth
            res[depth].append(cur.val) # fulfil the current depth
            if  cur.left: helper(cur.left, depth + 1) # process child nodes for the next depth
            if  cur.right: helper(cur.right, depth + 1)
        helper(root, 0)
        return res
