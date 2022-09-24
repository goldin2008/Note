"""
===================================================================================================
NOTE:
递归（深度和广度）只需要function call function，用一个result储存结果；

深度（迭代）需要额外用stack来存遍历的node，用while循环来遍历stack里面的所有node。数据结构栈stack用list []
深度遍历先遍历子node，然后再处理node，所以是preorder的话，先处理node再添加子node，如果不是preorder，需要用None标记待处理node

广度（迭代）需要额外用queue来存遍历的node，用while循环来遍历queue里面的所有node。队列queue用deque([])
广度遍历level order先处理node，然后再遍历添加子node
广度（递归和迭代）都是先处理node，再遍历添加子node
===================================================================================================

满二叉树: 如果一棵二叉树只有度为0的结点和度为2的结点，并且度为0的结点在同一层上，则这棵二叉树为满二叉树。
这棵二叉树为满二叉树，也可以说深度为k，有2^k-1个节点的二叉树。

完全二叉树的定义如下: 在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，
并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2^(h-1)  个节点。
优先级队列其实是一个堆，堆就是一棵完全二叉树，同时保证父子节点的顺序关系。

二叉搜索树是有数值的了，二叉搜索树是一个有序树。
1. 若它的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
2. 若它的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
3. 它的左、右子树也分别为二叉排序树

平衡二叉搜索树: 又被称为AVL（Adelson-Velsky and Landis）树，
且具有以下性质: 它是一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树。

链式存储方式就用指针， 顺序存储的方式就是用数组

二叉树主要有两种遍历方式:
1. 深度优先遍历: 先往深走，遇到叶子节点再往回走。
2. 广度优先遍历: 一层一层的去遍历。
深度优先遍历
1. 前序遍历（递归法，迭代法）
2. 中序遍历（递归法，迭代法）
3. 后序遍历（递归法，迭代法）
广度优先遍历
1. 层次遍历（迭代法）
二叉树中深度优先和广度优先遍历实现方式，我们做二叉树相关题目，经常会使用递归的方式来实现深度优先遍历，也就是实现前中后序遍历，使用递归是比较方便的。
栈其实就是递归的一种是实现结构，也就说前中后序遍历的逻辑其实都是可以借助栈使用递归的方式来实现的。
广度优先遍历的实现一般使用队列来实现，这也是队列先进先出的特点所决定的，因为需要先进先出的结构，才能一层一层的来遍历二叉树。

有同学会把红黑树和二叉平衡搜索树弄分开了，其实红黑树就是一种二叉平衡搜索树，这两个树不是独立的，所以C++中map、multimap、set、multiset的底层实现机制是二叉平衡搜索树，再具体一点是红黑树。

morris遍历是二叉树遍历算法的超强进阶算法，morris遍历可以将非递归遍历中的空间复杂度降为O(1)，感兴趣大家就去查一查学习学习，比较小众，面试几乎不会考。我其实也没有研究过，就不做过多介绍了。
"""

# 二叉树节点定义
class TreeNode: 
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None

"""
深度优先 递归
"""
# 前序遍历-递归-LC144_二叉树的前序遍历
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        # 保存结果
        result = []
        def traversal(root: TreeNode):
            if root == None:
                return
            result.append(root.val) # 前序
            traversal(root.left)    # 左
            traversal(root.right)   # 右
        traversal(root)
        return result
# 中序遍历-递归-LC94_二叉树的中序遍历
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)    # 左
            result.append(root.val) # 中序
            traversal(root.right)   # 右
        traversal(root)
        return result
# 后序遍历-递归-LC145_二叉树的后序遍历
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        def traversal(root: TreeNode):
            if root == None:
                return
            traversal(root.left)    # 左
            traversal(root.right)   # 右
            result.append(root.val) # 后序
        traversal(root)
        return result

"""
深度优先 迭代
数据结构: 栈 stack, [] in python
"""
# 迭代统一写法
# 迭代法前序遍历：
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st= []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
                st.append(node) #中
                st.append(None)
            else:
                node = st.pop()
                result.append(node.val)
        return result
# 迭代法中序遍历：
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                if node.right: #添加右节点（空节点不入栈）
                    st.append(node.right)
                
                st.append(node) #添加中节点
                st.append(None) #中节点访问过，但是还没有处理，加入空节点做为标记。
                
                if node.left: #添加左节点（空节点不入栈）
                    st.append(node.left)
            else: #只有遇到空节点的时候，才将下一个节点放进结果集
                node = st.pop() #重新取出栈中元素
                result.append(node.val) #加入到结果集
        return result
