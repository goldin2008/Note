class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        # R = true表示本轮循环结束后，字符串里依然有R。D同理
        R , D = True, True

        # 当flag大于0时，R在D前出现，R可以消灭D。当flag小于0时，D在R前出现，D可以消灭R
        flag = 0

        senate = list(senate)
        while R and D: # 一旦R或者D为false，就结束循环，说明本轮结束后只剩下R或者D了
            R = False
            D = False
            for i in range(len(senate)) :
                if senate[i] == 'R' :
                    if flag < 0: senate[i] = '0' # 消灭R，R此时为false
                    else: R = True # 如果没被消灭，本轮循环结束有R
                    flag += 1
                if senate[i] == 'D':
                    if flag > 0: senate[i] = '0'
                    else: D = True
                    flag -= 1
        # 循环结束之后，R和D只能有一个为true
        return "Radiant" if R else "Dire"
