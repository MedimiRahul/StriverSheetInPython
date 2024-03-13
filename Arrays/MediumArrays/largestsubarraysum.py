
# ^ largest subarray sum can be find in multiple ways 
# ^ we can find all possible subarrays using two loops and find max sum 
# ^ scond method can be we can use sliding window of all possible window sizes an compare the sum 
# ^ third is optimized that is kandane algorithm 

# ^ brute force 

def largestsum1(A):
    maxi=-99999999999
    for i in range(len(A)):
        sumi=0
        for j in range(i,len(A)):
            sumi+=A[j]
            if sumi>maxi:
                maxi=sumi    
    return maxi


print(largestsum1([-2,1,-3,4,-1,2,1,-5,4]))


# ^ kadane algorithm is based on the fact that we will not contribute -ve numbers to the sum 

def kadanealgo(A):
    maxsum=0
    maxsofar=-999999999
    for i in range(len(A)):
        maxsum+=A[i]
        if maxsum>maxsofar:
            maxsofar=maxsum
        if maxsum<0:
            maxsum=0
    return maxsofar

print(kadanealgo([-2,1,-3,4,-1,2,1,-5,4]))

