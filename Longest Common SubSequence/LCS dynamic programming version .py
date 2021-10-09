
# implement least common subsequence using dynamic programming
# LCM dynamic programming using python language

def lcs(x,y):
    m=len(x)
    n=len(y)
    L=[[None]*(n+1)for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                L[i][j]=0
            elif x[m-1]==y[n-1]:
                L[i][j]=L[i-1][j-1]+1
            else:
                L[i][j]=max(L[i-1][j],L[i][j-1])
    return L[m][n]
print("******************* Start *******************************")
x=input("Please Enter String 1 ...... ")
y=input("Please Enter String 2 ........ ")
print("The Total length of LCS is  ",lcs(x,y))
print("******************* End *******************************")


