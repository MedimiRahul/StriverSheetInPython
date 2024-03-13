
# ^ here also we can find each and every subarray and find the max sum 
# ^ lets try to use kadane algo to find the elements 


# ^ here the concept is we have a breakpoint when we hit -ve number and becomes 0
# ^ so there we are startig a new so there first index once again initiating
# ^ and for last index what we are doing wverytime maxsum is more than maxsofar we are updating lastindex

def printlargestsubarray(A):
    firstindex=0
    lastindex=0
    maxsum=0
    maxsofar=-999999999
    for i in range(len(A)):
        maxsum+=A[i]
        if maxsum>maxsofar:
            maxsofar=maxsum
            lastindex=i
        if maxsum<0:
            maxsum=0
            firstindex=i+1
    return firstindex,lastindex,maxsofar
A=[-2,1,-3,4,-1,2,1,-5,4]
x=printlargestsubarray([-2,1,-3,4,-1,2,1,-5,4])
print(A[x[0]:x[1]+1],x)
