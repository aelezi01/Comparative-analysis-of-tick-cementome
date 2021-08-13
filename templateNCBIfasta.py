import pandas as pd
import requests
import urllib.request
from pyhere import here

from Bio import Entrez
Entrez.email = 'areda.elezi@gmail.com'

dataset = pd.read_csv(here('data', 'Uniprot', 'ScapularisNCBI.csv'), skiprows=[0], header=None, index_col=False)
outFile = here('data', 'fasta', 'Ixodes_scapularis.fasta')
print(len(dataset))

obsolete = []
row = 0

for i in dataset.itertuples():
    ## retrieve the sequences using Uniprot IDs from the Uniprot website
    uniprotID = dataset.iloc(axis=0)[row, 0]
    row = row + 1\
    
    try:
        with Entrez.efetch(db='protein',id=uniprotID, rettype = 'fasta') as handle:

            ## read the content from the Entrez database
            seq = handle.read()

            ## open and write a new fasta file with all the sequences corresponding to the Uniprot IDs stored in the csv file
            with open(outFile, 'a') as ffasta:
                ffasta.write(seq)

            if len(seq) == 0:
                obsolete.append(row)
    except:
        obsolete.append(row)
        pass

print(len(obsolete))