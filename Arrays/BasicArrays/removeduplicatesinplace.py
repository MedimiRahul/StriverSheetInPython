# since the array is sorted we can just find unique elemets using set then place in order 
# this was the first method 

# second will be using two pointers 

def removedup(A):
    curr=1
    prev=0
    count=1
    while curr<len(A):
        if A[curr]==A[prev]:
            curr+=1
        else:
            prev+=1
            A[prev]=A[curr]
            curr+=1
            count+=1
    return count

A=[1,1,1,2,2,3,4,5,6,6,7]
print(removedup(A))
print(A)            



