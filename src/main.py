from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        birthday = request.form['birthday']
        sign = calculate_sign(birthday)
        return render_template('result.html', sign=sign)
    return render_template('index.html')

def calculate_sign(birthday):
    month, day = map(int, birthday.split('-')[1:])
    if month == 1 and day >= 20 or month == 2 and day <= 18:
        sign = 'みずがめ座'
    elif month == 2 and day >= 19 or month == 3 and day <= 20:
        sign = 'うお座'
    elif month == 3 and day >= 21 or month == 4 and day <= 19:
        sign = 'おひつじ座'
    elif month == 4 and day >= 20 or month == 5 and day <= 20:
        sign = 'おうし座'
    elif month == 5 and day >= 21 or month == 6 and day <= 20:
        sign = 'ふたご座'
    elif month == 6 and day >= 21 or month == 7 and day <= 22:
        sign = 'かに座'
    elif month == 7 and day >= 23 or month == 8 and day <= 22:
        sign = 'しし座'
    elif month == 8 and day >= 23 or month == 9 and day <= 22:
        sign = 'おとめ座'
    elif month == 9 and day >= 23 or month == 10 and day <= 22:
        sign = 'てんびん座'
    elif month == 10 and day >= 23 or month == 11 and day <= 21:
        sign = 'さそり座'
    elif month == 11 and day >= 22 or month == 12 and day <= 21:
        sign = 'いて座'
    else:
        sign = 'やぎ座'
    return sign

if __name__ == '__main__':
    app.run(debug=True)
