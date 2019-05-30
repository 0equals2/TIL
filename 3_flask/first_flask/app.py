from flask import Flask, render_template  # pip install requests
import lotto_package

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/pick_lotto')
def pick_lotto():
    lucky_numbers = lotto_package.get_random_numbers()
    return render_template('pick_lotto.html', numbers=lucky_numbers)


@app.route('/get_lotto/<int:num>')
def get_lotto(num):
    data = lotto_package.get_lotto_numbers(num)  # { 'real': [1,2,3], 'bonus': 4 }
    return render_template(
        'get_lotto.html',
        numbers=data['real'],
        draw_no=num
    )


@app.route('/lotto/<int:num>')
def lotto(num):
    lucky_numbers = lotto_package.get_random_numbers()
    real_data = lotto_package.get_lotto_numbers(num)  # { 'real': [1,2,3,4,5,6], 'bonus': 7 }

    real_numbers = real_data['real']
    bonus_number = real_data['bonus']

    result = lotto_package.get_result(real_numbers, lucky_numbers, bonus_number)

    return render_template(
        'lotto.html',
        result=result,
        real_numbers=real_numbers,
        lucky_numbers=lucky_numbers,
        bonus=bonus_number,
    )


@app.route('/square/<int:num>')
def square(num):
    result = num ** 2
    return f'{result}'


if __name__ == '__main__':
    app.run(debug=True)
