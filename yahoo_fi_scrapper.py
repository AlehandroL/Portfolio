from array import array
import requests
from bs4 import BeautifulSoup


def extract_yahoo_finance_data(stock: str) -> array:
    url_yahoo = f"https://finance.yahoo.com/quote/{stock}/history"
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36"

    headers = {}
    headers["user-agent"] = user_agent

    response = requests.get(url_yahoo, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    soup = soup.find('tbody')

    search = soup.find_all('tr')
    rows = []
    count = 0

    for tr in search:
        if count >= 11: break
        row = [stock]
        for td in tr:
            row.append(td.text)
        if len(row) < 8: continue #skips exceptional data values
        rows.append(row)
        count += 1
    
    return rows


def transform_into_float(x: str) -> float:
    x = x.replace('.', '')
    x = x.replace(',', '.')
    x = float(x)
    x = "%.2f" % x
    return x


def substract_two_str(x: str, y: str) -> float:
    x = x.replace('.', '')
    x = x.replace(',', '.')
    x = float(x)
    y = y.replace('.', '')
    y = y.replace(',', '.')
    y = float(y)
    result = x - y
    result = "%.2f" % result
    return result

def process_data(data: array) -> array:
    processed_data = []
    for i, stock_data in enumerate(data):
        daily_data = []
        if stock_data == data[-1]: break
        daily_data.append(stock_data[0]) #stock name
        daily_data.append(stock_data[1]) #date
        daily_data.append(transform_into_float(stock_data[2])) #open
        daily_data.append(transform_into_float(stock_data[5])) #close
        daily_data.append(substract_two_str(stock_data[6], data[i+1][6])) #diff
        processed_data.append(daily_data)
    return processed_data  
        

stocks = ['AAPL', 'GOOG', 'AMZN']
stocks_data = []

for stock in stocks:
    extracted_data = extract_yahoo_finance_data(stock)
    stocks_data.append(process_data(extracted_data))

for stock_data in stocks_data:
    for daily_data in stock_data:
        print(daily_data)
