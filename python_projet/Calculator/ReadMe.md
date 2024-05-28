Package permettant de calculer l'emprunte carbonne annuelle

Il est composé de trois modules :

calculator.py: composé des fonctions suivantes:
    -get_numeric_input
    -get_text_input
    -calculate : Retourne l'empreinte carbone selon les différentes sous categories et selon les grandes categories
    -visualize_emissions : Retourne un barplot qui affiche l'empreinte carbone selon les grandes categories

data.py qui permet de lire et traiter les données

main.py qui permet d'executer les 2 autres modules aifn d'obtenir l'empreinte carbone de l'utilisateur 
On va d'abord lire les données puis demander à l'utilisateur d'entrer des informations de consommations et enfin calculer.
Une fois le calcule effectuer grâce a la fonction calculate() de calculator, main affichera un barplot avec les consommation annuelles selon des catégories