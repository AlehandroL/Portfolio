from portfolio import Portfolio
from stock import Stock

def main(): myFunction()

def myFunction():
    x = Portfolio()

    amzn = Stock('AMZN', ShareCollection(Share(datetime='2022-01-01', price=500), ] {: 500, '2022-02-01': 530, '2022-03-01': 598, '2022-04-01': 589})
    googl = Stock('GOOGL', {'2022-01-01': 800, '2022-02-01': 830, '2022-03-01': 798, '2022-04-01': 829})
    fb = Stock('FB', {'2022-01-01': 650, '2022-02-01': 630, '2022-03-01': 698, '2022-04-01': 709})

    print(str(type(a)))
    if str(type(a)).find(".Stock'") > -1:
        print('Hola')
    if isinstance(a, Stock) > -1:
        print('Hola')

    x.add_shares(a, 10)
    x.add_shares(b, 2)
    x.add_stock(c)

    print(x)

    print(x.profit('2022-01-01', '2022-04-01'))
    print(x.profit('2022-01-01', '2022-04-01', annualized_return=True))

    y = Portfolio(a, c)
    print(y)
    
    

if __name__ == '__main__': main()