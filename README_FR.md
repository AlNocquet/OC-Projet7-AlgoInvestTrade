# AlgoInvest & Trade


### Contexte
--------
AlgoInvest & Trade souhaite améliorer ses outils d’aide à la décision afin de rendre ses
programmes d’investissement à court terme plus performants et de maximiser le profit
réalisé par ses clients après deux ans d’investissement.

En tant que développeur junior travaillant avec AlgoInvest & Trade, il m’a été demandé
de concevoir un algorithme capable de suggérer la meilleure combinaison d’actions à
acheter, dans le respect de contraintes métier strictes.
Chaque action ne peut être achetée qu’une seule fois, aucune fraction d’action n’est
autorisée, et le budget total ne doit pas dépasser 500 €.

Mon programme lit un fichier contenant les informations sur les actions (nom, coût et
bénéfice après deux ans), explore différentes stratégies d’investissement et affiche
le portefeuille maximisant le profit total.

Après avoir livré une première solution fonctionnelle basée sur la force brute, j’ai
ensuite développé une version optimisée, capable de traiter des volumes de données plus
importants et de fournir un résultat en moins d’une seconde.


### Objectifs du projet
-------------------
- Implémenter une solution brute force testant toutes les combinaisons possibles
- Implémenter une solution optimisée basée sur le problème du sac à dos (0/1 Knapsack)
- Comparer les performances des deux approches
- Valider les résultats sur plusieurs jeux de données
- Présenter l’analyse algorithmique dans un document PDF


### Contraintes métier
------------------
- Une action ne peut être achetée qu’une seule fois
- Aucune fraction d’action n’est autorisée
- Budget maximum : 500 €
- Le bénéfice est exprimé en pourcentage du coût de l’action après 2 ans


### Structure du projet
-------------------
bruteforce.py        : Solution brute force
optimized.py         : Solution optimisée (programmation dynamique)
datas/               : Jeux de données CSV
tests/               : Tests de parsing et tests algorithmiques
README.md            : Documentation du projet (EN)
README_FR.md         : Documentation du projet (FR)


### Installation
------------

```bash
1. Cloner le dépôt depuis GitHub :
  git clone https://github.com/AlNocquet/OC-Projet7-AlgoInvestTrade.git

2. Se placer dans le dossier du projet :
  cd OC-Projet7-AlgoInvestTrade

3. Lancer la version brute force (small dataset):
  python bruteforce.py datas/20_stocks.csv

4. Lancer la version optimisée (large datasets):
  python optimized.py datas/dataset1_Python+P7.csv
  python optimized.py datas/dataset2_Python+P7.csv
```


### Solution brute force
--------------------
L’algorithme brute force teste toutes les combinaisons possibles d’actions
respectant la contrainte de budget, puis sélectionne celle maximisant le profit.
Cette méthode garantit un résultat optimal mais possède une complexité exponentielle,
ce qui la rend inutilisable sur de grands jeux de données.


### Solution optimisée
------------------
La solution optimisée repose sur la programmation dynamique et le problème du sac à dos.
Elle conserve, pour chaque budget possible jusqu’à 500 €, le meilleur profit atteignable.
Cette approche garantit un résultat optimal tout en restant performante.


### Complexité des algorithmes
--------------------------
Brute force :
- Complexité temporelle : O(2^n)
- Utilisation mémoire : Faible

Optimisé (sac à dos) :
- Complexité temporelle : O(n × C), où C est le budget en centimes
- Utilisation mémoire : Modérée


### Tests
-----
Les tests de parsing vérifient la lecture et le nettoyage des données CSV.
Les tests algorithmiques vérifient le respect du budget et la validité du profit.
Les tests sont séparés de la logique d’affichage.


### Livrables
---------
- bruteforce.py
- optimized.py
- Présentation PDF (20 diapositives maximum) comprenant :
  - Analyse de la solution brute force
  - Diagramme / pseudocode
  - Algorithme optimisé et limites
  - Comparaison des performances
  - Comparaison avec les choix de Sienna


### Auteur
------
Alice Nocquet