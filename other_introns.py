import re
import string

specie = "Homo"
inputfile = open("/home/xiaoyu/protein/all_gene/result/" + specie + ".withintronSNP", "r")
pattern = re.compile(">(.*)@CDExons:(\S+)#@LCRpos:(.*)@intron_that_break_lcr(\S*)@Snp_in_intron_break_lcr:")

for line in inputfile:
    line = string.strip(line)
    match = pattern.match(line)
    if match != None:
        print match.group(2)
