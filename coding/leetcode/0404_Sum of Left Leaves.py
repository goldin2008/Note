# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归后序遍历
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        
        left_left_leaves_sum = self.sumOfLeftLeaves(root.left)  # 左
        right_left_leaves_sum = self.sumOfLeftLeaves(root.right) # 右
        
        cur_left_leaf_val = 0
        if root.left and not root.left.left and not root.left.right: 
            cur_left_leaf_val = root.left.val 
            
        return cur_left_leaf_val + left_left_leaves_sum + right_left_leaves_sum # 中

# 迭代
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        """
        Idea: Each time check current node's left node. 
              If current node don't have one, skip it. 
        """
        stack = []
        if root: 
            stack.append(root)
        res = 0
        
        while stack: 
            # 每次都把当前节点的左节点加进去. 
            cur_node = stack.pop()
            if cur_node.left and not cur_node.left.left and not cur_node.left.right: 
                res += cur_node.left.val
                
            if cur_node.left: 
                stack.append(cur_node.left)
            if cur_node.right: 
                stack.append(cur_node.right)
                
        return res
