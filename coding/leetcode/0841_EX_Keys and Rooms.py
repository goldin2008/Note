class Solution:
    def dfs(self, key: int, rooms: List[List[int]]  , visited : List[bool] ) :
        if visited[key] :
            return
        visited[key] = True
        keys = rooms[key]
        for i in range(len(keys)) :
            # 深度优先搜索遍历
            self.dfs(keys[i], rooms, visited)

    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [False for i in range(len(rooms))]

        self.dfs(0, rooms, visited)

        # 检查是否都访问到了
        for i in range(len(visited)):
            if not visited[i] :
                return False
        return True
