
# ^ longest consequtive sequence [3,8,5,7,6]  in this case would be 5,6,7,8 .. 
# ^ so the brute force method would be for each element check its next digit .
# ^ like for 3 check if 4 if there or not . if there then check for 5 with count increment to 2.
# ^ if not then go for next element . so here we are lineraly checking .

def linearsearch(A,e):
    for i in range(len(A)):
        if A[i]==e:
            return True
    return False    


def longest1(A):
    maxi=-9999999
    for i in range(len(A)):
        count=1
        x=linearsearch(A,A[i]+count)
        while x:
            count+=1
            x=linearsearch(A,A[i]+count)  
        if count>maxi:
            maxi=count
    return maxi        

print(longest1([100,200,1,2,4,3,5,7]))


# ^ so its complexity would be o(n^2) [1,1,2,2,3,4,5,7,100,200]

# ^ another method would be sort the array.
# ^ then same check for min so far 


def longest2(A):
    A.sort()
    mini=-99999999999
    currcount=0
    maxi=0
    for i in range(len(A)):
        if mini==A[i]-1:
            currcount+=1
            mini=A[i]
            if currcount>maxi:
                maxi=currcount
        elif mini==A[i]:
            pass        
        else:
            mini=A[i]
            currcount=1   
            if currcount>maxi:
                maxi=currcount
    return maxi

print(longest2([100,200,1,2,4,3,5,7]))


# ^ optimal solution would be lets save their single occurances either passing it in set 
# ^ then the logic would be we would be searching the occurances only if it is starting point.
# ^ means its element-1 would not be present . 

def linearsearch(A,e):
    for i in A:
        if i==e:
            return True
    return False
    

def longest3(A):
    b=set()
    maxi=0
    for i in A:
        b.add(i)
    for i in b:
        x=i
        Check=False
        for j in b:
            if j==x-1:
                Check=True
        if not Check:
            currcount=1
            y=linearsearch(b,i+currcount)
            while y:
                currcount+=1
                if currcount>maxi:
                    maxi=currcount 
                y=linearsearch(b,i+currcount) 
        else:
            pass
    return maxi

print(longest3([100,200,1,2,4,3,5,7]))    





                

                
                     









