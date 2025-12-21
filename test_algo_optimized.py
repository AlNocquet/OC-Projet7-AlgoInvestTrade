from optimized import get_stocks_from_csv, get_best_investment

CSV_PATH = "datas/dataset1_Python+P7.csv"
MAX_BUDGET = 500


if __name__ == "__main__":

    # Chargement des actions
    stocks = get_stocks_from_csv(CSV_PATH)
    assert len(stocks) > 0, "Aucune action chargée depuis le CSV"

    # Calcul du meilleur portefeuille
    portfolio = get_best_investment(stocks)
    assert portfolio is not None, "Aucun portefeuille retourné"
    assert len(portfolio) > 0, "Portefeuille vide"

    # Vérifications des contraintes
    total_cost = sum(stock[1] for stock in portfolio)
    total_profit = sum(stock[2] for stock in portfolio)

    assert total_cost <= MAX_BUDGET, "Budget maximal dépassé"
    assert total_profit >= 0, "Profit négatif"

    print("test_algo_optimized OK")