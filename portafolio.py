# These can be Enum too in python 3.4, but overkill
ACTION_BUY = "Buy"
ACTION_SELL = "Sell"
ACTION_KEEP = "Keep"

class Stock: 
    """
    A Stock class with its ticker, shares, and the current price
    """
    def __init__(self, ticker, shares, price):
        self.ticker = ticker
        self.shares = shares
        self.price = price

    def current_price(self):
        """
        Returns the last available price of the Stock
        """
        return self.price

    def value(self):
        """
        Returns the value of the Stock
        """
        return self.shares * self.current_price()
    
class Portafolio:
    """
    Portafolio with stocks and allocated stocks
    """
    def __init__(self, stocks, allocated_stocks):
        """
        stocks: list[Stocks]
        allocated_stocks: dict[str, number] e.g: {"META": 0.4, "APPL": 0.6}
        """
        self.stocks = stocks
        self.allocated_stocks = allocated_stocks

    def total_value(self):
        """
        Return the total value of the Portafolio
        """
        total = 0
        for stock in self.stocks:
            total += stock.value()
        return total

    def __str__(self):
        """String representation of the portfolio"""

        portafolio_str = ""
        portafolio_str += "="*40 + "\n"
        portafolio_str += f"Portafolio - Total value: {self.total_value():.2f}\n"
        portafolio_str += "="*40 + "\n"

        for stock in self.stocks:
            percentage = (stock.value() / self.total_value()) * 100
            portafolio_str+= f"{stock.ticker}: {stock.shares} shares - price: {stock.price:.2f} = {stock.value():.2f} ({percentage:.0f}%)\n"
        return portafolio_str

    def rebalance(self):  
        """
        Returns which stocks should be sold and which ones should be bought to have a balanced Portafolio based on allocated stocks
        """
        rebalance_stocks = []
        total_value = self.total_value()

        for stock in self.stocks:
            target_percentage = self.allocated_stocks[stock.ticker]
            target_value = target_percentage * total_value
            target_shares = target_value / stock.current_price()

            # build, sell or keep depending on the difference
            shares_difference = target_shares - stock.shares
            stock_action = {"ticker": stock.ticker, "shares": abs(shares_difference)}
            if shares_difference > 0: 
                stock_action["action"] = ACTION_BUY
            elif shares_difference < 0:
                stock_action["action"] = ACTION_SELL
            else:
                stock_action["action"] = ACTION_KEEP
            rebalance_stocks.append(stock_action)
        return rebalance_stocks

    def print_rebalance_actions(self):
        """
        Helper method to print the actions required to balance the Portafolio
        """
        allocated_stocks_str = " ".join([f"{k} {v*100:.0f}%" for k, v in self.allocated_stocks.items()])
        print(f"To make your portafolio: {allocated_stocks_str}")
        rebalance_stocks = self.rebalance()
        for stock in rebalance_stocks:
            print(f"{stock["action"]} {stock["ticker"]} {stock["shares"]:.2f} shares.")
        
if __name__ == "__main__":
    # Stocks
    meta = Stock("META", 100, 360)
    appl = Stock("APPL", 30, 300)
    nvidia = Stock("NVDA", 40, 180)
    
    # Portafolios
    my_portafolio1 = Portafolio(
        stocks=[meta,appl],
        allocated_stocks={"META": 0.4, "APPL": 0.6}
    )
    my_portafolio2 = Portafolio(
        stocks=[meta,appl,nvidia],
        allocated_stocks={"META": 0.1, "APPL": 0.1, "NVDA": 0.8}
    )

    # Rebalances
    print(my_portafolio1)
    my_portafolio1.print_rebalance_actions()
    print("\n")
    print(my_portafolio2)
    my_portafolio2.print_rebalance_actions()



