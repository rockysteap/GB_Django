from django.core.management.base import BaseCommand

from hw2_app.models import Order
from hw2_app.utils import validator


class Command(BaseCommand):
    help = f'Удаление по id Заказа'

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id заказа')

    def handle(self, *args, **options):
        order_id = options.get('order_id')

        error_info = f'Обновление БД не удалось.'
        if not validator.is_value_present_in_db(order_id, Order, 'pk'):
            self.stdout.write(f'order_id: "{order_id}" в БД не найден. {error_info}')
            return

        order = Order.objects.filter(pk=order_id).first()

        order.delete()
        self.stdout.write(f'Заказ с id {order_id} успешно удален.')
