# 1st method will be check if the next index element is equal or greater 

# main challenge here is is the array is sorted and rotated. means after rotation wheather it is sorted 

# the logic is if sorted the nbreakpoint is 0 and if sorted and rotated then braeakpooints will be 1

def sortedrotated(A):
    breakpoints=0
    for i in range(len(A)):
        if A[i-1]>A[i]:
            breakpoints+=1
    if breakpoints<=1:
        return True
    return False      
