from flask import Flask, url_for, request
enctype="multipart/form-data"

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route('/sample_file_upload', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        f = request.files['file']
        f.save('static/img/riana.png')
        # with open('static/img/riana.png', 'wb') as ff:
        # ff.write(f.read())
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                            <title>Пример загрузки файла</title>
                          </head>
                          <body>
                            <h1>Загрузим файл</h1>
                            <form method="post" enctype="multipart/form-data">
                               <div class="form-group">
                                    <label for="photo">Выберите файл</label>
                                    <input type="file" class="form-control-file" id="photo" name="file">
                                </div>
                                <img src="{url_for('static', filename='img/riana.png')}" 
                                alt="здесь должна была быть картинка, но не нашлась">
                                <button type="submit" class="btn btn-primary">Отправить</button>
                            </form>
                          </body>
                        </html>'''


@app.route('/carousel')
def carousel():
    return f'''<html>
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
  </head>
  <body>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img class="d-block w-100" src="static/img/riana.png" alt="фото нету">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="static/img/neeeinginer.png" alt="не найдено">
    </div>
    <div class="carousel-item">
      <img class="d-block w-100" src="static/img/riana.png" alt="произошла техническая шоколадка">
    </div>
  </div>
  <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Предыдущая</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Следующая</span>
  </a>
</div>
  </body>
</html>'''


@app.route('/listm')
def listm():
    return f'''<!DOCTYPE html>
<html lang="ru">
	<head>
	  <!-- Важная техническая информация для браузера -->
		<meta charset="utf-8">
		<meta http-equiv="X-UA-Compatible" content="IE=edge">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<!-- Информация об Авторе и описание проекта -->
		<meta name="description" content="сайт разработчика">
		<meta name="auyhor" content="егор">

		<!-- Иконка, которая будет на вкладке в браузере -->
		<link rel="icon" href="/favicon.ico">
		<!-- Заголовок на вкладке в браузере -->
		<title>Магазин sinteleo</title> 

		<link href="https://fonts.googleapis.com/css?family=Roboto:400,700&amp;sudset=cyrillic-ext"rel="stylesheet">
		<!-- Подключаем наш файл со стилями, который находится в папке css-->
		<link rel="stylesheet" href="bootstrap-grid.min.css">
		<link rel="stylesheet" href="css/animate.css-4.1.1.zip">
		<link href="style.css" rel="stylesheet">
	</head>
	<body>

		<header>
 			<div class="container">
 				<div class="row">
 					<div class="col-lg-7">
 						<img class="header-img wow fadeInleftBig" src="img/one.png" alt="">
 					</div>
 					<div class="col-lg-5">
 						<p class="header-pretitle wow fadeInRightBig" data-wow-delay="0.1s">поиск</p>
 						<h1 class="header-title wow fadeInRightBig"data-wow-delay="0.2s">место </h1>
 						<p class="header-subtitle wow fadeInRightBig"data-wow-delay="0.3s">В <br> Р </p>
 						<div class="header-button-block wow fadeInRightBig"data-wow-delay="0.4s">
 						<!--<a href="https://vk" class="header-button">Связатся</a>-->
 						<small></small>	
 						</div>
 					</div>
 				</div>
 			</div>

 		</header>

<section class="portfolio">
	<div class="container">
		<div class="porfolio-block wow fadeIn">
		<h2 class="portfolio-title">Фотографии</h2>
		<p class="porfolio-subtitle">Информация</p>
		<div class="foto12345">
        <img src="img/Screenshot_20220823_165511_com.whatsapp.jpg" alt="Га">
    </div>
		<div class="row">
			<div class="col-md-6">
				<div class="portfolio-col-1">
					<img src="img/Screenshot_20220823_165513_com.whatsapp.jpg" alt="Га">
				<h3>В</h3>
				<p class="portfolio-text">У "Га</p>
				<a href="file:///C:/Users/egor5/OneDrive/%D0%A0%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9%20%D1%81%D1%82%D0%BE%D0%BB/website/css/index.html">Смотреть фотографии и описание</a>
				</div>
			</div>
			<div class="col-md-6">
			<div class="portfolio-col-2">
				<img src="img/Screenshot_20220823_165514_com.whatsapp.jpg" alt="">
			<h3>Сайт </h3>
			<p class="portfolio-text">О</p>
			<a href="#">позвонить</a>
			</div>
			</div>
		</div>
		</div>
	</div>
	
</section>

<footer>
	<div class="container">
		<div class="row">
			<div class="col-md-4">
				<h4 class="footer-author">название</h4>
				<p class="footer-text">Р</p>
			</div>
			<div class="col-md-4">
				<div class="social-block">
					<p>Способы связатся с разработчиком:</p>
					<a class="wow bounceInDown" data-wow-delay="0.2s" href="#"><img src="img/onezz.png" alt="Telegram"></a>
				</div>
			</div>
			<div class="col-md-4">
				<div class="footer-cta-block">
					<p class="footer-cta">Н:</p>
				<a href="" class="footer-button">Написать</a>
				</div>
			</div>
		</div>
	</div>
</footer>

<script src="js/wow.min.js"></script>
<script>
	new WOW().init();
</script>

</body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')