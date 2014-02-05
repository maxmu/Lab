import csv

reader = csv.reader(open("/home/xiaoyu/protein/SNP/Homo.vcf"), delimiter = "\t")
for position in reader:
    print position
