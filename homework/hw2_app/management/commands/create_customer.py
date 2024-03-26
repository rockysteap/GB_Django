from django.utils.timezone import now
from django.core.management.base import BaseCommand

from hw2_app.models import Customer
from hw2_app.utils import validator


class Command(BaseCommand):
    help = f'Создание записи Клиента'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Имя пользователя')
        parser.add_argument('email', type=str, help='Email пользователя')
        parser.add_argument('phone_number', type=str, help='Номер телефона')

    def handle(self, *args, **options):
        username = options.get('username')
        email = options.get('email')
        phone_number = options.get('phone_number')

        error_info = f'Создание новой записи не удалось.'
        if validator.is_value_present_in_db(username, Customer, 'username'):
            self.stdout.write(f'username: "{username}" присутствует в БД. {error_info}')
            return
        if validator.is_value_present_in_db(email, Customer, 'email'):
            self.stdout.write(f'email: "{email}" присутствует в БД. {error_info}')
            return
        if validator.is_value_present_in_db(phone_number, Customer, 'phone_number'):
            self.stdout.write(f'phone_number: "{phone_number}" присутствует в БД. {error_info}')
            return

        customer = Customer(
            username=username,
            email=email,
            phone_number=phone_number,
            time_stamp_on_create=now(),
        )
        customer.save()

        self.stdout.write(f'{customer}')
