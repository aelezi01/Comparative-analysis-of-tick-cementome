import pandas as pd

# open and read the csv file
cement_villar_file = pd.read_csv('../Data_S4-hostSG.csv', skiprows = [0])

# remove rows without Uniprod IDs
# uniprotIDs_list = cement_villar_file.dropna(subset = ['Uniprot  accesion number'])

# store only the Uniprot ID values within a csv file
cement_villar_file.to_csv('Villar_uniprotIDs-hostSG.csv', index=False, columns = ['Uniprot accesion number'])

# the file will be used to find the corresponding gene names on Uniprot