#Portfolio

Repository made for applying to Fintual's developer position.

0. Content:

	1. Assignment
	2. Files
		a. 'portfolio.py'
		b. 'stock.py'
		c. 'main.py'
		d. 'test_portfolio.py'
	3. Solution explained



1. Assignment:

	Construct a simple Portfolio class that has a collection of Stocks and a "Profit" method that receives 2 dates and returns the profit of the Portfolio between those dates. Assume each Stock has a "Price" method that receives a date and returns its price.

	Bonus Track: make the Profit method return the "annualized return" of the portfolio between the given dates.



2. Files: 

	a. 'portfolio.py' : Contains the requested Portfolio class, and thus is the only relevant file to be reviewed. 

	b. 'stock.py' : A made up Stock class used for initializing and testing Portfolio capabilities. Other than __init__, __str__ and __repr__ methods, it includes the forementioned Price method (input dates should be passed as "YYYY-MM-DD" strings).

	c. 'main.py' : A simple script for testing the functionality of Portfolio methods.

	d. 'test_portfolio.py' : Contains unittests for some of the Portfolio methods.



3. Solution explained:

	Portfolio class has one protected array '_stocks' of dimensions n x 2 (n = number of different Stocks in it), where every item is a dimension-2 array ( _stock[i] = ['Stock object', 'Integer']), containing the Stock and the number of shares owned.
	
	Even though it was not required to include the number of shares, it stroke me as relevant to consider it since in practice every portfolio is conformed by a collection of different numbers of Stock shares. This is key when comparing different portfolios.
	
	
	
						TBC# preauth-io
