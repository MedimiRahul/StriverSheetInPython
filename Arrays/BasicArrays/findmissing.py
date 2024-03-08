# so most basic method will be linear search . 
# just maintain the variable and do linear search.

# another approach we can do is just search each and every number in that sorted array using binary search 
# which element not found return it.

# method1

def missing1(A,n):
    target=1
    for i in range(len(A)):
        if target!=A[i]:
            return target
        target+=1

A=[1,2,4,5]  
print(missing1(A,5))   

# method 2 will be find each and every element using binary search .

def binarysearch(A,num,start,end):
    mid=(start+end)//2
    if start>end:
        return False
    if A[mid]==num:
        return True
    elif A[mid]>num:
        return binarysearch(A,num,start,mid-1)
    elif A[mid]<num:
        return binarysearch(A,num,mid+1,end)
    
print(binarysearch([1,2,3,4,5],1,0,4))    

# so each time call this function 

# third method will be is to create the map with folllowing numbers as keys  and count its frequecy

# fourth method would be using mathematics . sum of numbers - sum of array would give missing numbers.
# sum of first n integers is n(n+1)/2

# forth is using xor . since xor of same elemets is 0 and xor of element with 0 is element itself
#  (so xor of all numbers ) ^ (xor of array) gives us misssing number 

def third(A,n):
    sumofn=(n*(n+1))//2
    sumi=0
    for i in A:
        sumi+=i
    return sumofn-sumi

A=[1,2,4,5]  
print(third(A,5))   

def forth(A,n):
    xorn=0
    xorA=0
    for i in range(1,n+1):
        xorn=xorn^i
    for i in range(len(A)):
        xorA=xorA^A[i] 
    return xorn^xorA       

A=[1,2,3,4,5]  
print(forth(A,5))   










