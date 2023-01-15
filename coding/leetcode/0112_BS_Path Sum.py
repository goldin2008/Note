# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetsum: int) -> bool:
        def isornot(root, targetsum) -> bool:
            if (not root.left) and (not root.right) and targetsum == 0:
                return True  # 遇到叶子节点，并且计数为0
            if (not root.left) and (not root.right):
                return False  # 遇到叶子节点，计数不为0
            if root.left:
                # targetsum -= root.left.val  # 左节点
                # if isornot(root.left, targetsum): return True  # 递归，处理左节点
                # targetsum += root.left.val  # 回溯
                if isornot(root.left, targetsum-root.left.val): return True  # 递归，处理左节点
            if root.right:
                # targetsum -= root.right.val  # 右节点
                # if isornot(root.right, targetsum): return True  # 递归，处理右节点
                # targetsum += root.right.val  # 回溯
                if isornot(root.right, targetsum-root.right.val): return True  # 递归，处理右节点
            return False

        if root == None:
            return False  # 别忘记处理空treenode
        else:
            return isornot(root, targetsum - root.val)

# 迭代 - 层序遍历
class solution:
    def haspathsum(self, root: treenode, targetsum: int) -> bool:
        if not root: 
            return false

        stack = []  # [(当前节点，路径数值), ...]
        stack.append((root, root.val))

        while stack: 
            cur_node, path_sum = stack.pop()

            if not cur_node.left and not cur_node.right and path_sum == targetsum: 
                return true

            if cur_node.right: 
                stack.append((cur_node.right, path_sum + cur_node.right.val))    

            if cur_node.left: 
                stack.append((cur_node.left, path_sum + cur_node.left.val))

        return false
