
# ^ majority element can be found using multiple ways 
# ^ we can count and store in map 
# ^ second is using moores voting algo 

def mooresvotingalgo(A):
    count=0
    element=None
    for i in range(len(A)):
        if count==0:
            element=A[i]
            count+=1
    return element

        
