import pandas as pd
import requests
from io import StringIO

# open and read the csv files
cement_villar_file = pd.read_csv('Villar_uniprotIDs.csv')
sialome_villar_file = pd.read_csv('Villar_uniprotIDs-tickSG.csv')
hostSG_villar_file = pd.read_csv('Villar_uniprotIDs-hostSG.csv')

# write the protein sequences in a FASTA file 
with open('VillarDBcement.fasta', 'w'):
    for x in 'Uniprot accesion number':
        # retrieve the Uniprot data from this website
        seq = 'https://www.uniprot.org/uniprot/'+ x +'.fasta'
