from bruteforce import get_stocks_from_csv, get_best_investment_bruteforce

CSV_PATH = "datas/20_stocks.csv"
MAX_BUDGET = 500


if __name__ == "__main__":

    stocks = get_stocks_from_csv(CSV_PATH)
    assert len(stocks) > 0, "Aucune action chargée"

    result = get_best_investment_bruteforce(stocks, MAX_BUDGET)
    assert result is not None, "Aucune combinaison trouvée"

    portfolio = result["stocks"]

    total_cost = sum(stock[1] for stock in portfolio)
    total_profit = sum(stock[2] for stock in portfolio)

    assert total_cost <= MAX_BUDGET, "Budget dépassé"
    assert total_profit >= 0, "Profit négatif"

    names = [stock[0] for stock in portfolio]
    assert len(names) == len(set(names)), "Action utilisée plusieurs fois"

    print("test_algo_bruteforce OK")