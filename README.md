# Comparative analysis of tick cementome composition
Comparison of tick cementome composition was performed by comparing published sialome and cementome datasets of a variety of species. <br>
Due to the fact that the datasets analysed were originated from various published research, there is a wide range of differences and uneveness in the data.
To create some consistency across the numerous datasets, only proteins with an existing Uniprot ID were included in the data analysis process.

## Uniprot IDs to FASTA files
A template script was written to search for fasta files matching each Uniprot ID stored within an input file. <br>
Once a sequence for each protein was identified, this would be appended to a new fasta file, which would then be used in Orthofinder.

## Contribution
All scripts and data wrangling was written and executed by Areda Elezi. <br>
_QMUL MSc Bioinformatics 2020/21_
