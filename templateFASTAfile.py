import pandas as pd
import requests
import urllib.request

from pyhere import here

dataset = pd.read_csv(here('data', 'ZambeziensisUniprot.csv'), skiprows=[0], header=None, index_col=False)
print(len(dataset))

obsolete = []
row = 0

for i in dataset.itertuples():
    ## retrieve the sequences using Uniprot IDs from the Uniprot website
    uniprotID = dataset.iloc(axis=0)[row, 0]
    url = 'https://www.uniprot.org/uniprot/'+ uniprotID +'.fasta'
    row = row + 1\
    
    try:
        with urllib.request.urlopen(url) as url:

            ## read the content from the url and decode it
            page = url.read()
            seq = page.decode('utf8')

            ## open and write a new fasta file with all the sequences corresponding to the Uniprot IDs stored in the csv file
            with open(here('fasta', 'Rhipicephalus_zambeziensis.fasta'), 'a') as ffasta:
                ffasta.write(seq)

            if len(seq) == 0:
                obsolete.append(row)
    except:
        obsolete.append(row)
        pass

print(len(obsolete))