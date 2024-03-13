
# ^ two sum problem 
# ^ first method would be find each and every pair which corresponds to sum 
# ^ so it would be o(n^2) 

# ^ second method would be sort and using two pointers find the sum 

def twosum1(A,target):
    for i in range(len(A)):
        for j in range(i+1,len(A)):
            sumi=A[i]+A[j]
            if sumi==target:
                return True
    return False

print(twosum1([2,6,5,8,11],14))


def twosum2(A,target):
    A.sort()
    i=0
    j=len(A)-1
    sumi=0
    while i<=j:
        sumi=A[i]+A[j]
        if sumi==target:
            return True
        if sumi>target:
            sumi-=A[j]
            j-=1
        if sumi<target:
            sumi-=A[i]
            i+=1
    return False            

print(twosum2([2,6,5,8,11],15))
