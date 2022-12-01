"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        from collections import deque
        que = deque([root])
        while que:
            size = len(que)
            for i in range(size):
                cur = que.popleft()
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
                # if cur.left and cur.right:
                #     cur.left.next = cur.right
                if i == size-1:
                    break
                cur.next = que[0]
        return root                    
        
# 层序遍历解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = [root]
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == n - 1:
                    break
                node.next = queue[0]
        return root

# 链表解法
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        first = root
        while first:
            cur = first
            while cur:  # 遍历每一层的节点
                if cur.left: cur.left.next = cur.right  # 找左节点的next
                if cur.right and cur.next: cur.right.next = cur.next.left  # 找右节点的next
                cur = cur.next # cur同层移动到下一节点
            first = first.left  # 从本层扩展到下一层
        return root
