from django.core.management.base import BaseCommand
from myapp2.models import User


class Command(BaseCommand):
    help = "Get user with age greater <age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **kwargs):
        age = kwargs['age']
        user = User.objects.filter(age__gt=age)
        self.stdout.write(f'{user}')

    # Для фильтрации объектов модели по заданным условиям можно использовать
    # метод filter() c параметрами через двойное подчеркивание:
    #   Model.objects.filter(<table_name>__<param>=value)
    # примеры <param>:
    # 💡 exact - точное совпадение значения поля
    # 💡 iexact - точное совпадение значения поля без учета регистра
    # 💡 contains - значение поля содержит заданный подстроку
    # 💡 in - значение поля находится в заданном списке значений
    # 💡 gt - значение поля больше заданного значения
    # 💡 gte - значение поля больше или равно заданному значению
    # 💡 lt - значение поля меньше заданного значения
    # 💡 lte - значение поля меньше или равно заданному значению
    # 💡 startswith - значение поля начинается с заданной подстроки
    # 💡 endswith - значение поля заканчивается на заданную подстроку
    # 💡 range - значение поля находится в заданном диапазоне значений
    # 💡 date - значение поля является датой, соответствующей заданной дате
    # 💡 year - значение поля является годом, соответствующим заданному году
