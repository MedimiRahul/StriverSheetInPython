# we can maintain a variable called count and when there is 1 we will add and 
# when it hits zero then count would be again 0. 

def consequtives1(A):
    count=0
    maxi=-999999999
    for i in range(len(A)):
        if A[i]==1:
            count+=1
            if count>maxi:
                maxi=count
        else:
            count=0
    return maxi

print(consequtives1([1,0,1,1,0]))                