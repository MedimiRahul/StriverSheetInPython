
# ^ so the first and foremost brute force method would be store th epositives in one array
# ^ and negatives in anaother array and the nfrom each array pick and add in resulting array 

# ^ if we dont want to use extra space for +ve and -ves 
# ^ arr[] = {1,2,-3,-1,-2,3}, N = 6
# ^ so waht we can do is swapping with +ve and -ve if not alternate 

def returnalternate(A):
    for i in range(len(A)):
        if (i%2==0 and A[i]>0) or (i%2==1 and A[i]<0):
            pass
        else:
            if A[i]>0:
                for j in range(i+1,len(A)):
                    if A[j]<0:
                        A[i],A[j]=A[j],A[i]
                        break
            else:
                for j in range(i+1,len(A)):
                    if A[i]>0:
                        A[i],A[j]=A[j],A[i]
                        break

A=[1,2,-3,-1,-2,3]     
returnalternate(A)
print(A)  

# ^ above code is not good 

def returealternate2(A):
    pos=0
    neg=1
    res=[0 for i in range(len(A))]
    for i in range(len(A)):
        if A[i]>0:
            if pos<len(A):
                res[pos]=A[i]
                pos+=2
        else:
            if neg<len(A):
                res[neg]=A[i]
                neg+=2
    return res            

A=[1,2,-3,-1,-2,3]     
print(returealternate2(A))              











