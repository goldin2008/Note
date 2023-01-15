class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # Greedy Algo:
        # 从下往上安装摄像头：跳过leaves这样安装数量最少，局部最优 -> 全局最优
        # 先给leaves的父节点安装，然后每隔两层节点安装一个摄像头，直到Head
        # 0: 该节点未覆盖
        # 1: 该节点有摄像头
        # 2: 该节点有覆盖
        
        result = 0
        # 从下往上遍历：后序（左右中）
        def traversal(curr: TreeNode) -> int:
            nonlocal result
            
            if not curr: return 2
            left = traversal(curr.left)
            right = traversal(curr.right)

            # Case 1:
            # 左右节点都有覆盖
            if left == 2 and right == 2: 
                return 0

            # Case 2:
                # left == 0 && right == 0 左右节点无覆盖
                # left == 1 && right == 0 左节点有摄像头，右节点无覆盖
                # left == 0 && right == 1 左节点有无覆盖，右节点摄像头
                # left == 0 && right == 2 左节点无覆盖，右节点覆盖
                # left == 2 && right == 0 左节点覆盖，右节点无覆盖
            elif left == 0 or right == 0: 
                result += 1
                return 1

            # Case 3:
                # left == 1 && right == 2 左节点有摄像头，右节点有覆盖
                # left == 2 && right == 1 左节点有覆盖，右节点有摄像头
                # left == 1 && right == 1 左右节点都有摄像头
            elif left == 1 or right == 1:
                return 2
            
            # 其他情况前段代码均已覆盖

        if traversal(root) == 0:
            result += 1
            
        return result
