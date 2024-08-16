from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        num_str = [ str(n) for n in nums]
        num_str.sort(reverse=True)
        i=1
        while i <len(num_str):
            a, b = num_str[i-1], num_str[i]
            if int(a+b) < int(b+a):
                num_str[i], num_str[i-1] = num_str[i-1], num_str[i]
                i = max(1, i - 1)  # Check the previous pair again
            else:
                i += 1
        result = ''.join(num_str)
        if result[0]=='0':
            return '0'
        return result



if __name__ == "__main__":
    nums = [74,21,33,51,77,51,90,60,5,56]
   
    sol = Solution()
    ans = sol.largestNumber(nums)  #"9077746056551513321"
    assert ans=="9077746056551513321"
