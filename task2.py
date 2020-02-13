#!/usr/bin/python
import time
import sys

#function to score how two characters are matched
def score(seq1,seq2):
    score=0
    if seq1=="A" and seq2=="A":
        score=3
    elif seq1=="C" and seq2=="C":
        score=2
    elif seq1=="G" and seq2=="G":
        score=1
    elif seq1=="T" and seq2=="T":
        score=2
    else:
        score=-3
    return score

#sets up an empty matrix
def newmatrix(seq1,seq2):
    matrix=[]
    width=len(seq1)+2
    height=len(seq2)+2
    for i in range (0,height):
        matrix.append([])
        for j in range (0,width):
            matrix[i].insert(0,"-")
    pos=2
    for base in seq1:
        #populates row 0 with the bases in sequence 1
        matrix[0][pos]=base
        #initailises row 1 to 0
        matrix[1][pos]=0
        pos=pos+1
    pos=2
    for base in seq2:
        #populates column 0 with the bases in sequence 2
        matrix[pos][0]=base
        #initailises column 1 to 0
        matrix[pos][1]=0
        pos=pos+1
    matrix[1][1]=0
    return matrix

#function to create the score matrix and back tracking matrix.
#Also fills these matrices.
def popmatrix(seq1,seq2):
    string1=""
    string2=""
    direction=""

    scorematrix=newmatrix(seq1,seq2)
    backtrack=newmatrix(seq1,seq2)
    #for each row in the backtracking matrix
    for r in range (0,len(backtrack)):
        #for each column in the backtracking matrix
        for c in range (0,len(backtrack[r])):
            #checks to see if there is a 0 in the score matrix and puts an E in the corresponding entry in the backtracking matrix.
            if scorematrix[r][c]==0:
                backtrack[r][c]="E"
    for i in range (2,len(scorematrix)):
        for j in range (2,len(scorematrix[i])):
            #calculates the potential scores for each direction.
            D=scorematrix[i-1][j-1]+score(scorematrix[i][0],scorematrix[0][j])
            U=scorematrix[i-1][j]-4
            L=scorematrix[i][j-1]-4
            #if all are negative, place a 0 in the score matrix and E in the backtracking matrix.
            if D<0 and U<0 and L<0:
                scorematrix[i][j]=0
                backtrack[i][j]="E"
            #if D is the largest, put corresponding score into the matrix.
            elif D>=U and D>L:
                scorematrix[i][j]=D
                backtrack[i][j]="D"
            #if U is the largest, put corresponding score into the matrix
            elif U>L:
                scorematrix[i][j]=U
                backtrack[i][j]="U"
            #if L is the largest, put corresponding score into the matrix
            else:
                scorematrix[i][j]=L
                backtrack[i][j]="L"
    best_score=0
    bestposition=[]
    #scans the matrix to find the highest score, scores the position 
    for x in range(2,len(scorematrix)):
        for y in range(2,len(scorematrix[x])):
            entry=scorematrix[x][y]
            if entry>best_score:
                best_score=entry
                bestposition=[x,y]
    
    x=bestposition[0]
    y=bestposition[1]
    #backtracks through matrix to generate optimal alignment
    while direction != "E":
        if backtrack[x][y]=="D":
            string1=str(backtrack[0][y])+string1
            string2=str(backtrack[x][0])+string2
            x=x-1
            y=y-1
        elif backtrack[x][y]=="U":
            string1="-"+string1
            string2=str(backtrack[x][0])+string2
            x=x-1
        else:
            string1=str(backtrack[0][y])+string1
            string2="-"+string2
            y=y-1
        direction=backtrack[x][y]
    return (string1,string2,best_score)


# ------------------------------------------------------------



# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# To work with the printing functions below the best local alignment should be called best_alignment and its score should be called best_score. 
returned=popmatrix(seq1,seq2)
best_score=returned[2]
best_alignment=returned[:2]

#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

