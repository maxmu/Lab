import re
import string
import os
import random

def get_LCR():
    LCR_dict = {}
    inputfile = open("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP", "r")
    pattern = re.compile(">GeneInformation:(.*)@GeneName:(\S+)@Chromosome:(\S+)@Strand:(\S+)@LCRpos:(\S+)#@LCR_SNP:")
    for line in inputfile:
        LCR = []
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            gene_name = match.group(2)
            chromosome = match.group(3)
            LCRpos_string = match.group(5)
            LCRpos_raw_array = LCRpos_string.split("#")
            for i in LCRpos_raw_array:
                array = i.split(",")
                LCR.append([array[0], chromosome, array[2], gene_name])
            LCR_dict[gene_name] = LCR
    inputfile.close()
    return LCR_dict

def sample_LCR_pos(gene_name_array, LCR_dict, size):
    result = []
    for i in range(size):
        name = random.choice(gene_name_array)
        position = random.choice(LCR_dict[name])
        result.append(position)
    return result

#Save all the cdexons positions in one big array:
def get_All_cde_pos():
    all_cde_pos_dict = {}
    inputfile = open("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP", "r")
    pattern = re.compile(">GeneInformation:(.*)@GeneName:(\S+)@Chromosome:(\S+)@Strand:(\S+)@CDExons:(\S+)#@LCRpos:(\S+)#@LCR_SNP:")
    for line in inputfile:
        cnt = 0
        all_pos = []
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            gene_name = match.group(2)
            chromosome = match.group(3)
            all_pos_string = match.group(5)
            all_pos_raw_array = all_pos_string.split("#")
            for i in all_pos_raw_array:
                array = i.split("~")
                begin = int(array[0])
                end = int(array[1])
                exon_pos = range(begin, end)
                for i in exon_pos:
                    all_pos.append([str(i), chromosome, str(cnt % 3 + 1)])
                    cnt += 1
            all_cde_pos_dict[gene_name] = all_pos
    inputfile.close()
    return all_cde_pos_dict

#Save all the cdexons position in one big array(non_dict)
def sample_non_LCR_pos(gene_name_array, LCR_dict, non_dict, size):
    result = []
    while len(result) < size:
        name = random.choice(gene_name_array)
        position_array = non_dict[name]
        position_raw = random.choice(position_array)
        position = position_raw.append(name)
        if position in LCR_dict[name]:
            continue
        else:
            result.append(position)
    return result
directory = "/home/xiaoyu/protein/all_gene/result/simulation_gene_based/"
gene_inputfile = open("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP", "r")
pattern = re.compile(">GeneInformation:(.*)@GeneName:(\S+)@Chromosome:(\S+)@Strand:(\S+)@CDExons:(\S+)#@LCRpos:(\S+)#@LCR_SNP:(\S+)")

#This array saves all of the gene name for pick
gene_name_array = []

for line in gene_inputfile:
    line = string.strip(line)
    match = pattern.match(line)
    if match != None:
        gene_name_array.append(match.group(2))
gene_inputfile.close()

LCR = get_LCR()
ALL = get_All_cde_pos()

print sample_LCR_pos(gene_name_array, LCR, 10)
print sample_non_LCR_pos(gene_name_array, LCR, ALL, 10)
