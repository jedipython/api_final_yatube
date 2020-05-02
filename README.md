# api_final

## Описание

REST API для проекта на Django, позволяет получать, обновлять, добавлять данные на сайт. Работает с постами, комментариями, подписками, группами (категориями) постов. Аутентификация выполняется посредством получения токена JWT через POST-запрос.

## Установка

` pip install -r requirements.txt `

## Примеры
Примеры обращения к API:

* `/redoc/` - Документация
* `/token/` - Получить токен
* `/token/refresh/` - Обновить токен
* `/posts/` - Получить список всех публикаций / Создать новую публикацию
* `/posts/{id}/` - Получить публикацию по id / Обновить по id / Удалить по id
* `/posts/{post_id}/comments/` - Получить список комментариев
* `/posts/{post_id}/comments/{comment_id}/` - Получить комментарий по id  / Создать комментарий / Обновить / Удалить комментарий
* `/follow/` - Получить список подписчиков / Создать подписку
* `/group/` - Получить список всех групп / Создать группу


