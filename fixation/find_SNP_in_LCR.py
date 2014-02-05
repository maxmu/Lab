import re
import string

species = ["Homo", "Gorilla", "Pan_paniscus", "Pan_troglodytes", "Pongo_abelii", "Pongo_pygmaeus"]
pattern = re.compile(">(.*)@Chromosome:(\S+)@Strand:(\S+)@LCRpos:(\S+)#")

for specie in species:

    inputfile2 = open("/home/xiaoyu/protein/SNP/" + specie + "_SNP_in_LCR_new", "r")
    pattern2 = re.compile("(\d+)#(\d+)")
    SNP = {}
    for line in inputfile2:
        line = string.strip(line)
        match2 = pattern2.match(line)
        if match2 != None:
            chromosome = str(match2.group(1))
            position = str(match2.group(2))
            if chromosome in SNP.keys():
                SNP[chromosome].append(position)
            else:
                SNP[chromosome] = []
                SNP[chromosome].append(position)
    count = 0
    inputfile2.close()
    inputfile = open("/home/xiaoyu/protein/all_gene/after_seg/LCR_information_file_new", "r") 
    outputfile = open("")
    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            chromosome = match.group(2)
            LCR_pos_string = match.group(4)
            LCR_pos_raw_array = LCR_pos_string.split("#")
            LCR_pos_array = []
            for position in LCR_pos_raw_array:
                array = position.split(",")
                LCR_pos_array.append(array)
            SNP_in_LCR = []
            for element in LCR_pos_array:
                if element[0] in SNP[chromosome]:
                    SNP_in_LCR.append(element)
            count += 1
            print specie + str(count)
            print SNP_in_LCR
    inputfile.close()

