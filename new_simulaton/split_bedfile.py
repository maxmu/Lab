import re
import os

numbers = ['X', 'Y']
for i in range(1,23):
    numbers.append(str(i))

for element in numbers:
    os.system("grep -P \"^chr" + element + "\t\" /home/xiaoyu/down_ftp/eichlerlab.gs.washington.edu/greatape/data/VCFs/SNPs/Callable_regions/Callable_coverage/Intersect_filtered_cov5.bed > chr" + element + ".bed")
