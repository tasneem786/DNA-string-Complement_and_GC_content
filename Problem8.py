dna = input ("Enter ")
C=G=0
for i in dna :
    if i =="G":
        G+=1
    if i == "C":
        C+=1
GC_percent = (G+C)*100/len(dna)
print ( GC_percent)
