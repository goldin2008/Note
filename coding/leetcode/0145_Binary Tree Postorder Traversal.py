# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []

        def traversal(root: TreeNode):
            if root is None:
                return
            traversal(root.left)    # 左
            traversal(root.right)   # 右
            result.append(root.val) # 后序

        traversal(root)
        return result


# 后序遍历-迭代-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            # 中结点先处理
            result.append(node.val)
            # 左孩子先入栈
            if node.left:
                stack.append(node.left)
            # 右孩子后入栈
            if node.right:
                stack.append(node.right)
        # 将最终的数组翻转
        return result[::-1]

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:
            return []        
        result = []
        st = [root]
        while st:
            node = st.pop()
            if node is None: #只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop()
                result.append(node.val)
            else:
                st.append(node) #添加中节点
                st.append(None) #中节点访问过，但是还没有处理，加入空节点做为标记。

                if node.right: #添加右节点（空节点不入栈）
                    st.append(node.right)

                if node.left: #添加左节点（空节点不入栈）
                    st.append(node.left)
        return result
