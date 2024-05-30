
# AlgoINVEST-TRADE :

Ce programme permet d'afficher le meilleur panier d'investissements parmi une liste d'actions donnée.

## Technologie :

Python

## Author :

Alice Nocquet


## Installation de l'environnement et lancement du programme :

Utiliser les commandes suivantes pour créer un environnement, installer les requirements et lancer le programme :

```bash
$ git clone https://github.com/AlNocquet/OC-Projet7-AlgoInvestTrade.git
$ cd OC-Projet7-AlgoInvestTrade
$ python3 -m venv venv (Sous Windows => python -m venv venv)
$ source venv/bin/activate (Sous Windows => venv\Scripts\activate)
$ pip install -r requirements.txt
```

## UTILISATION :

    Activez l'environnement ;


    Lancez les commandes suivantes :


        Pour lancer le fichier bruteforce.py :

            $ python bruteforce.py


            Le fichier bruteforce.py traite un fichier csv de 20 actions : 

                > Le programme calcule l'ensemble des combinaisons possibles avec les conditions suivantes : 
                    - Achat unique d'une action ;
                    - Toutes les combinaisons uniques possibles (A,B exclut combinaison B,A).
            
                > Affiche une nouvelle liste d'actions par meilleures rentabilités en ne dépassant pas un investissement total de 500 €.



        Pour lancer le fichier optimized.py :

            $ python optimized.py file "Nom du ficher à analyser (avec chemin éventuel). ex : data\\dataset1.csv"


            Le fichier optimized.py traite un fichier csv indiqué dans le terminal (ici 2 fichiers fournis de 1000 actions): 

                > Le programme nettoie la base de données des données non pertinentes (Coût investissement avec valeur négative ou égale à 0€)
                
                > Trie les actions par performance ;
                
                > Achète ces actions jusqu'à un investissement total au plus proche ou égal à 500 € ;
            
                > Affiche les données suivantes :
                    - Investissement de départ (coût total) en Euros ;
                    - Profit total du panier d'actions après 2 ans en Euros ;
                    - Valeur de rachat du panier d'actions après 2 ans en Euros.
