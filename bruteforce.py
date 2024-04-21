
import csv
from itertools import combinations
from operator import itemgetter


# PSEUDO CODE BRUTEFORCE

# DEBUT 

    # VARIABLE EXTRAIRE 20 ACTIONS DANS CSV
    # VARIABLE CALCULER TOUTES LES COMBINAISONS POSSIBLES
    # VARIABLE COUT TOTAL et PROFIT DE CHAQUE COMBINAISON (CONDITION < 500 €)
    # VARIABLE TRI DECROISSANT DES MEILLEURES PERFORMANCES

# FIN



def set_stocks_from_csv() -> list:
    """Sets a list of stocks from the csv file "20_stocks.csv" """

    # DEBUT

    stocks = []
    with open("datas/20_stocks.csv", newline="") as csv_File:
        reader = csv.DictReader(csv_File, delimiter=",")
    # Sélectionner le fichier CSV et le parcourir
        for row in reader:
            stock = (str(row['name']), int(row['price']), ((int(row['profit']) * 0.01) * int(row['price'])))
        # POUR chaque ligne du fichier CSV, définir une action comme suit :
            # name : "chaîne de caractère" <- row 0 ;
            # cost : INT (ENTIER) <- row 1 ;
            # Profit : INT (ENTIER / PERCENT) <- row 2 (Convertir % en Int avec le prix row[1]) ;
            stocks.append(stock)
            # Ajouter à la liste d'actions
    #print(stocks)
    return stocks

    # FIN


def get_all_combinations(stocks : list) -> list :
    """ Returns all combinations possibles of stocks (20 puissance 20)"""

    # DEBUT

    all_combinations = []
    # Créer une liste de toutes les combinaisons possibles d'actions
    for i in range(len(stocks)) :
        all_combi = combinations(stocks, i) #puissance 20
    # Pour chaque action de la liste "stocks" de 1 à 20, la combiner avec les autres (puissance 20 - (valeur non combinée avec elle-même + doublon géré par "combination"))
        for combination in all_combi :
            all_combinations.append(combination)
        # Pour chaque combinaison, l'ajouter à la liste all_combinations 
    #print(len(all_combinations))
    #print(all_combinations)
    return all_combinations
        
    # FIN


def valid_investments(all_combinations : list) -> list:
    """ Gets a list of investment proposals with a basket cost < or = €500 """

    # DEBUT

    valid_proposals = []

    max_investment = 500

    for combination in all_combinations:
        combination_cost = 0
        combination_profit = 0
        for i in range (len(combination)) :
            combination_cost += combination[i][1]
            combination_profit += combination[i][2]
    # POUR chaque combinaison d'actions de la liste des combinaisons possibles, initialiser à 0 le coût et le profit
        # PUIS additioner le coût et le profit des actions de chaque combinaison avec leurs index ["price"], ["profit"]

        if combination_cost <= max_investment :
        # SI le coût de la combinaison d'actions est inférieur ou égale à 500€
            valid_proposals.append((combination, combination_cost, combination_profit))
            #print(len(valid_proposals))
            #print(valid_proposals)
            # Ajouter la combinaison à la liste des propositions


def best_investments(valid_proposals : list) -> list:
    """ Returns a ranking of the best proposals of investment """

    best_investments = valid_proposals

    sorted_best_investments = sorted(best_investments, reverse=False, key=itemgetter(['price']))
    print(sorted_best_investments)
    return sorted_best_investments

    # Trier la liste en décroissant
    # Print la liste avec : Noms actions, coût total et rendement total. A FAIRE


if __name__ == '__main__':
    start = best_investments(valid_investments(get_all_combinations(set_stocks_from_csv())))

