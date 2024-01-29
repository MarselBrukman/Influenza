import sys
from Bio import pairwise2

x = open(sys.argv[1])
y = open(sys.argv[2],'w')
threshold = float(sys.argv[3])
r = x.read().split('\n')
n = 0
query = r[1]
for i in r:
    if '>' in i:
        name = i
        continue
    elif i != '':
        seq = i
        alignments = pairwise2.align.globalxx(query, seq)
        score = alignments[0][2]
        ln = max(len(query),len(i))
        identity = score/ln
        if identity >= threshold:
            y.write(name+'\n'+i+'\n')
        n+=1
        print(n)
        print(name)
        name = ''
x.close()
y.close()
