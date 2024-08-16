"""Let 1 represent ‘A’, 2 represents ‘B’, etc. Given a digit sequence, count the number of possible decodings of the given digit sequence. """
def numDecodings(s):
    dp = [0]* (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0

    for i in range(2, len(s)+1):
        if s[i-1]!='0':
            dp[i]+=dp[i-1]
        
        twoDigits = int(s[i-2:i])
        if 10 <= twoDigits <= 26:
            dp[i]+=dp[i-2]

    return dp[len(s)]

numDecodings("20")