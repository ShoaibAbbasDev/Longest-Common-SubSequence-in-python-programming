# recursive LCM algorithum imeplented in python

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
