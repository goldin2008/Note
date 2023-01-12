# 递归法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        elif p.val != q.val: return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
# 迭代法
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q: return True
        if not p or not q: return False
        que = collections.deque()
        que.append(p)
        que.append(q)
        while que:
            leftNode = que.popleft()
            rightNode = que.popleft()
            if not leftNode and not rightNode: continue 
            if not leftNode or not rightNode or leftNode.val != rightNode.val: return False 
            que.append(leftNode.left)
            que.append(rightNode.left)
            que.append(leftNode.right)
            que.append(rightNode.right)
        return True
