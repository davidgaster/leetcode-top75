# https://leetcode.com/problems/word-break-ii/
from collections import defaultdict
class Solution:
    
    '''
    Recursion with memoization.
    memo --> <str, [words]>
    Loop through input string, check current slice of the word is in the
    word dict, if so recurse on rest of word, add it to memo list
    '''
    def wordBreak(self, inp: str, wordDict: List[str]) -> List[str]:
        
        def dfs(inp):
            
            if inp in memo:
                return memo[inp]
            
            if inp is "":
                return [[]]
            
            for i in range(1,len(inp)+1):
                start = inp[:i]
                if start in wordSet:
                    for rest in dfs(inp[i:]):
                        memo[inp].append([start] + rest)
            
            return memo[inp]
            
        memo = defaultdict(list)
        wordSet = set(wordDict)
        ans = dfs(inp)
        return [' '.join(words) for words in ans]
            

    