from django.http import HttpResponse
import logging
from datetime import datetime

logger = logging.getLogger(__name__)


def main(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Мой сайт</title>
    </head>
    <body>
        <h1>Добро пожаловать на сайт!</h1>
    </body>
    </html>
    """
    logger.info(f'страница main посещалась в: {datetime.now()}')
    return HttpResponse(html)


def about_me(request):
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Обо мне</title>
    </head>
    <body>
        <h1>Меня зовут Лесников Игорь, я являюсь студентом GB по специальность Python-разработчик</h1>
    </body>
    </html>
    """
    logger.info(f'страница about_me посещалась в: {datetime.now()}')
    return HttpResponse(html)
