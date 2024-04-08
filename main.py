from flask import Flask, url_for, render_template
import os

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/index')
def cosmos():
    return "И на Марсе будут яблони цвести!"


@app.route('/list-market')
def news():
    with open('data_market/info_tovar.txt') as f:
        tovari = f.read().split('#')
        x = 0
        name = []
        foto = []
        for i in tovari:
            ii = i.split()
            name.append(ii[0])
            foto.append(ii[1])
        return render_template('css/index.html', name=name, foto=foto, x=x)


@app.route('/image_sample')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style123.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Первая HTML-страница</h1>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
