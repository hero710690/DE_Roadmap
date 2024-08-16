# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        if len(s)<1:
            return max_len
        
        char_set = set()
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1
            char_set.add(s[right])
            max_len = max(max_len, len(char_set))
        return max_len

if __name__=='__main__':
    sol = Solution()
    def test_lengthOfLongestSubstring():
        assert sol.lengthOfLongestSubstring(" ") == 1, "Test Case 1 Failed"
        assert sol.lengthOfLongestSubstring("bbbbb") == 1, "Test Case 2 Failed"
        assert sol.lengthOfLongestSubstring("pwwkew") == 3, "Test Case 3 Failed"
        print("All test cases passed!")

    test_lengthOfLongestSubstring()