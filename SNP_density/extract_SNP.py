import Count
import string
import re
import random

class gene_class:
    def __init__(self, name, chromosome, intron, exon):
        self.name = name
        self.chromosome = chromosome
        self.intron = intron
        self.exon = exon

#This is used to accept an array of gene names to construct the gene
#class to save the name and introns.
def construct_geneclass(gene):
    inputfile = open("/home/xiaoyu/protein/all_gene/after_seg/block_total", "r")
    gene = string.strip(str(gene))
    pattern = re.compile(">(\S+)\|chr:(\S+)\|strand:(\S+)\|Cdsbegin: (\S+)\|Cdsend: (\S+)\|ExonStart:(\S+)\|ExonEnd:(\S+)")

    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            if match.group(1) == gene:
                name = gene
                chromosome = match.group(2)
                cbegin = int(match.group(4))
                cend = int(match.group(5))
                    
                exonstart_string = match.group(6)
                exonend_string = match.group(7)

                exonstart_array = exonstart_string.split(",")
                exonend_array = exonend_string.split(",")
                
                exons_tuple_raw_list = []
                for count in range(len(exonstart_array)):
                    exons_tuple_raw_list.append((int(exonstart_array[count]), int(exonend_array[count])))
                
                exons_tuple_list = []
                for count in range(len(exons_tuple_raw_list)):
                    if exons_tuple_raw_list[count][1] < cbegin:
                        continue
                    elif exons_tuple_raw_list[count][0] > cend:
                        continue
                    elif exons_tuple_raw_list[count][0] < cbegin and exons_tuple_raw_list[count][1] > cbegin:
                        exons_tuple_list.append((cbegin, exons_tuple_raw_list[count][1]))
                    elif exons_tuple_raw_list[count][1] > cend and exons_tuple_raw_list[count][0] < cend:
                        exons_tuple_list.append((exons_tuple_raw_list[count][0], cend))
                    else:
                        exons_tuple_list.append(exons_tuple_raw_list[count])

                introns_tuple_list = []
                begin = 0
                end = 0
                for cnt in range(len(exons_tuple_list) - 1):
                    begin = exons_tuple_list[cnt][1]
                    end = exons_tuple_list[cnt + 1][0] - 1
                    
                    introns_tuple_list.append((begin, end))
    inputfile.close()
    return gene_class(str(gene), chromosome, introns_tuple_list, exons_tuple_list)

def random_pick(size, array):
    result = []
    for i in range(size):
        result.append(random.choice(array))
    return result

#This method could return a dictionary of SNP of specie
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

#gene should be a gene_class
def get_intron_SNP(gene, SNP_dictionary):
    intron_tuples = gene.intron
    SNP_array_of_chromosome = SNP_dictionary[str(gene.chromosome)]
    result = []
    for tuple in intron_tuples:
        for SNP in SNP_array_of_chromosome:
            if int(SNP) > tuple[0] and int(SNP) < tuple[1]:
                result.append(SNP)
    return result

not_LCR = Count.not_own_LCR_genes()
array = random_pick(100, not_LCR)
SNP_dict = get_SNP_dict("Homo")

total_SNP = 0
length = 0
for i in array:
    gene = construct_geneclass(i)
    SNP_in_intron = get_intron_SNP(gene, SNP_dict)

    for intron_tuple in gene.intron:
        length += intron_tuple[1] - intron_tuple[0] + 1

    print len(SNP_in_intron)
    total_SNP += len(SNP_in_intron)

density = float(float(total_SNP) / float(length))
print density
