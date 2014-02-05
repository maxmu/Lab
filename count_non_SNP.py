import re
import string
import os

inputfile = open("/home/xiaoyu/protein/all_gene/result/non_LII_with_SNP/Homo.non_LII_with_SNP", "r")
pattern = re.compile(">(\S+)@non_LII_with_SNP:(\S+),#")
total_SNP_in_non_LII = 0
for line in inputfile:
    line = string.strip(line)
    match = pattern.match(line)
    if match != None:
        SNP = match.group(2)
        SNP_raw_array = SNP.split(",#")
        for element in SNP_raw_array:
            array = element.split(",")
            print len(array)
            total_SNP_in_non_LII += len(array) - 1
print total_SNP_in_non_LII
