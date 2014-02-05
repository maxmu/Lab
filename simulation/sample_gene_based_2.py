import re
import string
import os
import random

#Save all the LCRs in one big array:
#    key: genename
#  value:[array_of_LCR_positions, chromosome]

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
                LCR.append(array[0])
            LCR_dict[gene_name] = [LCR, chromosome]
    inputfile.close()
    return LCR_dict

#Sample from the LCR dictionary in the format of(position, codon, chromosome, gene_name)
def sample_LCR_pos(gene_name_array, LCR_dict, size):
    result = []
    for i in range(size):
        name = random.choice(gene_name_array)

        length = len(LCR_dict[name][0])
        amino_length = length / 3
        rand = random.randint(0, amino_length - 1)

        position1 = LCR_dict[name][0][rand * 3]
        position2 = LCR_dict[name][0][rand * 3 + 1]
        position3 = LCR_dict[name][0][rand * 3 + 2]

        result.append([position1, str(1), LCR_dict[name][1], name])
        result.append([position2, str(2), LCR_dict[name][1], name])
        result.append([position3, str(3), LCR_dict[name][1], name])

    return result

#Save all the cdexons positions in one big array:
#now I change the format of saving all the big codon in the format of:
#    key : [gene_name]
#  value : [array_of_LCR_positions, chromosome]
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
                    all_pos.append(str(i))
                    cnt += 1
            all_cde_pos_dict[gene_name] = [all_pos, chromosome]
    inputfile.close()
    return all_cde_pos_dict

#Save all the cdexons position in one big array(non_dict)
def sample_non_LCR_pos(gene_name_array, LCR_dict, non_dict, size):
    result = []
    while len(result) < 3 * size:
        name = random.choice(gene_name_array)
        position_array = non_dict[name][0]
        chromosome = non_dict[name][1]

        length = len(non_dict[name][0])
        amino_length = length / 3
        rand = random.randint(0, amino_length - 1)

        position1 = non_dict[name][0][rand * 3]

        if position1 in LCR_dict[name][0]:
            continue
        else:
            position2 = non_dict[name][0][rand * 3 + 1]
            position3 = non_dict[name][0][rand * 3 + 2]
            result.append([position1, str(1), chromosome, name])
            result.append([position2, str(2), chromosome, name])
            result.append([position3, str(3), chromosome, name])
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
#input size here:~
for i in range(1001):
    file = directory + str(i) + ".simulation_gene_based"
    outputfile = open(file, "w")

    lcr_sample = sample_LCR_pos(gene_name_array, LCR, 5000)
    non_lcr_sample = sample_non_LCR_pos(gene_name_array, LCR, ALL, 5000)

    outputfile.write("LCR_positions:")

    for element in lcr_sample:
        outputfile.write(element[0] + "," + element[1] + "," + element[2] + "," + element[3] + "#")
    outputfile.write("\n")


    outputfile.write("non_LCR_positions:")

    for element in non_lcr_sample:
        outputfile.write(element[0] + "," + element[1] + "," + element[2] + "," + element[3] + "#")
    outputfile.write("\n")
    outputfile.close()
