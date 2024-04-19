
import csv


def set_stocks_from_csv() -> list:
    """Sets a list of stocks from the csv file "20_stocks.csv" """

    # DEBUT

    stocks = []
    with open("datas/20_stocks.csv", newline="") as csv_File:
        reader = csv.DictReader(csv_File, delimiter=",")
        for row in reader:
            stock = (str(row['name']), float(row['price']), float(row['profit']))
        ## POUR chaque ligne du fichier, données comme suit :
            ### name : "chaîne de caractère" <- row 0
            ### cost : FLOAT (DECIMAL) <- row 1
            ### Profit : FLOAT (DECIMAL) <- row 2
            stocks.append(stock)
            ## Ajouter à la liste d'actions
    print(stocks)
    return stocks

    # FIN










if __name__ == '__main__':
    start = set_stocks_from_csv()