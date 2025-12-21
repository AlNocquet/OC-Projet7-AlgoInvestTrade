# AlgoInvest & Trade


### Context
-------
AlgoInvest & Trade aims to improve its short-term investment decision tools in order to
maximize client profits after two years of investment.

As a junior developer working with AlgoInvest & Trade, I have been asked to design an
algorithm capable of suggesting the most profitable combination of stocks to buy, while
respecting strict business constraints.
Each stock can be purchased only once, no fractional shares are allowed, and the total
investment budget must not exceed 500 €.

My program reads a file containing stock data (name, price, and expected profit after
two years), explores possible investment strategies, and outputs the portfolio that
maximizes total profit.

After delivering an initial functional solution based on brute force, I was asked to
develop a more efficient optimized version, capable of handling larger datasets and
producing results in less than one second.


### Project Goals
-------------
- Implement a brute-force algorithm that explores all possible combinations
- Implement an optimized algorithm based on the 0/1 Knapsack problem
- Compare performance and efficiency of both approaches
- Validate results on multiple datasets
- Present the algorithmic analysis in a PDF presentation


### Business Constraints
--------------------
- Each stock can be purchased only once
- No fractional shares are allowed
- Maximum investment budget: 500 €
- Profit is expressed as a percentage of the stock price after 2 years


### Project Structure
-----------------
bruteforce.py        : Brute-force solution
optimized.py         : Optimized solution using dynamic programming
datas/               : CSV datasets
tests/               : Parsing and algorithm tests
README.md            : Project documentation (EN)
README_FR.md         : Project documentation (FR)


### Installation
------------

```bash
1. Clone the repository from GitHub:
   git clone https://github.com/AlNocquet/OC-Projet7-AlgoInvestTrade.git

2. Go to the project folder:
   cd OC-Projet7-AlgoInvestTrade

3. Run the brute-force version (small dataset):
   python bruteforce.py datas/20_stocks.csv

4. Run the optimized version (large datasets):
   python optimized.py datas/dataset1_Python+P7.csv
   python optimized.py datas/dataset2_Python+P7.csv
```


### Brute Force Solution
-------------------
The brute-force algorithm tests all possible combinations of stocks that respect
the budget constraint and selects the combination that maximizes profit.
This approach guarantees an optimal result but has exponential time complexity,
making it unsuitable for large datasets.

### Optimized Solution
------------------
The optimized solution uses a dynamic programming approach (0/1 Knapsack).
Instead of testing all combinations, it keeps only the best possible profit
for each budget value up to 500 €.
This approach guarantees an optimal result while remaining efficient.


### Algorithm Complexity
--------------------
Brute force:
- Time complexity: O(2^n)
- Memory usage: Low

Optimized (Knapsack):
- Time complexity: O(n × C), where C is the budget in cents
- Memory usage: Moderate

### Tests
-----
Parsing tests validate CSV loading and data cleaning.
Algorithm tests validate budget constraints and profit correctness.
Tests are separated from display logic.

### Deliverables
------------
- bruteforce.py
- optimized.py
- PDF presentation (20 slides maximum) including:
  - Brute-force analysis
  - Pseudocode / diagram
  - Optimized algorithm and limitations
  - Performance comparison
  - Comparison with Sienna’s investment choices

### Author
------
Alice Nocquet