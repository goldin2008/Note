class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # defaultdic(list) 是为了方便直接append
        tickets_dict = defaultdict(list)
        for item in tickets:
            tickets_dict[item[0]].append(item[1])
	# 给每一个机场的到达机场排序，小的在前面，在回溯里首先被pop(0）出去
	# 这样最先找的的path就是排序最小的答案，直接返回
        for airport in tickets_dict: tickets_dict[airport].sort()
        '''
        tickets_dict里面的内容是这样的
        {'JFK': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['JFK', 'SFO']})
        '''
        path = ["JFK"]
        def backtracking(start_point):
            # 终止条件
            if len(path) == len(tickets) + 1:
                return True
            for _ in tickets_dict[start_point]:
                #必须及时删除，避免出现死循环
                end_point = tickets_dict[start_point].pop(0)
                path.append(end_point)
                # 只要找到一个就可以返回了
                '''
                如果找到一条path，就会一直return True，不会到下一个statement, path.pop()
                如果在一条枝上没找到一条path,就会return None，那么就会运行下一个statement，path.pop()
                然后回溯，来换到另一个枝上测试是不是能找到一条path
                '''
                if backtracking(end_point):
                    return True
                path.pop()
                tickets_dict[start_point].append(end_point)

        backtracking("JFK")
        return path
