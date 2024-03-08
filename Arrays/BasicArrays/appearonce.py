
# ?so first basic method will be to create a map and Store the occurances 
# ?then which one has single occurance return it 
# ?it is using extra space 

# ?second method what we can do is using XOR. 
# ?as we know XOR of same elents will return 0 so xor of all the elemnts will
# ?return the single element as XOR of single elment with 0 is itself. 

def appearonce(A):
    xora=0
    for i in range(len(A)):
        xora^=A[i]
    return xora

print(appearonce([2,2,1]))    

