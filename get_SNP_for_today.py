import get_SNP_dict

specie = "Pongo_abelii"
outputfile = open("/home/xiaoyu/protein/all_gene/result/all_SNP_dict/" + specie + ".allSNP", "w")
dict = get_SNP_dict.get_SNP_dict(specie)

for key in dict.keys():
    string = str(key) + ":"
    for element in dict[key]:
        string += str(element) + ","
    outputfile.write(string + "\n")

outputfile.close()



