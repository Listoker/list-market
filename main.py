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
import sqlalchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


Polzovatel = 'qwert()'


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
    # главное окно
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#_[')
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
        if sam_tovar not in tovari_rasfasovka[-1]:
            tovari_rasfasovka.append(sam_tovar + '#')
        return render_template('css/index.html', tovari=tovari_rasfasovka, x=x)


@app.route('/list-market_tovar/<tovarr>')
def tovar(tovarr):
    # ссылка на показ товара
    with open(f'static/text_tovarov/{tovarr}.txt', encoding='UTF-8') as f:
        text_vsego = f.read().split('#@{]')
        return render_template('css/tovar.html', text_vsego=text_vsego, tovarr=tovarr, polzovatel=Polzovatel)


@app.route('/list-market_akkaynt')
def akkaynt():
    # ссылка на товар
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        tovari = f.read().split('#_[')
        x = 0
        name = str(Polzovatel).split('"')[7]
        return render_template('css/akkaynt.html', tovari=tovari, x=x, name=name)


@app.route('/list-market_')
def newss():
    # окно зарегистрированное
    with open('data_market/info_tovar.txt', encoding='UTF-8') as f:
        name = str(Polzovatel).split('"')[7]
        tovari = f.read().split('#_[')
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
        if sam_tovar not in tovari_rasfasovka[-1]:
            tovari_rasfasovka.append(sam_tovar + '#')
        return render_template('css/index_reg.html', tovari=tovari_rasfasovka, x=x, name=name)


@app.route("/")
def index():
    db_sess = db_session.create_session()
    news = db_sess.query(News).filter(News.is_private != True)
    return render_template("css/register.html", news=news)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Войти в аккаунт
    form = LoginForm()
    if form.validate_on_submit():
        global Polzovatel
        Polzovatel = form.username
        email = sqlalchemy.Column(sqlalchemy.String,
                                  index=True, unique=True, nullable=True)
        return redirect('/list-market_')
    return render_template('css/login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def reqister():
    # регистрация
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
    # Добавление товара
    name = str(Polzovatel).split('"')[7]
    if request.method == 'GET':
        data = os.listdir('static/img')
        data2 = []
        for i in data:
            data2.append('static/img/' + i)
        data = data2
        return render_template('css/sozdanie_tovara.html', data=data, name=name)
    elif request.method == 'POST':
        # расфасовка
        phone = request.form.get('phone')  # запрос к данным формы
        email = request.form.get('email')
        nousername = request.form.get('nouserName')
        city = request.form.get('city')

        name = str(Polzovatel).split('"')[7]
        comment = request.form.get('comment')
        f = request.form.get('email')
        f = request.files['file']
        i = 0
        while True:
            i += 1
            # сохранение всего
            if not os.path.exists(f'static/img/foto_tovarov/{nousername}_{str(i)}.png'):
                f.save(f'static/foto_tovarov/{nousername}_{str(i)}.png')
                with open(f'static/text_tovarov/{nousername}_{str(i)}.txt', 'w', encoding='UTF-8') as tekst:
                    comment = comment + '#@{]' + phone + '#@{]' + email + '#@{]' + city + '#@{]' + name
                    tekst.write(comment)
                with open('data_market/info_tovar.txt', 'r', encoding='UTF-8') as tovari:
                    tovari__ = tovari.read()
                with open('data_market/info_tovar.txt', 'w', encoding='UTF-8') as tovari:
                    if tovari__ == '':
                        tovari.write(nousername + '_' + str(i))
                    else:
                        tovari.write(tovari__ + '#_[' + nousername + '_' + str(i))
                break

        data = os.listdir('static/img')
        data2 = []

        for ii in data:
            data2.append('static/img/' + ii)
        data = data2
        # with open('static/img/riana.png', 'wb') as ff:
        # ff.write(f.read())
        return redirect('/list-market_')


if __name__ == '__main__':
    main()
    app.run(port=8080, host='127.0.0.1')
