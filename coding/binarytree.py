class Solution:
    """二叉树层序遍历迭代解法"""

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results
        
        from collections import deque
        que = deque([root])
        
        while que:
            size = len(que)
            result = []
            for _ in range(size):
                cur = que.popleft()
                result.append(cur.val)
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results

# 递归法
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root: return []
            if len(res) == depth: res.append([]) # start the current depth
            res[depth].append(root.val) # fulfil the current depth
            if  root.left: helper(root.left, depth + 1) # process child nodes for the next depth
            if  root.right: helper(root.right, depth + 1)
        helper(root, 0)
        return res


# 226.翻转二叉树
## 递归法：前序遍历：
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left #中
        self.invertTree(root.left) #左
        self.invertTree(root.right) #右
        return root


# 迭代法：深度优先遍历（前序遍历）：
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        st = []
        st.append(root)
        while st:
            node = st.pop()
            node.left, node.right = node.right, node.left #中
            if node.right:
                st.append(node.right) #右
            if node.left:
                st.append(node.left) #左
        return root


# 迭代法：广度优先遍历（层序遍历）：
import collections
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        queue = collections.deque() #使用deque()
        if root:
            queue.append(root)
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                node.left, node.right = node.right, node.left #节点处理
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return root


# 222.完全二叉树的节点个数
# 递归法
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.getNodesNum(root)
        
    def getNodesNum(self, cur):
        if not cur:
            return 0
        leftNum = self.getNodesNum(cur.left) #左
        rightNum = self.getNodesNum(cur.right) #右
        treeNum = leftNum + rightNum + 1 #中
        return treeNum

# 递归法：精简版
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

# 迭代法
import collections
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        queue = collections.deque()
        if root:
            queue.append(root)
        result = 0
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                result += 1 #记录节点数量
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
