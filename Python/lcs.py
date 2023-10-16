# Given two strings, find the length and the actual LCS (Longest Common Subsequence).

def lcs(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for x in range(n+1)] for x in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if (i == 0 or j == 0):
                dp[i][j] = 0
            elif (s1[i-1] == s2[j-1]):
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i][j-1], dp[i-1][j])
    
    index = dp[m][n]
    lcs = [""] * (index+1)
    lcs[index] = ""
    i = m
    j = n
    while (i > 0 and j > 0):
        if (s1[i-1] == s2[j-1]):
            lcs[index-1] = s1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif (dp[i-1][j] > dp[i][j-1]):
            i -= 1
        else:
            j -= 1
    return dp[m][n], "".join(lcs)

if __name__ == '__main__':
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    s1 = "ABCDGH"
    s2 = "AEDFHR"
    print(lcs(s1, s2))
    