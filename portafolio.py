# These can be Enum too
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
        return self.shares * self.current_price()
    
class Portafolio:
    """
    Portafolio with stocks and allocated stocks
    """
    def __init__(self, stocks, allocated_stocks):
        """
        stocks: list[Stocks]
        allocated_stocks: dict["ticker", percentage] e.g: {"META": 0.4, "APPL": 0.6}
        """
        self.stocks = stocks
        self.allocated_stocks = allocated_stocks

    def total_value(self):
        total = 0
        for stock in self.stocks:
            total += stock.value()
        return total

    def __str__(self):
        """String representation of the portfolio"""

        print(f"Portafolio - Total value: {self.total_value():3.f}\n")
        print("="*30 + "\n")

        for stock in self.stocks:
            percentage = (stock.value() / self.total_value()) * 100
            print(f"{stock.ticker}: {stock.shares} shares - price: {stock.price:3.f} = {stock.value():3f} ({percentage:2f})%")

    def rebalance(self):  
        """
        Returns which stocks should be sold and which ones should be bought to have a balanced Portafolio based on allocated stocks
        """
        rebalance_stocks = []
        total_value = self.total_value()

        for stock in self.stocks:
            target_percentage = self.allocated_stocks[stock.ticker]
            objetive_value = target_percentage * total_value
            objetive_shares = objetive_value / stock.current_price()

            # Buy or Sell depending of the difference
            shares_difference = objetive_shares - stock.shares
            stock_action = {"ticker": stock.ticker, "shares": abs(shares_difference)}
            if shares_difference > 0: 
                stock_action["action"] = ACTION_BUY
            elif shares_difference < 0:
                stock_action["action"] = ACTION_SELL
            else:
                stock_action["action"] = ACTION_KEEP
            rebalance_stocks.append(stock_action)
        return rebalance_stocks
        


if __name__ == "__main__":
    # Stocks
    meta = Stock("META", 100, 360)
    appl = Stock("APPL", 30, 300)
    nvidia = Stock("NVDA", 40, 180)
    
    my_portafolio1 = Portafolio(
        stocks=[meta,appl],
        allocated_stocks={"META": 0.4, "APPL": 0.6}
    )

    print(my_portafolio1)
    
    rebalance_stocks = my_portafolio1.rebalance()
    for stock in rebalance_stocks:
        print(f"{stock["action"]} {stock["ticker"]} {stock["shares"]} shares.")
    


