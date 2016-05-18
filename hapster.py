#Assuming no sequencing errors and each position has been sequenced with at least length 2
reads = raw_input("Reads File Name: ")
matrix = open(reads, 'r')
output = raw_input("Output File Name: ")
h0, h1, pos = "1", "0", 0
for read in matrix:
    if (pos == (len(read) - 2)):
        break
    if (read[pos] == '-' or read[pos+1] == '-'):
        continue
    if (read[pos] == h0[pos]):
        h0 += (read[pos+1])
        h1 += (str(1-int(read[pos+1])))
    else:
        h1 += (read[pos+1])
        h0 += (str(1-int(read[pos+1])))
    pos += 1
haplotypes = open(output, 'r+')
haplotypes.write(h0 + '\n' + h1 + '\n')
if (raw_input("Check results? y/n: ") == 'y'):
    correct = open(reads[:-4]+"_haplotypes.txt", 'r').readline()[:-1]
    if correct == h0 or correct == h1:
        print "CORRECT"
    else:
        print "WRONG"