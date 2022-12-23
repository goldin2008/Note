# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """递归法 更快"""
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        maxvalue = max(nums)
        index = nums.index(maxvalue)
        
        root = TreeNode(maxvalue)

        left = nums[:index]
        right = nums[index + 1:]

        root.left = self.constructMaximumBinaryTree(left)
        root.right = self.constructMaximumBinaryTree(right)
        return root
        
class Solution:
    """最大二叉树 递归法"""

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        return self.traversal(nums, 0, len(nums))
    
    def traversal(self, nums: List[int], begin: int, end: int) -> TreeNode:
        # 列表长度为0时返回空节点
        if begin == end:
            return None
        
        # 找到最大的值和其对应的下标
        max_index = begin
        for i in range(begin, end):
            if nums[i] > nums[max_index]:
                max_index = i
        
        # 构建当前节点
        root = TreeNode(nums[max_index])
        
        # 递归构建左右子树
        root.left = self.traversal(nums, begin, max_index)
        root.right = self.traversal(nums, max_index + 1, end)
        
        return root
