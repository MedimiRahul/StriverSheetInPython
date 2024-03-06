# 1st method is o(n^2) compare each and every item 
def large1(A):
    maxi=-9999999
    for i in range(len(A)):
        if A[i]>maxi:
            maxi=A[i]
    return maxi            



A=[8,5,1,9,4,6,10,-5,200]            
print(large1(A))


# recursive method 
def recurlarge(A,n):
    if n==1:
        return A[0]
    x=recurlarge(A,n-1)
    if A[n-1]>x:
        x=A[n-1]
    return x

A=[8,5,1,9,4,6,10,-5,200]            
print(recurlarge(A,len(A)))

