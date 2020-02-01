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
    elif seq1=="-" or seq2=="-":
        score=score-4
    else:
        score=score-3
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
    scorematrix=newmatrix(seq1,seq2)
    dirmatrix=newmatrix(seq1,seq2)
    for r in range (0,len(dirmatrix)):
        for c in range (0,len(dirmatrix[r])):
            if dirmatrix[r][c]==0:
                dirmatrix[r][c]="E"
    for i in range (2,len(scorematrix)):
        for j in range (2,len(scorematrix[i])):
            D=scorematrix[i-1][j-1]+score(scorematrix[i][0],scorematrix[0][j])
            U=scorematrix[i-1][j]-2
            L=scorematrix[i][j-1]-2
            #consider if there are two scores equal
            if D<0 and U<0 and L<0:
                scorematrix[i][j]=0
                dirmatrix[i][j]="E"
            elif D>U and D>L:
                scorematrix[i][j]=D
                dirmatrix[i][j]="D"
            elif U>L:
                scorematrix[i][j]=U
                dirmatrix[i][j]="U"
            else:
                scorematrix[i][j]=L
                dirmatrix[i][j]="L"
    print (scorematrix)
    print (dirmatrix)
    print (scorematrix[-1][-1])
popmatrix("ACGT","AGGT")


