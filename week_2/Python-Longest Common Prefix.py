class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortes_len = float('inf')
        prefix = ''
        for word in strs:
            if len(word)<  shortes_len:
                shortes_len = len(word)
                shortest_word = word
        i = 0
        while i < shortes_len:
            same = True
            for word in strs:
                if shortest_word[i]!= word[i]:
                    same = False
            if same:
                prefix += shortest_word[i]
                i+=1
            else:
                break
        return prefix


strs = ["flower","flow","flight"]
sol = Solution()
ans = sol.longestCommonPrefix(strs)
print(ans)