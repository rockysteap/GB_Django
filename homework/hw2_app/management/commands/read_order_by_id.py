from django.core.management.base import BaseCommand

from hw2_app.models import Order
from hw2_app.utils import validator


class Command(BaseCommand):
    help = f'Чтение по id Заказа'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id заказа')

    def handle(self, *args, **options):
        order_id = options.get('order_id')

        error_info = f'Чтение Заказа не удалось.'
        if not validator.is_value_present_in_db(order_id, Order, 'pk'):
            self.stdout.write(f'order_id: "{order_id}" в БД не найден. {error_info}')
            return

        order = Order.objects.filter(pk=order_id).first()
        self.stdout.write(f'{"-"*44} Заказ {order.pk} {"-"*44}')
        self.stdout.write(f'{order}')
        self.stdout.write(f'{"-"*40} Товары в заказе {"-"*40}')
        for product in order.products.all():
            print(product)
        self.stdout.write(f'{"-"*33} Общая сумма заказа: {order.total} {"-"*33}')
