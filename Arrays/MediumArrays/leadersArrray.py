
# ^ leaders means element greater than all the elemnts to the right 
# ^brute force method would be check each and every element with the elments to the right side 
# ^ optimised method would be check from end and also store the max so far value so that 
# ^ we can compare the element with the max value

def leadersArray(A):
    maxi=-999999999
    leaders=[]
    for i in range(len(A)-1,-1,-1):
        if i==len(A)-1:
            leaders.append(A[i])
            maxi=A[i]
        else:
            if A[i]>maxi:
                leaders.append(A[i])
                maxi=A[i]
    res=[leaders[i] for i in range(len(leaders)-1,-1,-1)]
    return res 

print(leadersArray([4,7,1,0]))



