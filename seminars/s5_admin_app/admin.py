# Задание №1
# 📌 Проверьте возможность доступа к админке.
# 📌 Создайте суперпользователя и войдите в админ панель.
#
# >: python manage.py createsuperuser
# -> login at http://127.0.0.1:8000/admin/ with su
#
#
# Задание №2
# 📌 Подключите к админ-панели созданные вами в рамках прошлых семинаров модели в приложениях:
#   ○ случайные числа,
#   ○ блог,
#   ○ магазин,
#   ○ другие, если вы их создавали.
#
#  В проекте seminars присутствуют модели Author, Article и Comment, буду использовать их,
#  в частности последнюю реализацию из приложения s4_app2_article_app.
from django.contrib import admin
from s4_app2_article_app.models import Author, Article, Comment
#
# Подключение моделей для задания 2:
# admin.site.register(Author)
# admin.site.register(Article)
# admin.site.register(Comment)
# Подключение моделей перенесено ниже в задание 5 (после объявления классов ModelAdmin)
#
#  Остальные модели будут подключаться в рамках проекта homework.
#
#
# Задание №3
# 📌 Создайте в админ панели несколько групп.
# Логика следующая:
# 📌 Группа определяет права внутри своего приложения.
# 📌 Группа читателей может просматривать модели приложения.
# 📌 Группа редакторов может читать, добавлять и изменять модели приложения.
# 📌 Группа админы также может удалять модели.
#
# Создадим группы:
# 1. s4_app2_Readers
#  permissions: s4_app2_article_app | author, article, comment | Can view
# 2. s4_app2_Editors
#  permissions: s4_app2_article_app | author, article, comment | Can add, change, view
# 3. s4_app2_Admins
#  permissions: s4_app2_article_app | author, article, comment | Can add, change, delete, view
#
# Создадим пользователей, добавим 'staff status' и отнесем в соответствующие группы:
# 1. Читатели: reader1, reader2, reader3 -> s4_app2_Readers
# 2. Редакторы: editor1, editor2, editor3 -> s4_app2_Editors
# 3. Админы: admin1, admin2, admin3 -> s4_app2_Admins
#
#  Залогинемся всеми представителями и проверим права использования на соответствие условиям задачи.
#
#
# Задание №4
# 📌 Создайте десяток разных пользователей.
# 📌 Помимо минимальной информации заполните дополнительные поля модели.
# 📌 Дайте пользователям права из различных групп, а также дополнительные индивидуальные разрешения.
#
# Десяток пользователей к этому моменту уже создано.
# Добавим пользователю reader1 возможность создавать комментарии
#  reader1 -> 'User permissions:' -> s4_app2_article_app | comment | can add comment
#
#
# Задание №5
# 📌 Настройте под свои нужды вывод информации об авторах, статьях и комментариях на страницах списков.
#


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email']
    ordering = ['lastname', 'firstname']
    search_fields = ['lastname', 'firstname']


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'time_stamp', 'author', 'category', 'views', 'is_published']
    ordering = ['-views']
    list_filter = ['category', 'is_published']
    search_fields = ['title', 'author']


class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'article', 'content', 'time_stamp_modify']
    ordering = ['-time_stamp_modify', 'author']
    list_filter = ['author']
    search_fields = ['content']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)

# В ДЗ:
# 📌 Настройте под свои нужды вывод информации о клиентах,
# товарах и заказах на страницах вывода информации об
# объекте и вывода списка объектов.
