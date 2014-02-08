import csv
import re
import string

def simplify_SNP_file(directory):
    pattern = re.compile("chr(\S+)(\s+)(\S+)(\s+)\.(\s+)(\S+)(\s+)(\S+)(\s+)(\S+)(\s+)PASS(\s+)AC=(\S+)(\s+)(\S+)(\s+)(.*)")
    inputfile = open(directory, "r")
    outputfile = open(directory + ".simp", "w")

    for line in inputfile:
        line = string.strip(line)
        match = pattern.match(line)
        if match != None:
            chromosome = match.group(1)
            position = match.group(3)
            ref = match.group(6)
            alt = match.group(8)
            individuals_string = match.group(17)
            individuals_raw_array = individuals_string.split("\t")

            individuals_array = []
            for element in individuals_raw_array:
                if element == "./.":
                    array = element.split("/")
                    for i in array:
                        individuals_array.append(i)
                else:
                    array = element.split(":")
                    array2 = array[0].split("/")
                    for i in array2:
                        individuals_array.append(i)
            genotype_array = []
            for element in individuals_array:
                if element == "0":
                    genotype_array.append(ref)
                elif element == "1":
                    genotype_array.append(alt)
                elif element == ".":
                    genotype_array.append(element)

            outputfile.write("chr" + chromosome + "\t" + position + "\t" + ref + "\t" + alt + "\t")
            for element in genotype_array:
                outputfile.write(element + "\t")
            outputfile.write("\n")

    inputfile.close()
    outputfile.close()

species = ["Pongo_abelii", "Pongo_pygmaeus"]
array = range(1, 23)
array += ["X", "Y"]
for specie in species:
    for cnt in array:
        directory = "/home/xiaoyu/down_ftp/eichlerlab.gs.washington.edu/greatape/data/VCFs/SNPs/" + specie + "/" + specie + ".vcf." + str(cnt) + ".cov5"
        simplify_SNP_file(directory)

