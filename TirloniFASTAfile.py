import pandas as pd
import requests
import urllib.request

#tirloniDB = pd.read_csv('TirloniSwissprot1.csv')
#tirloniDB = pd.read_csv('TirloniSwissprot2Tick.csv')
tirloniDB = pd.read_csv('TirloniSwissprot2HostContaminat.csv')
print(len(tirloniDB))

obsolete = []
row = 0

for i in tirloniDB.itertuples():
    ## retrieve the sequences using Uniprot IDs from the Uniprot website
    uniprotID = tirloniDB.iloc(axis=0)[row, 0]
    url = 'https://www.uniprot.org/uniprot/'+ uniprotID +'.fasta'
    row = row + 1
    
    try:
        with urllib.request.urlopen(url) as url:

            ## read the content from the url and decode it
            page = url.read()
            seq = page.decode('utf8')

            ## open and write a new fasta file with all the sequences corresponding to the Uniprot IDs stored in the csv file
            with open('TirloniDB1.fasta', 'a') as tirloniDB:
                VillarDBhostCement.write(seq)

            if len(seq) == 0:
                obsolete.append(row)
    except:
        obsolete.append(row)
        pass