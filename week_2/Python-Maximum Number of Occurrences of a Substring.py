from collections import defaultdict, Counter
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        result = 0
        #O(n x maxSize-minSize)
        """ for length in range(minSize, maxSize+1):
            count = defaultdict(int)
            unique_chars = Counter()
            l = 0
            for r in range(len(s)):
                unique_chars[s[r]]+=1
                if r-l+1 > length:
                    unique_chars[s[l]]-=1
                    if unique_chars[s[l]]==0:
                        del unique_chars[s[l]]
                    l+=1
                if r-l+1 == length and len(unique_chars) <= maxLetters:
                    count[s[l:r+1]] += 1
                    result = max(result, count[s[l:r+1]])"""
                
        # Optimized Algorithm Using minSize Only
        # We only consider substrings of minSize because, for any valid substring of a larger size, there will be a substring of size minSize that should also be valid and will potentially occur as frequently or more. Here’s how to implement this optimization:
        
        count = defaultdict(int)
        unique_chars = Counter()
        l = 0
        for r in range(len(s)):
            unique_chars[s[r]]+=1
            if r-l+1 > minSize:
                unique_chars[s[l]]-=1
                if unique_chars[s[l]]==0:
                    del unique_chars[s[l]]
                l+=1
            if r-l+1 == minSize and len(unique_chars) <= maxLetters:
                count[s[l:r+1]] += 1
                result = max(result, count[s[l:r+1]])
        return result