import pandas as pd
import requests
import urllib.request


## open and read the csv files
#cement_villar_file = pd.read_csv('Villar_uniprotIDs.csv', skiprows=[0], header=None, index_col=False )
sialome_villar_file = pd.read_csv('Villar_uniprotIDs-tickSG.csv')
#hostSG_villar_file = pd.read_csv('Villar_uniprotIDs-hostSG.csv')
#hostCem_villar_file = pd.read_csv('Villar_uniprotIDs-hostCement.csv')

obsolete = []
row = 0

for i in sialome_villar_file.itertuples():
    ## retrieve the sequences using Uniprot IDs from the Uniprot website
    uniprotID = sialome_villar_file.iloc(axis=0)[row, 0]
    url = 'https://www.uniprot.org/uniprot/'+ uniprotID +'.fasta'
    row = row + 1
    
    try:
        with urllib.request.urlopen(url) as url:

            ## read the content from the url and decode it
            page = url.read()
            seq = page.decode('utf8')

            ## open and write a new fasta file with all the sequences corresponding to the Uniprot IDs stored in the csv file
            with open('VillarDBtickSG.fasta', 'a') as VillarDBhostCement:
                VillarDBhostCement.write(seq)

            if len(seq) == 0:
                obsolete.append(row)
    except:
        obsolete.append(row)
        pass

print(len(obsolete))