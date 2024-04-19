



class Action:
    """Creates the Action object. The player instance must contain :
    the name, the cost, the profit after two years. """

    def __init__(
        self,
        name,
        price,
        profit,
    ):
        self.name = name
        self.price = price
        self.profit = profit