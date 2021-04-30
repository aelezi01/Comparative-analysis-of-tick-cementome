import pandas as pd

# open and read the csv file
cement_villar_file = pd.read_csv('../Data_S4.csv')

# remove rows without Uniprod IDs
uniprotIDs_list = cement_villar_file.dropna(subset = ['Uniprot  accesion number'])

# store only the Uniprot ID values within a csv file
uniprotIDs_list.to_csv('Villar_uniprotIDs.csv', index=False, columns = ['Uniprot  accesion number'])

# the file will be used to find the corresponding gene names on Uniprot