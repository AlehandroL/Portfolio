from datetime import date
from typing import Protocol

#Interface that recieves an stock object under the condition that it implements a "Price(date)" method
class stock_object(Protocol): 
    def Price(date: date) -> int: ...


class portfolio_item:
    """
    A portfolio_item contains a stock_object and the associated amount of shares owned.
    It implements the "Price" method, which call the method with the same name in it's stock_object.
    """
    def __init__(self, stock: stock_object, shares: int = 0):
        self.stock = stock
        self.shares = shares
    
    def set_shares(self, shares: int):
        self.shares = shares
    
    def add_shares(self, shares: int):
        self.shares += shares
    
    def remove_shares(self, shares: int):
        self.shares -= shares
    
    def get_shares(self) -> int:
        return self.shares
    
    def Price(self, date: date) -> int:
        return self.stock.Price(date)


class Portfolio:
    """A Portfolio object is a collection of portfolio_items and implements the "profit" method."""
    def __init__(self):
        self.portfolio_items = [] # [[portfolio_item_1], [portfolio_item_2], ... ]

    def __str__(self):
        return str(self.portfolio_items)

    def __repr__(self):
        return str(self.portfolio_items)

    def get_stock_index(self, stock: stock_object) -> int:
        """
        Returns the position of the Stock in the stocks array (-1 if not present).
        """
        for i, portfolio_item in enumerate(self.portfolio_items):
            if portfolio_item.stock == stock:
                return i
        return -1

    def has_stock(self, stock: stock_object) -> bool:
        if self.get_stock_index(stock) == -1:
            return False
        return True

    def add_stock(self, stock: stock_object) -> bool:
        """
        Returns false if the Stock is already in the Portfolio
        """
        if self.has_stock(stock):
            return False
        new_portfolio_item = portfolio_item(stock)
        self.portfolio_items.append(new_portfolio_item)
        return True

    def get_shares(self, stock: stock_object) -> int:
        index = self.get_stock_index(stock)
        if index == -1: 
            return 0
        portfolio_item = self.portfolio_items[index]
        return portfolio_item.get_shares()

    def add_shares(self, stock: stock_object, shares: int):
        if self.has_stock(stock):
            index = self.get_stock_index(stock)
            portfolio_item = self.portfolio_items[index]
            portfolio_item.add_shares(shares)
        else:
            if self.add_stock(stock):
                return self.add_shares(stock, shares)
            return False

    def remove_shares(self, stock: stock_object, shares: int):
        if self.has_stock(stock):
            index = self.get_stock_index(stock)
            portfolio_item = self.portfolio_items[index]
            portfolio_item.remove_shares(shares)

    def portfolio_value(self, date: date) -> float:
        portfolio_value = 0.0
        for p_item in self.portfolio_items:
            portfolio_value += p_item.get_shares()*p_item.Price(date.isoformat())
        return portfolio_value
    
    @staticmethod
    def dates_are_ordered(start_date: date, end_date: date) -> bool:
        return (start_date < end_date)

    @staticmethod
    def calculate_period_in_years(start_date: date, end_date: date) -> float:
        period = (end_date - start_date).days
        years = period/365.0
        return years

    def calculate_net_profit(self, start_date: date, end_date: date) -> int:
        start_value = self.portfolio_value(start_date)
        end_value = self.portfolio_value(end_date)
        return end_value - start_value
    
    def calculate_annualized_return(self, start_date: date, end_date: date) -> int:
        start_value = self.portfolio_value(start_date)
        end_value = self.portfolio_value(end_date)
        years = calculate_period_in_years(start_date, end_date)
        annualized_return = (end_value/start_value)**(1/years)-1
        return annualized_return

    def profit(self, start_date: date, end_date: date, annualized_return=False) -> float:
        if not dates_are_ordered(start_date, end_date):
            raise ValueError("'end_date' must be after 'start_date'.")
        if annualized_return is True: 
            annualized_return = self.calculate_annualized_return(start_date, end_date)
            return annualized_return
        profit = self.calculate_net_profit(start_date, end_date)
        return profit
