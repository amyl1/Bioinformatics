def score(alignment):
    score=0
    if alignment[0]=="A" and alignment[1]=="A":
        score=score+3
    elif alignment[0]=="C" and alignment[1]=="C":
        score=score+2
    elif alignment[0]=="G" and alignment[1]=="G":
        score=score+1
    elif alignment[0]=="T" and alignment[1]=="T":
        score=score+2
    elif alignment[0]=="-" or alignment[1]=="-":
        score=score-3
    else:
        score=score-4
    return score
def align(seq1,seq2):
    alignment=[]
    if len(seq1)==1 and len(seq2)==1:
        alignment.append(seq1)
        alignment.append(seq2)
        return score(alignment)
    else:
        return align(seq1[-1],seq2[-1])+align(seq1[:-1],seq2[:-1])
print(align("AGTC","CGTC"))
