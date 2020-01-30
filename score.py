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
def align(seq1,seq2):
    if len(seq1)==0:
        seq1="-"*len(seq2)
    elif len(seq2)==0:
        seq2=("-"*len(seq1))
    elif len(seq1)==1 and len(seq2)==1:
        return score (seq1,seq2)
    else:
        match_score=score(seq1[-1],seq2[-1])+align(seq1[:-1],seq2[:-1])
        blank1_score=score("-",seq2[-1])+align(seq1,seq2[:-1])
        blank2_score=score(seq1[-1],"-")+align(seq1[:-1],seq2)
        if match_score>blank1_score and match_score>blank2_score:
            return match_score
        elif blank1_score>blank2_score:
            return blank1_score
        else:
            return blank2_score
    return score(seq1,seq2)
print(align("GAATT","GATTC"))
