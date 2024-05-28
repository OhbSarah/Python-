'''
Executions des modules
'''


from load_data import *
import statistics
import visualization
import reg
import numpy as np

data= load_and_clean_data("eCO2mix_RTE_Annuel-Definitif_2020.csv")
print(data.head())
print(statistics.summary(data))
visualization.plot_pairs(data) #un peu long enviro 2min pour afficher

#choisir les variables explicatives pour la regression
corr_matrix = statistics.correlation_matrix(data)
co2_correlations = corr_matrix['Taux de Co2'][corr_matrix['Taux de Co2'] > 0.55]
co2_correlations = co2_correlations.drop(labels=['co2'], errors='ignore')
print(f"Corrélations avec 'co2' supérieures à 0.55 :{co2_correlations}")

    
X = data[['Consommation', 'Nucléaire','Charbon','Hydraulique','Gaz','Bioénergies','Fioul']].values
y = data['Taux de Co2'].values
    
#création du modèle
modele_multiple = reg.OrdinaryLeastSquares()
modele_multiple.fit(X, y)
    
#prédiction     
y_pred = modele_multiple.predict(X)

#Afficher les coefficients ainsi que les t-stats et les erreurs standars pour chaque coefficient en dehors de l'Intercepte et enfin le coefficient de determination
modele_multiple._print_results(data[['Consommation', 'Nucléaire','Charbon','Hydraulique','Gaz','Bioénergies','Fioul']], y,y_pred)

resi=y-y_pred

#Visualisation des prediction selon les observations 
modele_multiple.visualiser(X, y)
modele_multiple.visualise_result(X,y) #pour être sur de l'interpretation mais moins lisible

#Vérification des hypothéses sur les résidus
visualization.plot_residuals_vs_fitted(y_pred, resi)
visualization.plot_histogram(resi, title='Histogram des résidus')
visualization.qqplot(resi, distribution='norm', dist_params=(0, 1)) #long à s'afficher environ 3 à 10min

