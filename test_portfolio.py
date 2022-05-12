import unittest

from datetime import date

from portfolio import Portfolio
from stock import Stock


class TestPortfolio(unittest.TestCase):

    def test_profit_values(self):
        
        amzn = Stock('AMZN', {'2022-01-01': 500, '2022-02-01': 530, '2022-03-01': 598, '2022-04-01': 589})
        googl = Stock('GOOGL', {'2022-01-01': 800, '2022-02-01': 830, '2022-03-01': 798, '2022-04-01': 829})
        fb = Stock('FB', {'2022-01-01': 650, '2022-02-01': 630, '2022-03-01': 698, '2022-04-01': 709})
        
        portfolio = Portfolio()
        portfolio.add_shares(amzn, 1)
        portfolio.add_shares(googl, 1)
        
        portfolio2 = Portfolio()
        portfolio2.add_shares(fb, 10)
        
        portfolio3 = Portfolio()
        portfolio3.add_shares(fb, 3)
        portfolio3.add_shares(googl, 2)
        
        self.assertEqual(portfolio.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-04-01')), 118)
        self.assertEqual(portfolio2.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-02-01')), -200)
        self.assertEqual(portfolio3.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-03-01')), 140)
        
    def test_annualized_profit_values(self):
        
        amzn = Stock('AMZN', {'2022-01-01': 500, '2022-02-01': 530, '2022-03-01': 598, '2022-04-01': 589})
        googl = Stock('GOOGL', {'2022-01-01': 800, '2022-02-01': 830, '2022-03-01': 798, '2022-04-01': 829})
        fb = Stock('FB', {'2022-01-01': 650, '2022-02-01': 630, '2022-03-01': 698, '2022-04-01': 709})
        
        portfolio = Portfolio()
        portfolio.add_shares(amzn, 1)
        portfolio.add_shares(googl, 1)
        
        portfolio2 = Portfolio()
        portfolio2.add_shares(fb, 10)
        
        portfolio3 = Portfolio()
        portfolio3.add_shares(fb, 3)
        portfolio3.add_shares(googl, 2)
        
        self.assertAlmostEqual(portfolio.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-04-01'), True), 0.42241978)
        self.assertAlmostEqual(portfolio2.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-02-01'), 1), -0.30786447)
        self.assertAlmostEqual(portfolio3.profit(date.fromisoformat('2022-01-01'), date.fromisoformat('2022-03-01'), 3), 0.27033981)
        
if __name__ == '__main__':
    unittest.main()