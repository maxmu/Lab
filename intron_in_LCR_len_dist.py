import re
import string
specie = "Pongo_pygmaeus"
inputfile = open("/home/xiaoyu/protein/all_gene/result/" + specie + ".withintronSNP", "r")
outputfile = open("/home/xiaoyu/protein/all_gene/result2/" + specie + "SNP_in_intron_dist", "w")
pattern = re.compile("(.*)@intron_that_break_lcr:(\S+)#@Snp_in_intron_break_lcr:(\S*)")

gene_count = 0
intron_count = 0
SNP_count = 0

for line in inputfile:
    info_for_intron = {}
    line = string.strip(line)
    match = pattern.match(line)
    if match != None:
        intron_string = match.group(2)
        SNP_string = match.group(3)

        intron_raw_array = intron_string.split("#")
        intron_array = []
        for element in intron_raw_array:
            intron_array.append(element.split(","))
        
        for element in intron_array:
            info_for_intron[(element[2], element[3])] = 0
        
        if SNP_string != "":
            SNP_string = SNP_string[:len(SNP_string) - 1]
            SNP_raw_array = SNP_string.split("#")
            SNP_array = []
            for element in SNP_raw_array:
                SNP_array.append(element.split(","))
            for element in SNP_array:
                info_for_intron[(element[3], element[4])] += 1
            
        for key in info_for_intron.keys():
            length = int(key[1]) - int(key[0]) + 1
            density = float(info_for_intron[key]) / float(length)
            outputfile.write(str(length) + " " + str(info_for_intron[key]) + " " + str(density) + "\n")

            intron_count += 1
            SNP_count += info_for_intron[key]
print intron_count
print SNP_count
