import csv
from itertools import combinations


def get_stocks_from_csv(csv_path) -> list:
    """
    Read a CSV and return a list of actions as tuples:
        (name: str, price: float, profit_amount: float)

    Behavior:
    - Parses price and profit as floats (accepts comma as decimal separator).
    - Skips malformed lines with a warning.
    - Skips actions with price <= 0 with a warning.
    - Raises FileNotFoundError if the file is not found.

    Args:
        csv_path (str): Path to the CSV file.

    Returns:
        list: List of tuples (name, price, profit_amount). May be empty.
    """

    stocks = []

    try:
        with open(csv_path, newline="", encoding="utf-8") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=",")
            for line_number, row_dict in enumerate(reader, start=2):
                # tolerant name lookup (several possible header names)
                name = row_dict.get('name') or row_dict.get('Name') or row_dict.get('nom') \
                       or row_dict.get('title') or row_dict.get('action')

                try:
                    # handle comma decimal and surrounding spaces
                    price_text = (row_dict.get('price') or '').replace(',', '.').strip()
                    profit_text = (row_dict.get('profit') or '').replace(',', '.').strip()

                    # row_dict.get('price') or '': retrieve the string for the price column, or '' if it is missing
                    # .replace(',', '.') : replace a comma with a period to accept decimals written like 12,5
                    # .strip() : remove extra spaces at the beginning/end

                    # convert to numbers
                    price = float(price_text)
                    profit_pct = float(profit_text)

                except (KeyError, ValueError, TypeError):
                    print(f"[WARN] line {line_number} ignored (invalid format): {row_dict}")
                    continue

                if price <= 0:
                    print(f"[WARN] action ignored (price <= 0): {name} (price={price})")
                    continue

                profit_amount = price * (profit_pct / 100.0)
                # keep tuple structure (name, price, profit) for compatibility
                stocks.append((str(name), float(price), float(profit_amount)))

    except FileNotFoundError:
        print(f"[ERROR] file not found: {csv_path}")
        raise

    return stocks


def iter_combinations(stocks):
    """
    Generate all non-empty combinations of the given stock list.

    Behavior:
    - Produces combinations of size 1 up to len(stocks), in increasing size order.
    - Uses itertools.combinations to avoid duplicates and permutations
      (i.e. (A, B) is generated once, and (B, A) is never produced).
    - Yields each combination lazily as a tuple instead of building a full list
      in memory.
    - If `stocks` is empty, yields nothing.

    Args:
        stocks (sequence): Sequence of items (for example tuples
            (name, price, profit_amount)).

    Returns:
        generator: A generator that yields tuples representing each possible
            non-empty combination of items from `stocks`.
    """

    # count how many stock items are available (used to know the maximum combination size)
    num_stocks = len(stocks)
    
    # loop over desired combination sizes: 1, then 2, ..., up to all items
    # (this ensures we produce ('A',) ('B',) ('C',) before ('A','B'), etc.)
    for combo_size in range(1, num_stocks + 1):

        # for the current combo_size, generate each tuple of that length from `stocks`
        for combo in combinations(stocks, combo_size):

            # yield hands this combination to the caller and pauses until the caller requests the next one
            yield combo


def get_best_investment_bruteforce(stocks, max_cost=500.0):
    """
    Evaluate all combinations with a brute-force search and return the best one.

    Behavior:
    - Iterates over every non-empty combination of `stocks` using iter_combinations().
    - For each combination, computes:
        * total_cost  = sum of prices
        * total_profit = sum of profit_amount values
    - Discards any combination whose total_cost exceeds `max_cost`.
    - Keeps track of the combination with the highest total_profit.
    - Returns a dictionary describing the best portfolio found, or None
      if no valid combination respects the budget.

    Args:
        stocks (sequence): Sequence of items (tuples (name, price, profit_amount)).
        max_cost (float, optional): Maximum total cost allowed for the portfolio.
            Defaults to 500.0.

    Returns:
        dict | None: A dictionary of the form:
            {
                "stocks": combo_tuple,
                "total_cost": float,
                "total_profit": float
            }
            or None if no valid combination is found under the budget.
    """

    best = None
    for combo in iter_combinations(stocks):
        total_cost = sum(item[1] for item in combo)
        if total_cost > max_cost:
            continue
        total_profit = sum(item[2] for item in combo)
        if best is None or total_profit > best['total_profit']:
            best = {'stocks': combo, 'total_cost': total_cost, 'total_profit': total_profit}

    return best


def display_best_investment(best):
    """
    Print a human-readable summary of the best brute-force portfolio.

    Behavior:
    - If `best` is None, prints a message indicating that no valid
      combination respects the budget and returns immediately.
    - Otherwise:
        * prints each selected stock (name, price, profit_amount),
        * prints the total cost of the portfolio,
        * prints the total profit after 2 years,
        * prints the total resale value (cost + profit).

    Args:
        best (dict | None): Result returned by get_best_investment_bruteforce().
            Expected format:
            {
                "stocks": tuple_of_stocks,
                "total_cost": float,
                "total_profit": float
            }

    Returns:
        None
    """

    if best is None:
        print("Aucune combinaison ne respecte la contrainte de budget.")
        return

    # datas recovery
    combo = best['stocks']
    total_cost = best['total_cost']
    total_profit = best['total_profit']
    total_value = total_cost + total_profit

    print("\nMeilleure combinaison d'actions trouvée :\n")

    # Display each action one by one
    for stock in combo:
        name = stock[0]
        price = stock[1]
        profit = stock[2]
        print("- Action :", name, "| coût :", price, "€ | profit :", profit, "€")

    print("\nRécapitulatif :")
    print("Coût total du portefeuille :", total_cost, "€")
    print("Profit total après 2 ans   :", total_profit, "€")
    print("Valeur de revente totale   :", total_value, "€")


def main():
    """
    Entry point for the brute-force script.

    Behavior:
    - Defines the relative CSV path (datas/20_stocks.csv).
    - Calls get_stocks_from_csv() to parse the input file and build the
      list of stocks.
    - Prints a short summary of the parsed data (number of actions and
      the first 10 entries for visual inspection).
    - Runs the brute-force search via get_best_investment_bruteforce()
      with a maximum budget of 500€.
    - Calls display_best_investment() to print the optimal portfolio and
      its aggregated metrics.

    Args:
        None

    Returns:
        None
    """

    csv_path = "datas/20_stocks.csv"

    try:
        stocks = get_stocks_from_csv(csv_path)

    except FileNotFoundError:
        print("[ERREUR] Fichier introuvable :", csv_path)
        return

    except Exception as e:
        print("[ERREUR] Problème pendant la lecture du fichier :", e)
        return

    print("\nNombre d'actions lues :", len(stocks))

    print("Voici les premières actions :\n")

    for i, s in enumerate(stocks[:10], start=1):
        name = s[0]
        price = s[1]
        profit = s[2]
        print(i, ":", "name =", name, ", price =", price, "€ , profit =", profit, "€")

    best = get_best_investment_bruteforce(stocks, max_cost=500.0)

    display_best_investment(best)

    print("\n--- Fin du programme bruteforce ---\n")