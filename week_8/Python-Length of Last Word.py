# https://leetcode.com/problems/length-of-last-word/
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        if len(s)==1 and s[0]!=" ":
            return 1
        cnt = 0
        i = len(s)-1
        while i>0:
            if s[i]!=" ":
                break    
            i-=1
        while i>=0 and s[i]!= ' ':
            i-=1
            cnt+=1
        return cnt

if __name__ == "__main__":
    sol = Solution()
    def test_lengthOfLastWord():
        assert sol.lengthOfLastWord("a ") == 1, " test 1 passed"
        assert sol.lengthOfLastWord("   fly me   to   the moon  ") == 4, "test 2 passed"
        assert sol.lengthOfLastWord("Hello World") == 5, "test 3 passed"
        print("All test cases passed!")
    test_lengthOfLastWord()