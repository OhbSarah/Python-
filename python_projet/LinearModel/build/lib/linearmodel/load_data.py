'''
    Lire un fihier csv et le nettoyer
'''

import pandas as pd

def load_and_clean_data(filepath):
    """
    Charge les données à partir d'un fichier CSV, nettoie 
    en remplaçant les lignes contenant des valeurs NaN par 0 et en convertissant les colonnes de temps en format datetime.

    Arguments:
        filepath : Chemin complet vers le fichier CSV à charger.

    Retourne:
        pd.DataFrame: Un DataFrame pandas nettoyé.
    """
    data = pd.read_csv(filepath, delimiter=';')       
    data.fillna(0,inplace=True)
    data['Heures'] = pd.to_datetime(data['Heures'], format='%H:%M').dt.time
    return data
