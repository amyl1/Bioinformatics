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
print (newmatrix("AC","AG"))