# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        seem = set()
        while n !=1 and n not in seem:
            seem.add(n)
            n = sum([int(num)**2 for num in str(n)])
        return n==1

if __name__ == '__main__':
    n = 19
    sol = Solution()
    ans = sol.isHappy(n) #True