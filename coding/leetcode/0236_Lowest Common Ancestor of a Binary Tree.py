# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""二叉树的最近公共祖先 递归法

在递归函数有返回值的情况下: 
如果要搜索一条边，递归函数返回值不为空的时候，立刻返回，
如果搜索整个树，直接用一个变量left、right接住返回值，这个left、right后序还有逻辑处理的需要，
也就是后序遍历中处理中间节点的逻辑（也是回溯）

求最小公共祖先，需要从底向上遍历，那么二叉树，只能通过后序遍历（即:回溯）实现从底向上的遍历方式。
"""
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        return right
