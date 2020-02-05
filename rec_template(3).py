#!/usr/bin/python
import time
import sys

# YOUR FUNCTIONS GO HERE -------------------------------------
def score(string1,string2):
    score=0
    for i in range (0,len(string1)):
        if string1[i]=="A" and string2[i]=="A":
            score=score+3
        elif string1[i]=="C" and string2[i]=="C":
            score=score+2
        elif string1[i]=="G" and string2[i]=="G":
            score=score+1
        elif string1[i]=="T" and string2[i]=="T":
            score=score+2
        elif string1[i]=="-" or string2[i]=="-":
            score=score-4
        else:
            score=score-3
    return score

sequence=[]
def align(al1,al2,seq1,seq2):
    if len(seq1)==0 or len(seq2)==0:
        if len(seq1)==0:
            al1+="-"*len(seq2)
            al2+=seq2
        elif len(seq2)==0:
            al1+=seq1
            al2+=("-"*len(seq1))
        sequence.append([al1,al2])
    else:
        align(al1+seq1[0], al2+seq2[0], seq1[1:],seq2[1:])
        align(al1+seq1[0], al2+"-", seq1[1:],seq2)
        align(al1+"-", al2+seq2[0], seq1, seq2[1:])
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
align("","",seq1,seq2)
best_score=0
best_alignment=""
num_alignments=0
for i in range (0,len(sequence)):
    num_alignments+=1
    string1=sequence[i][0]
    string2=sequence[i][1]
    current_score=score(string1,string2)
    if current_score>best_score:
        best_score=current_score
        best_alignment=sequence[i]


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
