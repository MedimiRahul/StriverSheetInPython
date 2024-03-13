
# ^ there are multiple ways to sort general sorting algorithms can do 
# ^ second alternative would be count the number of occurances using map 
# ^ and then overwrite the array

# ^ third method would be using DNf sort 

def sortarray01(A):
    counti={}
    for i in range(len(A)):
        counti.setdefault(A[i],0)
        counti[A[i]]+=1
    i=0
    count0=counti[0]
    count1=counti[1]
    count2=counti[2]
    while count0!=0:
        A[i]=0
        count0-=1
        i+=1
    while count1!=0:
        A[i]=1
        count1-=1
        i+=1
    while count2!=0:
        A[i]=2
        count2-=1
        i+=1

A=[1,1,2,0,0,2,0,1]
sortarray01(A)
print(A)               
               


def DNFsort(A):
    low=0
    mid=0
    end=len(A)-1

    while mid<=end:
        if A[mid]==0:
            A[low],A[mid]=A[mid],A[low]
            low+=1
            mid+=1
        elif A[mid]==1:
            mid+=1
        elif A[mid]==2:
            A[end],A[mid]=A[mid],A[end]
            end-=1

A=[1,1,2,0,0,2,0,1]
DNFsort(A)
print(A)                             

 