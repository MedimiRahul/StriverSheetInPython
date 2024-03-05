# * * * 
# * * * 
# * * * 
# print these 

def pattern1(n):
    for i in range(n):
        print('* '*n);

pattern1(3);

# * 
# * * 
# * * * 
# * * * * 
# * * * * *

def pattern2(n):
    for i in range(n):
        print('* '* (i+1));

pattern2(5);

# 1
# 12
# 123
# 1234

# using recursion 


def pattern3(n):
    if n==1:
        x=str(n)
        print(x)
        return x
    a=pattern3(n-1)
    a+=str(n)
    print(a)
    return a

pattern3(4)


# 1
# 22
# 333


def pattern4(n):
    if n==1:
        x=str(n)
        print(x)
        return
    pattern4(n-1)
    for i in range(n):
        print(n, end='')
    print()    

pattern4(3)    


# ****
# ***
# **
# *

def pattern5(n):
    for i in range(n,0,-1):
        print('*'*i);

pattern5(4)



# 54321
# 4321
# 321
# 21
# 1

# by using recursion could not be done

def pattern6(n):
    for i in range(n,0,-1):
        for j in range(i,0,-1):
            print(j,end='')
        print()    
pattern6(5)        



#    *
#   ***
#  *****
# *******


def pattern7(Trows,curr):
    if curr==1:
        x=(Trows*2)-curr-1
        y=x//2
        print(' '*y + '*'*curr + ' '*y)
        return
    pattern7(Trows,curr-2)
    x=(Trows*2)-curr-1
    y=x//2
    print(' '*y + '*'*curr + ' '*y)
    return 

pattern7(4,(4*2-1))
    


# *****
#  ***
#   *

def pattern8(Trows,curr):
    if curr==1:
        x=((Trows*2)-1)-1
        y=x//2
        print(' '*y+'*'+' '*y)
        return 
    a=(Trows*2)-1-curr
    b=a//2
    print(' '*b +'*'*curr +' '*b)
    pattern8(Trows,curr-2)

pattern8(3,(3*2)-1)    


#   *
#  ***
# *****
# *****
#  ***
#   *

def pattern9(Trows):
    pattern7(Trows,(Trows*2)-1)
    pattern8(Trows,(Trows*2)-1)

pattern9(3)    


# *
# **
# ***
# ****
# ***
# **
# *

def pattern10(Trows):
    for i in range(1,Trows+1):
        print("*"*i)
    for i in range(Trows-1,0,-1):
        print('*'*i)

pattern10(4)            


# 1
# 01
# 101

def pattern11(n):
    # Write your solution here.
    if n==1:
        print(1)
        return str(1)
    a=pattern11(n-1)
    if a[0]=='1':
        b='0'+a
    else:
        b='1'+a 
    print(b)
    return b           

pattern11(3)


def pattern12(trows,curr):
    if curr==1:
        print('1'+' '*((trows*2)-2)+'1')
        return '1'
    a=pattern12(trows,curr-1)
    b=a+str(curr)
    c=sorted(b,reverse=True)
    d=''.join(c)
    print(b+' '*((trows*2)-2*(curr))+d)
    return b

pattern12(3,3)


def pattern13(trows,curr):
    
    

