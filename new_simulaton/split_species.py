import csv

reader = csv.reader(open("/home/xiaoyu/protein/SNP/Pan_paniscus/Pan_paniscus.remove.csv"), delimiter = "\t")

writer_gbg = csv.writer(open("/home/xiaoyu/protein/SNP/Gorilla.gbg.remove.vcf", 'w'), delimiter = "\t")
writer_ggd = csv.writer(open("/home/xiaoyu/protein/SNP/Gorilla.ggd.remove.vcf", 'w'), delimiter = "\t")
writer_ggg = csv.writer(open("/home/xiaoyu/protein/SNP/Gorilla.ggg.remove.vcf", 'w'), delimiter = "\t")

writer_gbg.writerow(['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'Gorilla_beringei_graueri-9732_Mkubwa', 'Gorilla_beringei_graueri-A929_Kaisi', 'Gorilla_beringei_graueri-Victoria'])
writer_ggd.writerow(['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'Gorilla_gorilla_dielhi-B646_Nyango'])
writer_ggg.writerow(['CHROM', 'POS', 'ID', 'REF', 'ALT', 'QUAL', 'FILTER', 'INFO', 'FORMAT', 'Gorilla_gorilla_gorilla-9749_Kowali', 'Gorilla_gorilla_gorilla-9750_Azizi', 'Gorilla_gorilla_gorilla-9751_Bulera', 'Gorilla_gorilla_gorilla-9752_Suzie', 'Gorilla_gorilla_gorilla-9753_Kokomo', 'Gorilla_gorilla_gorilla-A930_Sandra', 'Gorilla_gorilla_gorilla-A931_Banjo', 'Gorilla_gorilla_gorilla-A932_Mimi', 'Gorilla_gorilla_gorilla-A933_Dian', 'Gorilla_gorilla_gorilla-A934_Delphi', 'Gorilla_gorilla_gorilla-A936_Coco', 'Gorilla_gorilla_gorilla-A937_Kolo', 'Gorilla_gorilla_gorilla-A962_Amani', 'Gorilla_gorilla_gorilla-B642_Akiba_Beri', 'Gorilla_gorilla_gorilla-B643_Choomba', 'Gorilla_gorilla_gorilla-B644_Paki', 'Gorilla_gorilla_gorilla-B647_Anthal', 'Gorilla_gorilla_gorilla-B650_Katie', 'Gorilla_gorilla_gorilla-KB3782_Vila', 'Gorilla_gorilla_gorilla-KB3784_Dolly', 'Gorilla_gorilla_gorilla-KB4986_Katie', 'Gorilla_gorilla_gorilla-KB5792_Carolyn', 'Gorilla_gorilla_gorilla-KB5852_Helen', 'Gorilla_gorilla_gorilla-KB6039_Oko', 'Gorilla_gorilla_gorilla-KB7973_Porta', 'Gorilla_gorilla_gorilla-X00108_Abe', 'Gorilla_gorilla_gorilla-X00109_Tzambo'])

for position in reader:
    gbg = position[0:9] + position[9:12]
    ggd = position[0:9] + [position[12]]
    ggg = position[0:9] + position[13:]

    writer_gbg.writerow(gbg)
    writer_ggd.writerow(ggd)
    writer_ggg.writerow(ggg)

