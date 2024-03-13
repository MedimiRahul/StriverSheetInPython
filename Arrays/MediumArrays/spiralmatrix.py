
# ^{ { 1, 2, 3, 4 },
# ^{ 5, 6, 7, 8 },
# ^{ 9, 10, 11, 12 },
# ^{ 13, 14, 15, 16 } }

# ^ so we will maintain 4 pointers topleft topright bottomleft bottomright
# ^ the exit condition would be when topleft>topright


def spiralmatrix(mat):
    startrow=0
    endrow=len(mat)-1
    startcol=0
    endcol=len(mat[0])-1
    res=[]
    while startcol<=endcol:
        i=startrow
        j=startcol
        while j<=endcol:
            res.append(mat[startrow][j])
            j+=1
        i+=1    
        while i<endrow:
            res.append(mat[i][endcol])
            i+=1
        j-=1    
        while j>=startcol:
            res.append(mat[endrow][j])
            j-=1
        i-=1    
        while i>startrow:
            res.append(mat[i][startcol])
            i-=1
        startcol+=1
        endcol-=1
        startrow+=1
        endrow-=1
    print(res)         


a=[[1,2,3],[4,5,6],[7,8,9]]
spiralmatrix(a)    








