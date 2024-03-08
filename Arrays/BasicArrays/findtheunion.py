# to find the union of arrays multiple ways are there 
# first is add the array then we can pass it into set data structure 

# second is without using extraspace using two pointers 

# third is using map we can store the frequency of elements and can append the keys 


def findunion(A,B):
    i=0
    j=0
    res=[]
    while i<len(A) and j<len(B):
        if A[i]<B[j]:
            if len(res)==0 or (len(res)!=0 and res[len(res)-1]!=A[i]):
                res.append(A[i])   
            i+=1
        elif A[i]==B[j]:
            if len(res)==0 or (len(res)!=0 and res[len(res)-1]!=A[i]):
                res.append(A[i])   
            i+=1
            j+=1
        elif A[j]<B[i]:  
            if (len(res)==0) or (len(res)!=0 and res[len(res)-1]!=A[j]):
                res.append(A[j])   
            j+=1  

    while i<len(A):
        if res[-1]!=A[i]:
            res.append(A[i])
        i+=1
    while j<len(B):
        if res[-1]!=B[j]:
            res.append(B[j])
        j+=1
    return res    

A=[1,2,3,4,5,6,7,8,9,10]
B=[2,3,4,4,5,11,12]

print(findunion(A,B))         