import re
import string
import get_SNP_dict


class gene_with_non_LII:
    def __init__(self, name, chromosome, non_LII_list):
        self.name = name
        self.chromosome = chromosome
        self.non_LII_list = non_LII_list

    def __str__(self):
        return ">Genename:" + str(self.name) + "@chromosome" + str(self.chromosome) + "@non_LII_list" + str(self.non_LII_list)

def get_non_LII(directory):
    gene_list = []
    inputfile = open(directory, "r")
    pattern = re.compile(">(.*)@GeneName:(\S+)@Chromosome:(\S+)@Strand:(.*)@CDExons:(\S+)#@LCRpos:(\S+)@intron_that_break_lcr:(\S*)@Snp_in_intron_break_lcr:(\S*)")

    exons = {}

    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            all_non_LII = []
            name = match.group(2)
            chromosome = match.group(3)
            gene = gene_with_non_LII(name, chromosome, all_non_LII)

            cdexons_string = match.group(5)
            cdexons_raw_array = cdexons_string.split("#")
            cdexons_array = []
            for exon in cdexons_raw_array:
                exon_array = exon.split("~")
                cdexons_array.append((int(exon_array[0]), int(exon_array[1])))

            #Here, we need to decide whether the gene have the intron that do not interrupt
            #the LCR regions, firstly, if the array length is 1, that means that we only
            #have one exon, that means we do not have intron in there.

            introns = []
            if len(cdexons_array) == 1:
                continue
            else:
                for i in range(len(cdexons_array)):
                    if i < (len(cdexons_array) - 1):
                        begin = cdexons_array[i][1]
                        end = cdexons_array[i + 1][0] - 1
                        introns.append((begin, end))
                    else:
                        break
            #Get all the introns, need to exclude the introns that are not introns that can break the LCR
            #Need to fix this area: And the thing I need to do is to extend it in this if/else to fix things instead of using "continue"
            
            LII_string = match.group(7)
            if LII_string == "":
                gene.non_LII_list = introns
                

            else:
                LII_string = LII_string[:len(LII_string) - 1]

                LII_raw_array = LII_string.split("#")
                LII_array = []
                for element in LII_raw_array:
                    array = element.split(",")
                    LII_array.append((int(array[2]), int(array[3])))
                
            
                non_LII = []
                for i in introns:
                    if i in LII_array:
                        continue
                    else:
                        non_LII.append(i)
                gene.non_LII_list = non_LII
            gene_list.append(gene)
    inputfile.close()
    return gene_list

gene_list = get_non_LII("/home/xiaoyu/protein/all_gene/result/Homo.withintronSNP")

species = ["Pongo_pygmaeus"]

for specie in species:
    SNP_dict = get_SNP_dict.get_SNP_dict(specie)
    outputfile = open("/home/xiaoyu/protein/all_gene/result/non_LII_with_SNP/" + specie + ".non_LII_with_SNP", "w")

    gene_count = 1
    for gene in gene_list:
        print specie + str(gene_count)
        gene_count += 1
        outputfile.write(">" + gene.name + "@non_LII_with_SNP:")
        SNPs_array = SNP_dict[str(gene.chromosome)]
        for intron in gene.non_LII_list:
            SNP_count = 0
            begin = int(intron[0])
            end = int(intron[1])
            length = end - begin + 1
            outputfile.write(str(begin) + "~" + str(end) + ",")
            for SNP in SNPs_array:
                SNP_int = int(SNP)
                if SNP_int >= begin and SNP_int < end:
                    outputfile.write(SNP + ",")
            outputfile.write("#")
        outputfile.write("\n")
    outputfile.close()






 
