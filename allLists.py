import pandas as pd

## open all datasets

antunesDB = pd.read_csv('Data_Sheet_1_antunes.csv', skiprows=[0], header=None, index_col=False)
tirloniDB = pd.read_csv('TirloniSwissprot2Tick.csv', skiprows=[0], header=None, index_col=False)
cement_villar_file = pd.read_csv('Villar_uniprotIDs.csv', skiprows=[0], header=None, index_col=False)


## save uniprot IDs to lists


## compare lists and save conserved genes (Uniprot IDs present in all lists) into a new list
conserved = []


for i in tirloniDB:
    if i in cement_villar_file:
        conserved.append(i)


print(conserved)
## create csv file with allconserved genes
