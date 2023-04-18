# api_YaMDb

### Техническое описание проекта YaMDb:

Проект YaMDb собирает отзывы (Reviews) пользователей на произведения (Titles).

Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором.

Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

Отзыв может быть прокомментирован (Сomment) пользователями.

### Запуск проекта

Заполнить infra/.env по шаблону:

    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=postgres
    POSTGRES_USER=postgres
    POSTGRES_PASSWORD=postgres
    DB_HOST=db
    DB_PORT=5432

Сборка и запуск контейнеров:

    cd infra
    docker-compose up

Миграции:

    docker-compose exec web python manage.py migrate

Заполенение проекта тестовыми данными:

    docker-compose exec web python manage.py db_import

Создание суперпользователя:

    docker-compose exec web python manage.py createsuperuser

Сборка стат. файлов:

    docker-compose exec web python manage.py collectstatic --no-input

После этого можно перейти на http://127.0.0.1:80/admin/

### Над проектом работали:

[Максим Бризганов](https://github.com/Tapochekmira) | Разработчик, контент пользователей: Category, Genre, Title

</b>

[Элмер Ефлов](https://github.com/nm0i) | Разработчик, кастомная модель User + Review, Comment

</b>

[Сергей Патраков](https://github.com/sergeypatrakov) | Разработчик, модель администратора Admin + регистрация и аутентификация пользователей
