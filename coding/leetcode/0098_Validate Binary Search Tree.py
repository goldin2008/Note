# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归 - 利用BST中序遍历特性,把树"压缩"成数组
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 思路: 利用BST中序遍历的特性.
        # 中序遍历输出的二叉搜索树节点的数值是有序序列
        candidate_list = []
        
        def __traverse(root: TreeNode) -> None: 
            nonlocal candidate_list
            if not root: 
                return 
            __traverse(root.left)
            candidate_list.append(root.val)
            __traverse(root.right)
            
        def __is_sorted(nums: list) -> bool: 
            for i in range(1, len(nums)): 
                if nums[i] <= nums[i - 1]: # ⚠️ 注意: Leetcode定义二叉搜索树中不能有重复元素
                    return False
            return True
        
        __traverse(root)
        res = __is_sorted(candidate_list)
        
        return res

# 递归 - 标准做法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # 规律: BST的中序遍历节点数值是从小到大. 
        cur_max = -float("INF")
        def __isValidBST(root: TreeNode) -> bool: 
            nonlocal cur_max
            
            if not root: 
                return True
            
            is_left_valid = __isValidBST(root.left)
            if cur_max < root.val: 
                cur_max = root.val
            else: 
                return False
            is_right_valid = __isValidBST(root.right)
            
            return is_left_valid and is_right_valid
        return __isValidBST(root)

# 迭代-中序遍历
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack = []
        cur = root
        pre = None
        while cur or stack:
            if cur: # 指针来访问节点，访问到最底层
                stack.append(cur)
                cur = cur.left
            else: # 逐一处理节点
                cur = stack.pop()
                if pre and cur.val <= pre.val: # 比较当前节点和前节点的值的大小
                    return False
                pre = cur 
                cur = cur.right
        return True

# 遵循Carl的写法，只添加了节点判断的部分
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # method 2
        que, pre = [], None
        while root or que:
            while root:
                que.append(root)
                root = root.left
            root = que.pop()
            # 对第一个节点只做记录，对后面的节点进行比较
            if pre is None:
                pre = root.val
            else:
                if pre >= root.val: return False
                pre = root.val
            root = root.right
        return True
