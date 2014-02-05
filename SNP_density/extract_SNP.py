import Count
import string
import re

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


gene = construct_geneclass("uc001acx.1")
print gene.intron
        
