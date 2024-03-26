from decimal import Decimal

from django.core.management.base import BaseCommand

from hw2_app.models import Product, Order
from hw2_app.utils import validator


class Command(BaseCommand):
    help = (f'Изменение по id Заказа и id Товара. '
            f'Товар добавляется в Заказ, в случае отсутствия в Заказе. '
            f'Товар удаляется из Заказа, в случае обнаружения в Заказе. ')

    def add_arguments(self, parser):
        parser.add_argument('order_id', type=int, help='id заказа')
        parser.add_argument('product_id', type=int, help='id товара')

    def handle(self, *args, **options):
        order_id = options.get('order_id')
        product_id = options.get('product_id')

        error_info = f'Создание новой записи не удалось.'
        if not validator.is_value_present_in_db(order_id, Order, 'pk'):
            self.stdout.write(f'order_id: "{order_id}" в БД не найден. {error_info}')
            return
        if not validator.is_value_present_in_db(product_id, Product, 'pk'):
            self.stdout.write(f'product_id: "{product_id}" в БД не найден. {error_info}')
            return

        order = Order.objects.filter(pk=order_id).first()
        product = Product.objects.filter(pk=product_id).first()
        if product in order.products.all():
            order.products.remove(product)
        else:
            order.products.add(product)

        order.save()
        order.total = sum([Decimal(i.price) for i in order.products.all()])
        order.save()

        self.stdout.write(f'{order}')