# 迭代法后序遍历：
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        st = []
        if root:
            st.append(root)
        while st:
            node = st.pop()
            if node != None:
                st.append(node) #中
                st.append(None)
                
                if node.right: #右
                    st.append(node.right)
                if node.left: #左
                    st.append(node.left)
            else:
                node = st.pop()
                result.append(node.val)
        return result

"""
广度优先(层序遍历) 递归
"""
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

"""
广度优先(层序遍历) 迭代
数据结构: 队列 queue, deque() in python
"""
class Solution:
    """二叉树层序遍历迭代解法"""
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        results = []
        if not root:
            return results

        from collections import deque
        que = deque([root])

        while que:
            # que里面现有的所有node都是一层要遍历的node
            size = len(que)
            result = []
            # 遍历一层的所有node
            for _ in range(size):
                # 处理node
                cur = que.popleft()
                result.append(cur.val)
                # 添加左右子node
                if cur.left:
                    que.append(cur.left)
                if cur.right:
                    que.append(cur.right)
            results.append(result)

        return results


#1 226.翻转二叉树
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


#2 101. 对称二叉树
# 给定一个二叉树，检查它是否是镜像对称的。
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
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


#3 104.二叉树的最大深度
# 给定一个二叉树，找出其最大深度。
# 二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#4 559.n叉树的最大深度
class solution:
    def maxdepth(self, root: treenode) -> int:
        return self.getdepth(root)
        
    def getdepth(self, node):
        if not node:
            return 0
        leftdepth = self.getdepth(node.left) #左
        rightdepth = self.getdepth(node.right) #右
        depth = 1 + max(leftdepth, rightdepth) #中
        return depth

class solution:
    def maxdepth(self, root: 'node') -> int:
        if not root:
            return 0
        depth = 0
        for i in range(len(root.children)):
            depth = max(depth, self.maxdepth(root.children[i]))
        return depth + 1


#5 111.二叉树的最小深度
# 给定一个二叉树，找出其最小深度。
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        min_depth = 10**9
        if root.left:
            min_depth = min(self.minDepth(root.left), min_depth) # 获得左子树的最小高度
        if root.right:
            min_depth = min(self.minDepth(root.right), min_depth) # 获得右子树的最小高度
        return min_depth + 1


#6 ??? 222.完全二叉树的节点个数
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


# 110.平衡二叉树
# 给定一个二叉树，判断它是否是高度平衡的二叉树。


# 257. 二叉树的所有路径
# 给定一个二叉树，返回所有从根节点到叶子节点的路径。


# 404.左叶子之和
# 计算给定二叉树的所有左叶子之和。


# 513.找树左下角的值
# 给定一个二叉树，在树的最后一行找到最左边的值。


# 112. 路径总和
# 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。


# 106.从中序与后序遍历序列构造二叉树
# 根据一棵树的中序遍历与后序遍历构造二叉树。


# 654.最大二叉树
# 给定一个不含重复元素的整数数组。一个以此数组构建的最大二叉树定义如下：
# 二叉树的根是数组中的最大元素。
# 左子树是通过数组中最大值左边部分构造出的最大二叉树。
# 右子树是通过数组中最大值右边部分构造出的最大二叉树。
# 通过给定的数组构建最大二叉树，并且输出这个树的根节点。


# 617.合并二叉树
# 给定两个二叉树，想象当你将它们中的一个覆盖到另一个上时，两个二叉树的一些节点便会重叠。


# 700.二叉搜索树中的搜索
# 给定二叉搜索树（BST）的根节点和一个值。 你需要在BST中找到节点值等于给定值的节点。 返回以该节点为根的子树。 如果节点不存在，则返回 NULL。





# 98.验证二叉搜索树
# 给定一个二叉树，判断其是否是一个有效的二叉搜索树。
# 假设一个二叉搜索树具有如下特征：
# 节点的左子树只包含小于当前节点的数。
# 节点的右子树只包含大于当前节点的数。
# 所有左子树和右子树自身必须也是二叉搜索树。
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


# 530.二叉搜索树的最小绝对差
# 给你一棵所有节点为非负值的二叉搜索树，请你计算树中任意两节点的差的绝对值的最小值。


# 501.二叉搜索树中的众数
# 给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。
# 假定 BST 有如下定义：
# 结点左子树中所含结点的值小于等于当前结点的值
# 结点右子树中所含结点的值大于等于当前结点的值
# 左子树和右子树都是二叉搜索树


# 236. 二叉树的最近公共祖先
# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
class Solution:
    """二叉树的最近公共祖先 递归法"""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root
        if left:
            return left
        return right


# 235. 二叉搜索树的最近公共祖先
# 给定一个二叉搜索树, 找到该树中两个指定节点的最近公共祖先。
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”


