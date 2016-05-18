# Hapster
Assembles haplotypes from short read sequencing data (See data generated by datagen for formatting input). This program employs a fairly simple algorithm since it assumes no sequencing errors and that every position has been sequenced at least twice. After assembling the haplotype, Hapster will offer to check the output with the true haplotype sequences if available (It will automatically open output_haplotypes.txt if output.txt was used for sequencing data)

datagen produces 2 complementary haplotype sequences of a given length as well as simulated sequencing data for this haplotype. 

Instructions for use:
1. Run as "python datagen.py n output" in terminal
  -"n" = the number of SNPs
  -"output" = name of output file for generated data (.txt will be concatenated automatically"
2. When completed, "output.txt" will contain the sequencing data and "output_haplotypes.txt" will contain the haplotype sequences. 

Number of reads per SNP is normally distributed with mean of 15, standard dev of 4, and minimum of 1. Length of each read is normally distributed with mean of 4, standard dev of 2, and minimum of 2. These values are somewhat arbitrary and can be changed within datagen.py. However, the minimum values are the least that is required for Hapster to successfully assemble the haplotype. 
