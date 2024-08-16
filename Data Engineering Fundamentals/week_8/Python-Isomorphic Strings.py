# https://leetcode.com/problems/isomorphic-strings/
from collections import defaultdict
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        def isIso(s,t):
            mapping = defaultdict()
            isIsomorphic = True
            for i in range(len(s)):
                char_s = s[i]  
                char_t = t[i]
                if char_s in mapping:  
                    if mapping[char_s] == char_t:
                        continue
                    else:  
                        return False  
                else:  
                    mapping[char_s] = char_t  
            
            return isIsomorphic
        return isIso(s,t) and isIso(t,s)
if __name__ == "__main__":
    sol = Solution()
    def test_isIsomorphic():
        assert sol.isIsomorphic("egg","add") == True, "Test Case 1 Failed"
        assert sol.isIsomorphic("badc","baba") == False, "Test Case 2 Failed"
        assert sol.isIsomorphic("aaabbbab","bbbaaaab") == False, "Test Case 3 Failed"
        print("All test cases passed!")
    test_isIsomorphic()
    

            