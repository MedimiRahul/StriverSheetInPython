# move zeros to the end 
# so just start from end and if non zero no swap otherwise swap it 

# brute force would be just collecr non zeros and zeros seperately then combine it 
# and then seeing it migrate the original array

# so extra space is requtired

# optimised will be swapping by checkig from the last.

def movezerostoend(A):
    i=0
    j=len(A)-1
    while i<=j:
        if A[i]==0 and A[j]==0:
            j-=1
        elif A[i]!=0 and A[j]==0:
            i+=1
            j-=1
        elif A[i]==0 and A[j]!=0:
            A[i],A[j]=A[j],A[i]
            i+=1
            j-=1
        elif A[i]!=0 and A[j]!=0:
            i+=1

A=[1 ,0 ,2 ,3 ,0 ,4 ,0 ,1]       
movezerostoend(A)
print(A)                



