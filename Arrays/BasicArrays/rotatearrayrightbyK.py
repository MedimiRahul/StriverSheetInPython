# rotate array to right k times 
# so baseic method is using built in pop pop then insert at beginning 

# another is just split the array from start upto len(arr)-k then add two arrays 
# so basically we are using an extra space and then rotated 

# in order to do using inplace we can use reversal algorithm 
# reversal algorithm states that 

# first upto k you just reverse the things .
# then indivisually reverse upto k and k:last

def rotaterightk(A,k):
    i=0
    j=len(A)-1
    while i<k:
        A[i],A[j]=A[j],A[i]
        i+=1
        j-=1
    def reversearray(A,start,end):
        i=start
        j=end
        while i<=j:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1

    reversearray(A,0,k-1)
    reversearray(A,k,len(A)-1)
    reversearray(A,2*k,len(A)-1)

A=[1,2,3,4,5,6,7,8]
k=2
rotaterightk(A,k)
print(A)             
    