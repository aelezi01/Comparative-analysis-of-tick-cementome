import pandas as pd

# open and read the csv file
cement_villar_file = pd.read_csv('../Data_S4.csv')

# create a list with the Uniprod IDs
uniprotIDs_list = pd.Series(list(cement_villar_file['Uniprot  accesion number']))
uniprotIDs_list.dropna()
print(uniprotIDs_list)

# store the list in a csv file
#uniprotIDs_list.to_csv('Villar_uniprotIDs.csv', index=False)

# the file will be used to find the corresponding gene names on Uniprot