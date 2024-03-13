
# ^ so to generate number of possible permutaions (n!) 

# ^ [[1,2],[2,1]]

def possiblepermutation(A,n):
    if n==1:
        return [A[:n]]
    numofp=possiblepermutation(A,n-1)
    totalp=[]
    for i in range(len(numofp)):
        x=numofp[i]
        for j in range(len(x)+1):
            y=[i for i in x]
            y.insert(j,A[n-1])
            totalp.append(y)
    return totalp

A=[1,2,3]
print(possiblepermutation(A,3))        

