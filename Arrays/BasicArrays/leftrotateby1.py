# left rotate array by one 
# so first method will be just remove first element from array and push it to last 

# in low level what we can do is shift each element onw step ahead

def rotateleft(A):
    first=A[0]
    for i in range(1,len(A)):
        A[i-1]=A[i]
    A[len(A)-1]=first

A=[3,4,5]
rotateleft(A)
print(A)        
