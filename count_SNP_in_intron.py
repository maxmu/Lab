import re
import string

specie = "Pongo_pygmaeus"

inputfile = open("/home/xiaoyu/protein/all_gene/result/" + specie + ".withintronSNP", "r")
#This is for calculate intron number
pattern_calculate_intron = re.compile(">GeneInformation:(.*)@intron_that_break_lcr:(\S+)#@Snp_in_intron_break_lcr:(\S*)")
#This is for count the SNPs in introns that can break a LCR
pattern_count_SNP_in_intron = re.compile(">GeneInformation:(.*)@intron_that_break_lcr:(\S+)#@Snp_in_intron_break_lcr:(\S*)#")

Genes_have_intron = 0
intron_cnt = 0
total_length_intron = 0
SNP_count = 0
for line in inputfile:
    line = string.strip(line)
#Here, we need to change the pattern for different usage
    match = pattern_count_SNP_in_intron.match(line)
    if match != None:


#1
#For these lines, I just use them to get how many SNPs in introns that
#can break the LCR and calculate the SNP density in them
"""
SNP_in_intron = match.group(3)
        SNP_array = SNP_in_intron.split("#")
        SNP_count += len(SNP_array)
        #print SNP_array
"""
#print "We get " + str(SNP_count) + "SNPs in introns that can break the LCR"


#2
#For these lines, I just use it to calculate how many genes that have intron
#that can break them. Beside, I can also find how many intron there are that
#can break the LCR regions
"""
        Genes_have_intron += 1
        intron_string = match.group(2)
        intron_array = intron_string.split("#")
        intron_cnt += len(intron_array)
        
        intron_length_in_gene = 0
        for intron in intron_array:
            array = intron.split(",")
            begin = int(array[2])
            end = int(array[3])
            length = end - begin + 1
            intron_length_in_gene += length
        total_length_intron += intron_length_in_gene

"""        
#print "we have " + str(Genes_have_intron) + "genes that have intron that ca break them."
#print "the number of all the introns that break the LCRs is: " + str(intron_cnt)
#print "we have " + str(total_length_intron) + " bp introns"



