import re
#read the origin fasta file
import os
os.chdir(c/Users/Dell/Desktop/Practical8/IBI1_2021-22)
file = open ("Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa")
#the result is to create a new file cut_genes.fa
result = open("cut_genes.fa""w")
DNA = file.read()
DNA = "". join(DNA.split("/n"))
DNA = DNA.lstrip(">")
genes = re.split(r">",DNA)
output = " "
#output the name, length and genes that contain the specific sequence
for i in range (len(genes)):
    if re.search(r"GAATTC",genes[i]):
        name = str(re.findall(r"gene:(.+?)s",genes[i]))
        name = name.strip("['']")
        a = str(re.findall(r"](.+)",genes[i]))
        a = a.strip("['']")
        b = len(a)
        output = output+">"+name+"     "+str(b)+"/n"+"+a+"+"/n"
    result.write(output)
    file.close()
    result.close()