# python-advanced-intro

## Описание
Проект представляет собой микросервис на FastAPI с конечной точкой для получения данных о пользователе, содержит набор api тестов.

### Задание из урока
Разработать микросервис на Python + FastAPI, можно использовать ChatGPT / autotests.ai (для аппрува доступа отписать в чат потока).



1. Разработать несколько API-автотестов на https://reqres.in (если обучались на основном курсе python - можно взять код автотестов из домашнего задания)\
Можно также за основу взять https://github.com/qa-guru/qa_guru_python_9_19
2. Вместо https://reqres.in разработать свой микросервис в стеке Python + FastAPI (допускается также Flask, Django).
Пример - https://github.com/qa-guru/python-advanced-intro

- Автотесты должны также успешно проходить.

- В коде микросервиса не должно быть хардкода\
Например, не должно быть эндпоинтов типа /api/users/2 -  правильнее /api/users/{user_id}

3. Данные для ответа пока что можно хранить в текстовом файле, в следующих занятиях мы перенесем их в базу данных

4. Желательно оформить README.md - https://school.qa.guru/teach/control/stream/view/id/465999013 в тренинге есть несколько занятий по оформлению красивой документации.

### Структура проекта

- mservice_tests/api_tests/test_users_get_single_user.py – api тесты для проверки работы ручки.
- mservice/service.py – основной файл с реализацией микросервиса FastAPI.
- main.py – файл для запуска сервера.

## Установка
1.	Клонируйте репозиторий:
```sh
git clone <URL_репозитория>
```
2. Настройте виртуальное окружение проекта, указав интерпретатор
3. Установите зависимости из requirements.txt

## Запуск сервера
```sh
python3 main.py
```

## API
### Конечные точки
- GET /api/users/{id}\
  Возвращает данные пользователя по id.

## Тестирование

Для запуска тестов выполните команду:
```sh
 pytest -v -s -l --alluredir=allure-results
```
Для генерации отчета тестирования выполните команду:
```sh
 allure serve allure-results/
```

### Примечания
- Убедитесь, что сервер запущен перед запуском тестов.