# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 递归法
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)
        
    def compare(self, left, right):
        #首先排除空节点的情况
        if left == None and right != None: return False
        elif left != None and right == None: return False
        elif left == None and right == None: return True
        #排除了空节点，再排除数值不相同的情况
        elif left.val != right.val: return False
        
        #此时就是：左右节点都不为空，且数值相同的情况
        #此时才做递归，做下一层的判断
        outside = self.compare(left.left, right.right) #左子树：左、 右子树：右
        inside = self.compare(left.right, right.left) #左子树：右、 右子树：左
        isSame = outside and inside #左子树：中、 右子树：中 （逻辑处理）
        return isSame

# deque.popleft() is O(1) -- a constant time operation.
# While list.pop(0) is O(n) -- linear time operation: the larger the list the longer
# CPython list implementation is array-based.
# pop(0) removes the first item from the list and it requires to shift left len(lst) - 1 items to fill the gap.
# deque() implementation uses a doubly linked list.
# No matter how large the deque, deque.popleft() requires a constant (limited above) number of operations.

# 迭代法： 使用队列
# deque
import collections
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        queue = collections.deque()
        queue.append(root.left) #将左子树头结点加入队列
        queue.append(root.right) #将右子树头结点加入队列
        while queue: #接下来就要判断这这两个树是否相互翻转
            leftNode = queue.popleft()
            rightNode = queue.popleft()
            if not leftNode and not rightNode: #左节点为空、右节点为空，此时说明是对称的
                continue
            
            #左右一个节点不为空，或者都不为空但数值不相同，返回false
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            queue.append(leftNode.left) #加入左节点左孩子
            queue.append(rightNode.right) #加入右节点右孩子
            queue.append(leftNode.right) #加入左节点右孩子
            queue.append(rightNode.left) #加入右节点左孩子
        return True

# 迭代法：使用栈
# stack []
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        st = [] #这里改成了栈
        st.append(root.left)
        st.append(root.right)
        while st:
            rightNode = st.pop()
            leftNode = st.pop()
            if not leftNode and not rightNode:
                continue
            if not leftNode or not rightNode or leftNode.val != rightNode.val:
                return False
            st.append(leftNode.left)
            st.append(rightNode.right)
            st.append(leftNode.right)
            st.append(rightNode.left)
        return True

# 层次遍历
# I don't think this is a good way.
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        que = [root]
        while que:
            this_level_length = len(que)
            for i in range(this_level_length // 2):
                # 要么其中一个是None但另外一个不是
                if (not que[i] and que[this_level_length - 1 - i]) or (que[i] and not que[this_level_length - 1 - i]):
                    return False
                # 要么两个都不是None
                if que[i] and que[i].val != que[this_level_length - 1 - i].val:
                    return False
            for i in range(this_level_length):
                if not que[i]: continue
                que.append(que[i].left)
                que.append(que[i].right)
            que = que[this_level_length:]
        return True
