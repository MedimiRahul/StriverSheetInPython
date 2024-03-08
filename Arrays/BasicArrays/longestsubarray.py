
# ^so longest subarrray with sum k can be done in multiple ways 
# ^ find all the subarrrays with suk k and then find the max count 

# ^only positives we have considered in this quetion 

def longest1(A,k):
    maxi=-999999
    for i in range(len(A)):
        sumi=0
        counti=0
        for j in range(i,len(A)):
            sumi+=A[j]
            if sumi==k:
                counti=j-i+1
                if counti>maxi:
                    maxi=counti
                break    

    return maxi

print(longest1([2,3,5,1,9],10))


# ^second method we can do is using sliding window since we require subarray

def longest2(A,k):
    i=0
    j=0
    sumi=0
    maxi=0
    while i<=j and j<len(A):
        sumi+=A[j]
        if sumi==k:
            if (j-i+1)>maxi:
                maxi=j-i+1
            j+=1    
        elif sumi>k:
            sumi-=A[i]
            i+=1
        elif sumi<k:
            j+=1         
    return maxi

print(longest2([-1,1,1],1))





