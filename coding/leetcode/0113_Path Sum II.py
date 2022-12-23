# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetsum: int) -> List[List[int]]:
        def traversal(cur_node, remain): 
            if not cur_node.left and not cur_node.right:
                if remain == 0: 
                    result.append(path[:])
                return

            if cur_node.left: 
                path.append(cur_node.left.val)
                traversal(cur_node.left, remain-cur_node.left.val)
                path.pop()

            if cur_node.right: 
                path.append(cur_node.right.val)
                traversal(cur_node.right, remain-cur_node.right.val)
                path.pop()

        result, path = [], []
        if not root: 
            return []
        path.append(root.val)
        traversal(root, targetsum - root.val)
        return result

# 迭代法，用第二个队列保存目前的总和与路径
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        que, temp = deque([root]), deque([(root.val, [root.val])])
        result = []
        while que:
            for _ in range(len(que)):
                node = que.popleft()
                value, path = temp.popleft()
                if (not node.left) and (not node.right):
                    if value == targetSum:
                        result.append(path)
                if node.left:
                    que.append(node.left)
                    temp.append((node.left.val+value, path+[node.left.val]))
                if node.right:
                    que.append(node.right)
                    temp.append((node.right.val+value, path+[node.right.val]))
        return result
