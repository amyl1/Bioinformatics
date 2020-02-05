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
        

align("","","GAA","GAT")
bestscore=0
bestalignment=""

for i in range (0,len(sequence)):
    string1=sequence[i][0]
    string2=sequence[i][1]
    currentscore=score(string1,string2)
    if currentscore>bestscore:
        bestscore=currentscore
        bestalignment=sequence[i]
print (bestscore)
print (bestalignment)