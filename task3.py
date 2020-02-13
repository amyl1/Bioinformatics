import sys
def NJ(filename):
    matrix=[]
    opened= open(filename, 'r')
    r=0
    #reads in file line by line until end of file
    while True:
        line = opened.readline()
        if not line:
            break
        #removes line breaks
        row=line.rstrip('\n')
        matrix.append(row.split(" "))
        if matrix[0][0]=='-':
            matrix[0].remove('-')
        if r>0:
            #converts each numerical character into a float
            for char in range (1,len(matrix[r])):
                matrix[r][char]=float(matrix[r][char])
        #counts number of rows
        r+=1
    
    while len(matrix)>2:
        matrix[0].append("sum")
        Qmatrix=[]
        print("matrix:")
        #calculate row total
        for row in range (1,len(matrix)):
            total=0
            for col in range (1,len(matrix[row])):
                total+=matrix[row][col]
            matrix[row].append(total)
        #print matrix row by row
        for i in range (0,len(matrix)):
            print(matrix[i])
        Qmatrix.append(matrix[0][:-1])
        for row in range (1,len(matrix)):
            #list containing q scores to be inserted
            insert=[]
            y=len(Qmatrix[0])
            for col in range (1,y+1):
                if matrix[row][col]==0:
                    insert.append(0)
                else:
                    r=len(matrix)
                    dis_ab=matrix[row][col]
                    sum_a=matrix[row][-1]
                    sum_b=matrix[col][-1]
                    Q=((r-2)*dis_ab)-float(sum_a)-float(sum_b)
                    insert.append(Q)
            Qmatrix.append(insert)
        smallestQ=0
        #finds smallest q score and stores its position
        for Qrow in range(1,len(Qmatrix)-1):
            for Qcol in range(0,len(Qmatrix[Qrow])):
                if smallestQ>=Qmatrix[Qrow][Qcol]:
                    smallestQ=Qmatrix[Qrow][Qcol]
                    smallestpos=[Qrow-1,Qcol]
        print("Qmatrix:")
        for i in range (0,len(Qmatrix)):
            print(Qmatrix[i])
        #names new species
        newspecies=str(matrix[0][smallestpos[0]])+str(matrix[0][smallestpos[1]])
        newdist=[newspecies]
        #calculates new distances
        for col in range(1,len(matrix[0])):
            dist_ac=matrix[smallestpos[0]+1][col]
            dist_bc=matrix[smallestpos[1]+1][col]
            dist_ab=matrix[smallestpos[0]+1][smallestpos[1]+1]
            distance=(dist_ac+dist_bc-dist_ab)/2
            if distance!=0:
                newdist.append(distance)
        if len(matrix)==3:
            break
        x=0
        #deletes rows and columns of species and inserts new species
        for row in range (0,len(matrix)):
            if row>0:
                x=1
            del matrix[row][-1]
            del matrix[row][smallestpos[0]+x]
            del matrix[row][smallestpos[1]+x]
        del matrix[smallestpos[0]+1]
        del matrix[smallestpos[1]+1]
        matrix[0].insert(smallestpos[0]-1,newdist[0])
        for row in range (1,len(matrix)):
            matrix[row].insert(smallestpos[0],newdist[row])
        newdist.insert(smallestpos[0],0)
        matrix.insert(smallestpos[0],newdist)  

#reads in file from command line
filename = (sys.argv[1])
NJ(filename)