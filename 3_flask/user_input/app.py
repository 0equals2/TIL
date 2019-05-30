from flask import Flask, render_template,request
from iexfinance.stocks import Stock

import pprint
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_stock')
def stock():
    return render_template('search_stock.html',
                           is_first_search=True,)

@app.route('/search_result')
def result():
    TOKEN = 'pk_3735af3998a84704aa98d4b7e9c0cd15'
    user_input = request.args.get('keyword')
    if user_input:
        stock = Stock(user_input, token=TOKEN) #대문자는 class
    try:
        data = stock.get_quote()
    except:
        return render_template(
            'search_stock.html',
            result=False,
        )
    return render_template('search_stock.html',
        result = True,
        c_name=data['companyName'],
        l_price=data['latestPrice'],
        )

if __name__ == '__main__':
    app.run(debug=True)
