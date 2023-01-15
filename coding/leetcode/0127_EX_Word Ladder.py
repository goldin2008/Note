class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if len(wordSet)== 0 or endWord not in wordSet:
            return 0
        mapping = {beginWord:1}
        queue = deque([beginWord]) 
        while queue:
            word = queue.popleft()
            path = mapping[word]
            for i in range(len(word)):
                word_list = list(word)
                for j in range(26):
                    word_list[i] = chr(ord('a')+j)
                    newWord = "".join(word_list)
                    if newWord == endWord:
                        return path+1
                    if newWord in wordSet and newWord not in mapping:
                        mapping[newWord] = path+1
                        queue.append(newWord)                      
        return 0
