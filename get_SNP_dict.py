import re
import string

def get_SNP_dict(specie):
    inputfile = open("/home/xiaoyu/protein/SNP/" + specie + ".vcf", "r")
    pattern = re.compile("chr(\S+)(\s+)(\S+)(\s+)\.")
    SNP = {}
    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            chromosome = match.group(1)
            position = match.group(3)
            if chromosome in SNP.keys():
                SNP[chromosome].append(position)
            else:
                SNP[chromosome] = []
                SNP[chromosome].append(position)
    inputfile.close()
    return SNP
