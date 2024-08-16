# https://leetcode.com/problems/zigzag-conversion/
"""
Strategy to Solve the Problem:
Edge Cases: If numRows is 1, then the zigzag is just the original string. Return the string as is.

Row Tracking: Use a list of strings to keep track of the characters for each row.

Direction Control: Utilize a variable to determine whether the direction is "down" the rows or needs to "turn" at the top or bottom to go back up.

Iteration over Characters:

Append characters to the appropriate row based on the current position and direction.
Adjust the current row index (currRow) accordingly: increment when moving down, decrement when moving up.
Construct the Result String: Once all characters have been placed into their respective rows, concatenate all rows to form the final string.

"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or len(s)<=numRows:
            return s

        row = [''] * numRows
        goDown = False
        curRow = 0

        for char in s:
            row[curRow]+=char
            if curRow==0 or curRow==numRows-1:
                goDown = not goDown
            curRow +=1 if goDown else -1
        return ''.join(row)

if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 3
    sol = Solution()
    ans = sol.convert(s,numRows) #"PAHNAPLSIIGYIR"
        