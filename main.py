import os
import datetime
from data.news import News
from forms.user import RegisterForm
from flask import Flask, redirect, render_template, request
from data import db_session
from data.users import User
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


class LoginForm(FlaskForm):
    username = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')


def main():
    db_session.global_init("db/blogs.db")
    # app.run()


@app.route('/list-market')
def news():
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#')
        x = 0
        tovari_rasfasovka = []
        a = 0
        sam_tovar = ''
        for i in tovari:
            if a == 0:
                sam_tovar = i
                a = 1
            else:
                tovari_rasfasovka.append(sam_tovar + '#' + i)
                a = 0
        return render_template('css/index.html', tovari=tovari_rasfasovka, x=x)


@app.route('/list-market_')
def newss():
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#')
        x = 0
        print(tovari)
        return render_template('css/index_reg.html', tovari=tovari, x=x)


@app.route('/list-market_tovar')
def tovar():
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#')
        x = 0
        name = []
        foto = []
        for i in tovari:
            ii = i.split()
            name.append(ii[0])
            foto.append(ii[1])
        return render_template('css/tovar.html', name=name, foto=foto, x=x)


@app.route('/list-market_akkaynt')
def akkaynt():
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#')
        x = 0
        print(tovari)
        return render_template('css/akkaynt.html', tovari=tovari, x=x)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("css/register.html", news=news)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/list-market_')
    return render_template('css/login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('css/register.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('css/register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        user = User(
            name=form.name.data,
            email=form.email.data,
            about=form.about.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('css/register.html', title='Регистрация', form=form)


@app.route('/sozdanie_tovara', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        data = os.listdir('static/img')
        data2 = []
        for i in data:
            data2.append('static/img/' + i)
        data = data2
        return render_template('css/sozdanie_tovara.html', data=data)
    elif request.method == 'POST':
        for i in range(1000):
            if not os.path.exists('static/img/r' + str(i) + '.png'):
                chislo = i
                f = request.files['file']
                f.save('static/img/r' + str(chislo) + '.png')
                break
        data = os.listdir('static/img')
        data2 = []
        for ii in data:
            data2.append('static/img/' + ii)
        data = data2
        # with open('static/img/riana.png', 'wb') as ff:
        # ff.write(f.read())
        return render_template('css/sozdanie_tovara.html', data=data)


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
