# https://leetcode.com/problems/maximum-swap/
class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of characters (digits)  
        digits = list(str(num))  
        max_index = [-1] * 10  # To store the last occurrence of each digit (0-9)  
        
        # Record the last occurrence of each digit  
        for i in range(len(digits)): 
            print(digits[i])
            max_index[int(digits[i])] = i  
        print(max_index)
        # Try to find the first digit that can be swapped to make a larger number  
        for i in range(len(digits)):  
            # Check for a larger digit to the right of the current digit  
            for d in range(9, int(digits[i]), -1):  
                if max_index[d] > i:  
                    # We found a larger digit to swap with, perform swap  
                    digits[i], digits[max_index[d]] = digits[max_index[d]], digits[i]  
                    # Convert the list of chars back to an integer  
                    return int(''.join(digits))  
        
        # If no swap was made, return the original number  
        return num  
    

if __name__ == '__main__':

    num = 2736
    sol = Solution()
    ans = sol.maximumSwap(num) #ans = 7236
    print(ans) 