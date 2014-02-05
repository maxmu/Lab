import re
import string

#Return one tuple (LCR, non_LCR)
def read_simulation_gene(directory):
    inputfile = open(directory, "r")
    pattern_lcr = re.compile("LCR_positions:(\S+)#")
    pattern_non = re.compile("non_LCR_positions:(\S+)#")

    for line in inputfile:
        line = string.strip(line)
        match1 = pattern_lcr.match(line)
        match2 = pattern_non.match(line)

        if match1 != None:
            LCR_dict = {}
            position_string = match1.group(1)
            position_raw_array = position_string.split("#")
            for element in position_raw_array:
                array = element.split(",")
                if array[2] in LCR_dict.keys():
                    LCR_dict[array[2]].append(array)
                else:
                    LCR_dict[array[2]] = []
                    LCR_dict[array[2]].append(array)

        if match2 != None:
            non_dict = {}
            position_string = match2.group(1)
            position_raw_array = position_string.split("#")
            for element in position_raw_array:
                array = element.split(",")
                if array[2] in non_dict.keys():
                    non_dict[array[2]].append(array)
                else:
                    non_dict[array[2]] = []
                    non_dict[array[2]].append(array)
    inputfile.close()
    return (LCR_dict, non_dict)

def whole_file(chr_num):
    result_sequence = ""
    input_file = open("/home/xiaoyu/hg19/chromosomes/chr" + str(chr_num) + ".fa", "r")
    for line in input_file:
        if line.startswith(">"):
            continue
        else:
            line = string.strip(line)
            result_sequence += line
    input_file.close()
    return result_sequence


#use dict tuple to extract information.
def extract(dict_tuple):
    LCR_dict = dict_tuple[0]
    non_dict = dict_tuple[1]

    for key in LCR_dict.keys():
        sequence = whole_file(key)
        for element in LCR_dict[key]:
            element.append(sequence[int(element[0])].upper())
        print key
    for key in non_dict.keys():
        sequence = whole_file(key)
        for element in non_dict[key]:
            element.append(sequence[int(element[0])].upper())
        print key
    return (LCR_dict, non_dict)

dict_tuple = read_simulation_gene("/home/xiaoyu/protein/all_gene/result/simulation_gene_based/10.simulation_gene_based")
print dict_tuple[0]["11"]
"""
directory = "/home/xiaoyu/protein/all_gene/result/simulation_gene_based_processed"
for count in range(1000):
    inputfile = "/home/xiaoyu/protein/all_gene/result/simulation_gene_based/" + str(count) + ".simulation_gene_based"
    outputfile_absolute_name = "/home/xiaoyu/protein/all_gene/result/simulation_gene_based_processed/" + str(count) + ".simulation_gene_based_processed"
    dict_tuple = read_simulation_gene(inputfile)
    new_dict_tuple = extract(dict_tuple)
    print count

    outputfile = open(outputfile_absolute_name, "w")
"""  







