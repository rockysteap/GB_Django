from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']

        # user = User.objects.get(pk=pk)
        # !! get() заберет из БД запись по ключу, если ключа нет - выдаст ошибку
        # !! лучше использовать метод filter()
        user = User.objects.filter(pk=pk).first()
        # .first() вернет <class 'myapp2.models.User'> запись или None

        # user = User.objects.filter(pk=pk).all()  # Вернет запись или None
        # .all() -> вернет <QuerySet []> с записью (записями, если ищем не по уникальному ключу) или пустой

        self.stdout.write(f'{user}')
