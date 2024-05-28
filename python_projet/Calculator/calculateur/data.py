''' 
Lire les diffrents fichier et enrichi la base de données basecarbone_sample.csv à partir de basecarbone-v17-fr.csv
'''

import pandas as pd 

def load_and_clean_data():
    '''
    Lire et mettre en forme les données necessaire pour le calculateur
    '''
    base_sample = pd.read_csv('basecarbone_sample.csv',sep=';')
    base_full = pd.read_csv('basecarbone-v17-fr.csv',sep=',')

    filtered_data =pd.concat([base_full[base_full['Nom base français']== "Bus"], base_full[base_full['Nom base français']== "Bovin viande" ]])
    common_columns = ['Identifiant de l\'élément', 'Nom base français', 'Unité français', 'Total poste non décomposé', 'Nom attribut français']
    filtered_data_common = filtered_data[common_columns]
    base_sample_enriched = pd.concat([base_sample, filtered_data_common])
    base_sample = base_sample_enriched
    return base_sample
    