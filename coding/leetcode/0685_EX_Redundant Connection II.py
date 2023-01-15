class Solution:

    def __init__(self):
        self.n = 1010
        self.father = [i for i in range(self.n)]


    def find(self, u: int):
        """
        并查集里寻根的过程
        """
        if u == self.father[u]:
            return u
        self.father[u] = self.find(self.father[u])
        return self.father[u]

    def join(self, u: int, v: int):
        """
        将v->u 这条边加入并查集
        """
        u = self.find(u)
        v = self.find(v)
        if u == v : return
        self.father[v] = u
        pass


    def same(self, u: int, v: int ):
        """
        判断 u 和 v是否找到同一个根，本题用不上
        """
        u = self.find(u)
        v = self.find(v)
        return u == v

    def init_father(self):
        self.father = [i for i in range(self.n)]
        pass

    def getRemoveEdge(self, edges: List[List[int]]) -> List[int]:
        """
        在有向图里找到删除的那条边，使其变成树
        """

        self.init_father()
        for i in range(len(edges)):
            if self.same(edges[i][0], edges[i][1]): # 构成有向环了，就是要删除的边
                return edges[i]
            self.join(edges[i][0], edges[i][1]);
        return []

    def isTreeAfterRemoveEdge(self, edges: List[List[int]], deleteEdge: int) -> bool:
        """
        删一条边之后判断是不是树
        """

        self.init_father()
        for i in range(len(edges)):
            if i == deleteEdge: continue
            if self.same(edges[i][0], edges[i][1]): #  构成有向环了，一定不是树
                return False
            self.join(edges[i][0], edges[i][1]);
        return True

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(self.n)]

        for i in range(len(edges)):
            inDegree[ edges[i][1] ] += 1

        # 找入度为2的节点所对应的边，注意要倒序，因为优先返回最后出现在二维数组中的答案
        towDegree = []
        for i in range(len(edges))[::-1]:
            if inDegree[edges[i][1]] == 2 :
                towDegree.append(i)

        # 处理图中情况1 和 情况2
        # 如果有入度为2的节点，那么一定是两条边里删一个，看删哪个可以构成树
        if len(towDegree) > 0:
            if(self.isTreeAfterRemoveEdge(edges, towDegree[0])) :
                return edges[towDegree[0]]
            return edges[towDegree[1]]

        # 明确没有入度为2的情况，那么一定有有向环，找到构成环的边返回就可以了
        return self.getRemoveEdge(edges)
