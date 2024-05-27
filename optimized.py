
import csv
import argparse
from colorama import Fore, Style, Back


MAX_COST = 500

def get_stocks_from_csv(file) -> list:
    """ Gets a list of stocks from the csv file and excludes irrelevant datas (profits <= 0)"""

    stocks = []

    with open(file, newline="") as csv_File:
        reader = csv.DictReader(csv_File, delimiter=",")
        for row in reader:
            stock = (row['name'], float(row['price']), float(row['profit']))
            if stock[1] > 0 :
                stocks.append(stock)
    #print(len(stocks))
    #print(stocks[:5])
    return stocks


def get_best_investment(stocks: list) -> list:
    """ Sorts stocks by performance and buy up to a total purchase cost of €500 """

    best_investment = []

    total_purchase = 0

    stocks_by_profit = sorted(stocks, reverse=True, key=lambda stocks : stocks[2])
    print(stocks_by_profit[:5])

    while total_purchase < MAX_COST:
        for stock in stocks_by_profit:
            total_cost = 0
            total_profit = 0
            for i in range (len(stock)) :
                total_cost += stock[i][1]
                total_profit += stock[i][2]
                best_investment.append(stock, total_cost, total_profit)

    print(Fore.GREEN + Style.BRIGHT + f"Le meilleur éventail d'investissements est : " + Style.RESET_ALL)
    for b in best_investment[0] :
        print(" "+ f"{b}")
    print(Fore.GREEN + Style.BRIGHT + f"Avec un coût total de : " + Style.RESET_ALL + f"{round(best_investment[1],2)}")
    print(Fore.GREEN + Style.BRIGHT + f"Avec un profit total de : " + Style.RESET_ALL + f"{round(best_investment[2],2)}")

    return(best_investment)


def main():
    stocks = get_stocks_from_csv(file="datas/dataset1_Python+P7.csv")
    get_best_investment(stocks)


if __name__ == '__main__':
    start = main()