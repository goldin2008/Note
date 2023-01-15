# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root : return  None # 节点为空，返回
        if root.val < key :
            root.right = self.deleteNode(root.right, key)
        elif root.val > key :
            root.left = self.deleteNode(root.left, key)
        else:
            # 当前节点的左子树为空，返回当前的右子树
            if not root.left : return root.right
            # 当前节点的右子树为空，返回当前的左子树
            if not root.right: return root.left
            # 左右子树都不为空，找到右孩子的最左节点 记为p
            node = root.right
            while node.left :
                node = node.left
            # 将当前节点的左子树挂在p的左孩子上
            node.left = root.left
            # 当前节点的右子树替换掉当前节点，完成当前节点的删除
            root = root.right
        return root

# 迭代法
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # 找到节点后分两步，1. 把节点的左子树和右子树连起来，2. 把右子树跟父节点连起来
        # root is None
        if not root: return root
        p = root
        last = None
        while p:
            if p.val==key:
                # 1. connect left to right
                # right is not None -> left is None | left is not None
                if p.right:
                    if p.left:
                        node = p.right
                        while node.left:
                            node = node.left
                        node.left = p.left
                    right = p.right
                else:
                # right is None -> right=left
                    right = p.left
                # 2. connect right to last
                if last==None:
                    root = right
                elif last.val>key:
                    last.left = right
                else:
                    last.right = right
                # 3. return
                break
            else:
                # Update last and continue
                last = p
                if p.val>key:
                    p = p.left
                else:
                    p = p.right
        return root
