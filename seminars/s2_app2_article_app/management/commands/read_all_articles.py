from django.core.management.base import BaseCommand

from s2_app2_article_app.models import Article


class Command(BaseCommand):
    help = 'Выборка всех статей'

    def handle(self, *args, **options):
        articles = Article.objects.all()
        self.stdout.write(f'{articles}')
