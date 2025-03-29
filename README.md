# AlgoINVEST-TRADE

This program displays the most profitable basket of investments from a given list of stocks.


## Technology

Python


## Author

Alice Nocquet


## Environment setup and program launch

Use the following commands to create a virtual environment, install dependencies, and run the program:

```bash
$ git clone https://github.com/AlNocquet/OC-Projet7-AlgoInvestTrade.git
$ cd OC-Projet7-AlgoInvestTrade
$ python3 -m venv venv           # On Windows: python -m venv venv
$ source venv/bin/activate       # On Windows: venv\Scripts\activate
$ pip install -r requirements.txt
```


## USAGE

Activate the virtual environment, then run the desired command below:


### ▶️ To run `bruteforce.py`:

```bash
$ python bruteforce.py
```

This script processes a CSV file containing 20 stock offers:

- It calculates all possible combinations under the following conditions:
  - A stock can only be purchased once
  - All unique combinations (A,B ≠ B,A)

- It displays the most profitable combination of actions that **does not exceed €500 total investment**


### 🚀 To run `optimized.py`:

```bash
$ python optimized.py file "Path to the CSV file to analyze (e.g. data\\dataset1.csv)"
```

This script processes a user-specified CSV file (e.g., 1000 stock offers):

- Cleans out invalid data (investment cost ≤ 0€)
- Sorts actions by performance and selects them until reaching a total investment **as close as possible to €500**
- Displays the following output:
  - Total initial investment (in €)
  - Total profit after 2 years (in €)
  - Resale value of the basket after 2 years (in €)
