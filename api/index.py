from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

# Пример данных для поиска (можно заменить на реальный источник данных)
routes = {
    "тату": [
        "77. Саранча ——— Ж.Д. Вокзал",
        "23. Тунель ——— Военкомат",
        "14. Базар стоянка ——— Ж.Д. Вокзал"
    ],
    "музей": [
        "54. Базар ——— Рес больница ",
        "14. Базар ——— Ж.Д вокзал",
        "7.  Базар ——— не знаю вроде Кум ауыл",
        "77. Саранча ——— Ж.Д вокзал",
        "55. Базар ——— Кум ауыл",
    ],
    "рес.больница": [
        "54. Базар стоянка ——— Рес больница",
        "10. Ж.Д вокзал ——— 26 мкр",
        "4.  Ж.Д вокзал ——— Аэропорт",
    ]
}

@app.route('/', methods=['GET'])
def home():
    return render_template('search.html', results=[])

@app.route('/search', methods=['POST'])
def search():
    location = request.form['location']
    # Простая фильтрация результатов по введенному месту
    filtered_results = [k for i,k in routes.items() if location in i]
    return render_template('search.html', results=filtered_results, loc=location)

@app.route('/map')
def map():
    return render_template('map.html')

@app.route('/qrcode')
def qrcode():
    return render_template('qrcode.html')


if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.38')
