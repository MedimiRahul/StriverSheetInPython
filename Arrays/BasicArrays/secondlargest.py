# 1st method will be find the largest . then apply condition that it would be largest but smaller than
# 1st largest.

def secondlargest(A):
    firstlarge=-999999
    secondlarge=-9999999
    for i in range(len(A)):
        if A[i]>firstlarge:
            firstlarge=A[i]

    for i in range(len(A)):
        if A[i]>secondlarge and A[i]<firstlarge:
            secondlarge=A[i]
    return secondlarge

A=[8,5,1,9,4,6,10,-5,200]            
print(secondlargest(A))



# lets try to make in single transversal 

def secondlargestoptimize(A):
    firstlarge=-99999999
    secondlarge=-9999999
    for i in range(len(A)):
        if A[i]>firstlarge:
            secondlarge=firstlarge
            firstlarge=A[i]
    return secondlarge
        
        
print(secondlargestoptimize(A))

