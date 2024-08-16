# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse(self, x: int) -> int:
        
        x_str =  str(abs(x))
        reverse = x_str[::-1]
        result = int(reverse) 
        if x < 0:
            return  -result if -result > -(2**31) else 0
        return result if result < (2**31)-1 else 0
if __name__ == '__main__':
    x = -123
    sol = Solution()
    ans = sol.reverse(x)

    print(ans)