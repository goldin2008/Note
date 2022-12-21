"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# 递归法
class solution:
    def maxdepth(self, root: 'node') -> int:
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxdepth(root.children[i]))
        return depth + 1

# 迭代法
import collections
class solution:
    def maxdepth(self, root: 'node') -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        depth = 0 #记录深度
        while queue:
            size = len(queue)
            depth += 1
            for i in range(size):
                node = queue.popleft()
                for j in range(len(node.children)):
                    if node.children[j]:
                        queue.append(node.children[j])
        return depth

# 使用栈来模拟后序遍历依然可以
class solution:
    def maxdepth(self, root: 'node') -> int:
        st = []
        if root:
            st.append(root)
        depth = 0
        result = 0
        while st:
            node = st.pop()
            if node != none:
                st.append(node) #中
                st.append(none)
                depth += 1
                for i in range(len(node.children)): #处理孩子
                    if node.children[i]:
                        st.append(node.children[i])
                    
            else:
                node = st.pop()
                depth -= 1
            result = max(result, depth)
        return result
