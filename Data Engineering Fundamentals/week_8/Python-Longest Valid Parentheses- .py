# https://leetcode.com/problems/longest-valid-parentheses/
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        if len(s)<=1:
            return 0
        last_parenthese = -1
        max_length = 0
        for i in range(len(s)):
            char = s[i]
            if char=="(":
                stack.append(i)
            elif stack:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    max_length = max(max_length, i-last_parenthese)
            else:
                last_parenthese = i
        return max_length

if __name__ == "__main__":
    sol = Solution()
    def test_longestValidParentheses():
        assert sol.longestValidParentheses("()((()()") == 4, "Test Case 1 Failed"
        assert sol.longestValidParentheses(")()())()()(") == 4, "Test Case 2 Failed"
        assert sol.longestValidParentheses("((()()") == 4, "Test Case 3 Failed"
        print("All test cases passed!")
    test_longestValidParentheses()
    