這題用 dfs memoization
https://medium.com/data-science-for-kindergarten/140-word-break-ii-b52e3a89eb1c

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
      
        #上圖可看出當string為"dogo"時，底下情況都相同，因此建立memo來儲存這種重複的情況
        memo = {}

        def dfs(string):
             
            #running dfs 遇到有在memo裡的string直接回傳
            if string in memo:
                return memo[string]
            
            #dfs到最後一位沒有字母了則return [""]
            if not string:
                return [""]
            
            #建立一個local_res紀錄每一個string回傳的word
            local_res = []

            for word in wordDict:
                
                #看string中有沒有包含word
                if string.startswith(word):
                    #如果有包含word，則剩下的部分為string[len(word):]
                    #再去run dfs
                    sub_words = dfs(string[len(word):])
                    
                    #go through 下一層(dfs(string[len(word):])的word加入當前的local_res並return
                    for sub_word in sub_words:
                        #這邊注意字與字之間用" "連接，且當回傳""時，以""連接，最後一個word後面才不會有" "
                        local_res.append(word + (" " if sub_word else "") + sub_word)

            #例如dfs()先走到最後一位沒有字母
            #memo[""]=[""] 接著return到上一層
            #memo["go"]=["go"]
            #memo["dogo"]=["do go"]
            #memo["sanddogo"]=["sand do go"]
            #memo["catsanddogo"]=["cat sand do go"] (其中一個path)

            memo[string] = local_res
            return local_res

        return dfs(s)