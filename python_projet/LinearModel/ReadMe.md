Le Package à pour but d'analyser la production electrique francaise. Les donnees proviennent de la societe RTE : elle enregistrent la quantite d'électricité produite pour chaque filiere du mix énergetique durant lannee 2020 et d'expliquer le taux demission de CO2 en fonction decertaines covariables du jeu de donnees par un modéle linéaire.

Le Package est composé de différents Module.

main.py permet d'executer les codes implémenter dans les differents modules.

statistics.py permet de calculer toutes les statistqiues descriptives basiques telque la moyenne, la variance, la correlation, les quantiles...

visualization.py permet des visualiser les résultats avec des fonction qui permette d'afficher des barplot, boxplot, qqplot, scatter, histogramme...

reg.py contient une class permettant de produire une regression linéaire par la méthode des moindre carrés

Lors de l'execution du main on obtient des resultats plutôt satisfaisant du coté du coefficient de determination et des coefficients
La visualisation du nuage de point des predictions en fonction des observations nous montre aussi que nous avons un modele plutôt correcte 
la visualisation du graphique predictions et observation nous confirme cela mais il est moins lisible au vue du nombres de données
Enfin la visualisation des résidus nous montre que même si le modele est satisfaisant on peut encore améliorer cette regression car les résidus ne sont pas Normal.
