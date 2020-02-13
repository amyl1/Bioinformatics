#!/usr/bin/python
import time
import sys

# YOUR FUNCTIONS GO HERE -------------------------------------

#list to store all generated alignments
alignments=[]
def GenSeq(seq1,seq2,al1,al2):
    x=len(seq1)
    y=len(seq2)
    #checks if both sequences are not empty
    if x!=0 and y!=0:
        #alignment matching the first two bases
        GenSeq(seq1[1:],seq2[1:],al1+seq1[0], al2+seq2[0])
        #alignment matching a gap in seq1 with a base in seq2 
        GenSeq(seq1, seq2[1:],al1+"-", al2+seq2[0])
        #matching a base in seq1 with a gap in seq2
        GenSeq(seq1[1:],seq2,al1+seq1[0], al2+"-")
    #if either of the sequences are empty
    else:
        #make the aligned sequences up to the same length by adding gaps
        if x==0:
            al2+=seq2
            al1+="-"*y
        elif y==0:
            al1+=seq1
            al2+="-"*x
        #adds the aligned strings and their corresponding scores to the list
        alignments.append([al1,al2,GenScore(al1,al2)])
    return alignments

#function which takes in the two aligned sequences and scores them
def GenScore(string1,string2):
    total=0
    for i in range (0,len(string1)):
        if string1[i]=="A" and string2[i]=="A":
            total=total+3
        elif string1[i]=="G" and string2[i]=="G":
            total=total+1
        elif string1[i]=="T" and string2[i]=="T":
            total=total+2
        elif string1[i]=="C" and string2[i]=="C":
            total=total+2
        elif string1[i]=="-" or string2[i]=="-":
            total=total-4
        #if the bases do not match
        else:
            total=total-3
    return total
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
# Call any functions you need here, you can define them above.
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
# The number of alignments you have checked should be stored in a variable called num_alignments.

GenSeq(seq1,seq2,"","")
#sets the best score seen so far to the score of the first alignment
best_score=alignments[0][2]
best_alignment=""
#iterates through list of alignments and compares each score to current best
for i in range (0,len(alignments)):
    current_score = alignments[i][2]
    #if it finds a new best, update best score and store this alignment
    if current_score>=best_score:
        best_score=current_score
        best_alignment=alignments[i]
num_alignments=len(alignments)
#-------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Alignments generated: '+str(num_alignments))
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

