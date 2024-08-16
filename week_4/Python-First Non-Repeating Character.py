from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = defaultdict(int)
        for word in s:
            count_dict[word]+=1
        for i in range(len(s)):
            if count_dict[s[i]]==1:
                return i
        return -1


if __name__ == '__main__':
    s = "leetcode"
    sol = Solution()
    ans = sol.firstUniqChar(s) # ans = 0
    print(ans)
