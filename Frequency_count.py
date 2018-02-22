import csv
import operator
import collections as c

freq={}

filein=open( "input.txt", "r")
text=filein.read()
filein.close()

list=text.lower().replace('.',' ') 
data = list.split() 

for word in data:
    freq[word]=0
    for iword in data:
        if word==iword:
            freq[word]+=1

op = c.OrderedDict(sorted(freq.items(), key=lambda t: t[1],reverse=True))   
 
fileout = open( "output.csv", "w",newline='')
writer = csv.writer
header=("Keyword","Frequency")
writer.writerow(header)
writer.writerows(op.items())
fileout.close()