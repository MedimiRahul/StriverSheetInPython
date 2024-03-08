# linear search is o(n) linearly compare each and every element 

def linearsearch(A,num):
    for i in range(len(A)):
        if num==A[i]:
            return i
    return 'not found'    
        
    