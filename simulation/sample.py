import os
import re
import string
import random


#For the function of construct, we pass one directory into this fun
#and then extract one big array of LCR array that contain all the LCR
#positions. format : position, chromosome, codon
def construct_LCR(directory):
    all_LCR = []
    inputfile = open(directory, "r")
    pattern = re.compile(">GeneInformation:(.*)@Chromosome:(\S+)@Strand:(.*)#@LCRpos:(\S+)#@LCR_SNP:")
    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            LCRs_string = match.group(4)
            chromosome = match.group(2)

            LCRs_raw_array = LCRs_string.split("#")            
            for LCR in LCRs_raw_array:
                position = []
                array = LCR.split(",")
                position.append(str(array[0]))
                position.append(str(chromosome))
                position.append(str(array[2]))
                all_LCR.append(position)
    return all_LCR

#For this function, we can construct one big array with all the exons
#saved in it.        
def construct_non_LCR(directory):
    all_non_LCR = []
    inputfile = open(directory, "r")
    pattern = re.compile(">GeneInformation:(.*)@Chromosome:(\S+)@Strand:(.*)@CDExons:(\S+)#@LCRpos:(.*)")
    line_cnt = 1
    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            chromosome = match.group(2)
            CDExons = match.group(4)
            
            CDExons_raw_array = CDExons.split("#")
            cnt = 0
            for cdexon in CDExons_raw_array:
                array = cdexon.split("~")
                begin = int(array[0])
                end = int(array[1])
                for i in range(begin, end):
                    position = []
                    position.append(str(i))
                    position.append(str(chromosome))
                    position.append(str(cnt % 3 + 1))
                    cnt += 1
                    all_non_LCR.append(position)
    return all_non_LCR

#This array is used to exclude all the LCR positions in coding regions
#raw_array stores all the positions in coding regions
#remove_array stores all the positions in LCR
def exclude(raw_array, remove_array):
    result = []
    for i in raw_array:
        if i in remove_array:
            continue
        else:
            print i
            result.append(i)
    return result

#This function is used to randomly pick a size of positions from array
def randomly_pick(array, size):
    result = []
    for cnt in range(size):
        result.append(random.choice(array))
    return result


#This is for test of the code:
LCR = construct_LCR("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP") 
exon = construct_non_LCR("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP")

non_LCR_result = exclude(exon, LCR)
print non_LCR_result

simulation_count = 1
for cnt in range(1, 1001):
    print simulation_count
    simulation_count += 1

    directory = "/home/xiaoyu/protein/all_gene/result/simulation/"
    file = directory + str(cnt) + ".simulation"
    outputfile = open(file, "w")

    LCR_result = randomly_pick(LCR, 5000)
    non_LCR_result = randomly_pick(non_LCR, 5000)
    
    outputfile.write("LCR:")
    for pos in LCR_result:
        outputfile.write(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + "#")

    outputfile.write("\n")

    outputfile.write("non_LCR:")
    for pos in non_LCR_result:
        outputfile.write(str(pos[0]) + "," + str(pos[1]) + "," + str(pos[2]) + "#")

    outputfile.close()