# 701.二叉搜索树中的插入操作
# 给定二叉搜索树（BST）的根节点和要插入树中的值，将值插入二叉搜索树。 返回插入后二叉搜索树的根节点。 输入数据保证，新值和原始二叉搜索树中的任意节点值都不同。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        # 返回更新后的以当前root为根节点的新树，方便用于更新上一层的父子节点关系链

        # Base Case
        if not root: return TreeNode(val)

        # 单层递归逻辑:
        if val < root.val: 
            # 将val插入至当前root的左子树中合适的位置
            # 并更新当前root的左子树为包含目标val的新左子树
            root.left = self.insertIntoBST(root.left, val)

        if root.val < val:
            # 将val插入至当前root的右子树中合适的位置
            # 并更新当前root的右子树为包含目标val的新右子树
            root.right = self.insertIntoBST(root.right, val)

        # 返回更新后的以当前root为根节点的新树
        return root


# 450.删除二叉搜索树中的节点
# 给定一个二叉搜索树的根节点 root 和一个值 key，删除二叉搜索树中的 key 对应的节点，并保证二叉搜索树的性质不变。返回二叉搜索树（有可能被更新）的根节点的引用。
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if not root: return root  #第一种情况：没找到删除的节点，遍历到空节点直接返回了
        if root.val == key:  
            if not root.left and not root.right:  #第二种情况：左右孩子都为空（叶子节点），直接删除节点， 返回NULL为根节点
                del root
                return None
            if not root.left and root.right:  #第三种情况：其左孩子为空，右孩子不为空，删除节点，右孩子补位 ，返回右孩子为根节点
                tmp = root
                root = root.right
                del tmp
                return root
            if root.left and not root.right:  #第四种情况：其右孩子为空，左孩子不为空，删除节点，左孩子补位，返回左孩子为根节点
                tmp = root
                root = root.left
                del tmp
                return root
            else:  #第五种情况：左右孩子节点都不为空，则将删除节点的左子树放到删除节点的右子树的最左面节点的左孩子的位置
                v = root.right
                while v.left:
                    v = v.left
                v.left = root.left
                tmp = root
                root = root.right
                del tmp
                return root
        if root.val > key: root.left = self.deleteNode(root.left,key)  #左递归
        if root.val < key: root.right = self.deleteNode(root.right,key)  #右递归
        return root


# 669. 修剪二叉搜索树
# 给定一个二叉搜索树，同时给定最小边界L 和最大边界 R。通过修剪二叉搜索树，使得所有节点的值在[L, R]中 (R>=L) 。你可能需要改变树的根节点，所以结果应当返回修剪好的二叉搜索树的新的根节点。


# 108.将有序数组转换为二叉搜索树
# 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        '''
        构造二叉树：重点是选取数组最中间元素为分割点，左侧是递归左区间；右侧是递归右区间
        必然是平衡树
        左闭右闭区间
        '''
        # 返回根节点
        root = self.traversal(nums, 0, len(nums)-1)
        return root

    def traversal(self, nums: List[int], left: int, right: int) -> TreeNode:
        # Base Case
        if left > right:
            return None
        
        # 确定左右界的中心，防越界
        mid = left + (right - left) // 2
        # 构建根节点
        mid_root = TreeNode(nums[mid])
        # 构建以左右界的中心为分割点的左右子树
        mid_root.left = self.traversal(nums, left, mid-1)
        mid_root.right = self.traversal(nums, mid+1, right)

        # 返回由被传入的左右界定义的某子树的根节点
        return mid_root


# 538.把二叉搜索树转换为累加树
# 给出二叉 搜索 树的根节点，该树的节点值各不相同，请你将其转换为累加树（Greater Sum Tree），使每个节点 node 的新值等于原树中大于或等于 node.val 的值之和。
# 提醒一下，二叉搜索树满足下列约束条件：
# 节点的左子树仅包含键 小于 节点键的节点。 节点的右子树仅包含键 大于 节点键的节点。 左右子树也必须是二叉搜索树。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = TreeNode()

    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        倒序累加替换：  
        [2, 5, 13] -> [[2]+[1]+[0], [2]+[1], [2]] -> [20, 18, 13]
        '''
        self.traversal(root)
        return root

    def traversal(self, root: TreeNode) -> None:
        # 因为要遍历整棵树，所以递归函数不需要返回值
        # Base Case
        if not root: 
            return None
        # 单层递归逻辑：中序遍历的反译 - 右中左
        self.traversal(root.right)  # 右

        # 中节点：用当前root的值加上pre的值
        root.val += self.pre.val    # 中
        self.pre = root             

        self.traversal(root.left)   # 左