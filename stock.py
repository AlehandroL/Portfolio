# Stock class included only for testing Portfolio methods.


import string


class Stock:
    """A Stock object that contains information about historic prices of the stock."""
    
    def __init__(self, name: 'str', historic_value: 'dict'):
        self.name = name
        self.historic_value = historic_value
    
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name

    def Price(self, date: string):
        return self.historic_value[date]
