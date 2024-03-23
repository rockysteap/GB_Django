from django.core.management.base import BaseCommand
from myapp2.models import Author, Post


class Command(BaseCommand):
    help = "Get all posts by author id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    """
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        author = Author.objects.filter(pk=pk).first()
        if author is not None:
            posts = Post.objects.filter(author=author)
            intro = f'All posts of {author.name}\n'
            text = '\n'.join(post.content for post in posts)
            self.stdout.write(f'{intro}{text}')
    """

    # Если нам не нужно имя автора в строке intro, можно снизить
    # количество запросов к базе данных и фильтровать посты
    # по автору непосредственно из модели пост:
    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        posts = Post.objects.filter(author__pk=pk)
        intro = f'All posts\n'
        # text = '\n'.join(post.content for post in posts)
        # Изменим вывод всего содержимого из content
        # на пользовательский метод внутри модели User,
        # который выводи первые 8 слов:
        text = '\n'.join(post.get_summary() for post in posts)
        self.stdout.write(f'{intro}{text}')

    # Иными словами, просим найти посты где у поля автор первичный ключ равен pk.
