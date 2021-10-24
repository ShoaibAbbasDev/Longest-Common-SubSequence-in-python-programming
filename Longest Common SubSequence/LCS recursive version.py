'''
# recursive LCM algorithum imeplented in python
# python LCM recusive algorithm were funtion calling itself many time until finding Longest common subsequence LCM
'''
def lcs(x,y,m,n):
    if m==0 or n==0:
        return 0;
    elif x[m-1] == y[n-1]:
        return 1+ lcs(x,y,m-1,n-1);
    else:
        return max(lcs(x,y,m-1,n),lcs(x,y,m,n-1));

x=input("Enter String 1 .... ")
y=input("Enter String 2 .... ")
print("The Total length of LCS is  ",lcs(x,y,len(x),len(y)))


# Dynamic Programming implementation of LCS problem

def lcs(X, Y):
	# find the length of the strings
	m = len(X)
	n = len(Y)

	# declaring the array for storing the dp values
	L = [[None]*(n + 1) for i in range(m + 1)]

	"""Following steps build L[m + 1][n + 1] in bottom up fashion
	Note: L[i][j] contains length of LCS of X[0..i-1]
	and Y[0..j-1]"""
	for i in range(m + 1):
		for j in range(n + 1):
			if i == 0 or j == 0 :
				L[i][j] = 0
			elif X[i-1] == Y[j-1]:
				L[i][j] = L[i-1][j-1]+1
			else:
				L[i][j] = max(L[i-1][j], L[i][j-1])

	# L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
	return L[m][n]
# end of function lcs


# Driver program to test the above function
X = "AGGTAB"
Y = "GXTXAYB"
print("Length of LCS is ", lcs(X, Y))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

