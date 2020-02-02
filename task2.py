def score(seq1,seq2):
    score=0
    if seq1=="A" and seq2=="A":
        score=score+3
    elif seq1=="C" and seq2=="C":
        score=score+2
    elif seq1=="G" and seq2=="G":
        score=score+1
    elif seq1=="T" and seq2=="T":
        score=score+2
    return score

def newmatrix(seq1,seq2):
    matrix=[]
    height=len(seq1)+2
    width=len(seq2)+2
    for i in range (0,height):
        matrix.append([])
        for j in range (0,width):
            matrix[i].insert(0,"-")
    pos=2
    for base in seq1:
        matrix[0][pos]=base
        matrix[1][pos]=0
        pos=pos+1
    pos=2
    for base in seq2:
        matrix[pos][0]=base
        matrix[pos][1]=0
        pos=pos+1
    matrix[1][1]=0
    return matrix

def popmatrix(seq1,seq2):
    string1=""
    string2=""
    direction=""

    scorematrix=newmatrix(seq1,seq2)
    backtrack=newmatrix(seq1,seq2)

    for r in range (0,len(backtrack)):
        for c in range (0,len(backtrack[r])):
            if backtrack[r][c]==0:
                backtrack[r][c]="E"
    for i in range (2,len(scorematrix)):
        for j in range (2,len(scorematrix[i])):
            D=scorematrix[i-1][j-1]+score(scorematrix[i][0],scorematrix[0][j])
            U=scorematrix[i-1][j]-4
            L=scorematrix[i][j-1]-4
            #consider if there are two scores equal
            if D<0 and U<0 and L<0:
                scorematrix[i][j]=0
                backtrack[i][j]="E"
            elif D>=U and D>L:
                scorematrix[i][j]=D
                backtrack[i][j]="D"
            elif U>L:
                scorematrix[i][j]=U
                backtrack[i][j]="U"
            else:
                scorematrix[i][j]=L
                backtrack[i][j]="L"
    
    bestscore=scorematrix[-1][-1]
    print (scorematrix)
    i=len(backtrack[0])-1
    j=len(backtrack)-1
    while direction != "E":
        print (direction)
        if backtrack[i][j]=="D":
            string1=str(backtrack[0][i])+string1
            string2=str(backtrack[j][0])+string2
            j=j-1
            i=i-1
        elif backtrack[i][j]=="U":
            string1="-"+string1
            string2=str(backtrack[j][0])+string2
            j=j-1
        else:
            string1=str(backtrack[0][i])+string1
            string2="-"+string2
            i=i-1
        direction=backtrack[j][i]
    return (string1,string2)
        
    
#fix error with strings of different length   
print(popmatrix("GATT","GAAT"))


