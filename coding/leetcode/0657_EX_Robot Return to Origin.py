# 时间复杂度：O(n)
# 空间复杂度：O(1)
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x = 0 # 记录当前位置
        y = 0
        for i in range(len(moves)):
            if (moves[i] == 'U'):
                y += 1
            if (moves[i] == 'D'):
                y -= 1
            if (moves[i] == 'L'):
                x += 1
            if (moves[i] == 'R'):
                x -= 1
        return x == 0 and y == 0
