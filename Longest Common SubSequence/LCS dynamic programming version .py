# Implementing LCS using dynamic programming
def lcs(x, y):
    m = len(x)
    n = len(y)
    
    # Initialize a 2D list (matrix) with zeros
    dp_table = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Build the dp_table matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # Compare current characters
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
            else:
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i][j - 1])
    
    return dp_table[m][n]  # The bottom-right corner contains the length of LCS

# Input and output handling
if __name__ == "__main__":
    print("******************* Start *******************************")
    x = input("Please Enter String 1: ")
    y = input("Please Enter String 2: ")
    print("The Total length of LCS is:", lcs(x, y))
    print("******************* End *********************************")
