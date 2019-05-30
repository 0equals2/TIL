from iexfinance.stocks import Stock
import pprint

pp = pprint.PrettyPrinter()

TOKEN= 'pk_3735af3998a84704aa98d4b7e9c0cd15'

aapl = Stock('FB', token=TOKEN)  #대문자는 클래스
data = aapl.get_quote()
pp.pprint(data)
print(data['companyName'], data['latestPrice'])