#https://leetcode.com/problems/minimum-window-substring/
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) == len(t) ==1:
            if s==t:
                return s
            else:
                return ""
        if len(t)> len(s):
            return ""
        
        start_idx = 0
        end_idx = 0
        min_len = float('inf')
        min_start_idx = 0
        min_end_idx = 0
        required_chars = len(t)
        char_count_t = defaultdict(int)
        for char in t:
           char_count_t[char]+=1
         
        while end_idx < len(s):
            if s[end_idx] in char_count_t:
                if char_count_t[s[end_idx]] > 0:
                    required_chars -= 1
                char_count_t[s[end_idx]] -= 1

            while required_chars == 0:
                if end_idx - start_idx < min_len:
                    min_len = end_idx - start_idx
                    min_start_idx = start_idx
                    min_end_idx = end_idx

                if s[start_idx] in char_count_t:
                    char_count_t[s[start_idx]] += 1
                    if char_count_t[s[start_idx]] > 0:
                        required_chars += 1

                start_idx += 1

            end_idx += 1
        return s[min_start_idx:min_end_idx+1] if min_len != float('inf') else ""

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    sol = Solution()
    ans = sol.minWindow(s,t)
        