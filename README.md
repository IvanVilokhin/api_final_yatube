# api_final_yatube
 API для Yatube

## Описание
В проекте реализуется API для приложения Yatube. Функционал приложения - crud операции для постов и комментариев.
Доступна возможность подписки на других авторов.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/IvanVilokhin/api_final_yatube.git

```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас windows

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
## Примеры запросов к Api:

**Создание нового поста**
```
POST-запрос для авторизованного пользователя
POST http://127.0.0.1:8000/api/v1/posts/
Authorization: Bearer <JWT_токен>
```
Тело запроса:
```json
{
    "text": "some text"
}
```
Ответ:
```json
{
    "id": 1,
    "author": "username",
    "text": "some text",
    "pub_date": "2025-05-10T20:38:31.608545+03:00",
    "image": null,
    "group": null
}
```

**Получение списка постов**
GET-запрос для анонимного пользователя
```
GET http://127.0.0.1:8000/api/v1/posts/
```
Ответ:
```json
[
    {
        "id": 2,
        "author": "user1",
        "text": "text",
        "pub_date": "2025-05-10T20:54:20.560477+03:00",
        "image": null,
        "group": null
    },
    {
        "id": 1,
        "author": "user2",
        "text": "some text",
        "pub_date": "2025-05-10T20:38:31.608545+03:00",
        "image": null,
        "group": null
    }
]
```
**Получение списка сообществ**

```
GET-запрос для анонимного пользователя по адресу http://127.0.0.1:8000/api/v1/groups/ 
Ответ:
```json
[
    {
        "id": 1,
        "title": "TestGroup",
        "slug": "test-group",
        "description": "Some text."
    }
]
```
**Подписка на автора**
```
POST-запрос от авторизованного пользователя
POST http://127.0.0.1:8000/api/v1/follow/
Authorization: Bearer <JWT_токен>
```
Тело запроса:
```json
{
    "following": "user_1"
}
```
Ответ:
```json
{
    "following": "user_1",
    "user": "user"
}
```