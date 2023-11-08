from django.core.management.base import BaseCommand, CommandError
from newsapp.models import *


class Command(BaseCommand):
    help = 'Delete all news at category'

    def add_arguments(self, parser):
        parser.add_argument('post', type=str)

    def handle(self, *args, **options):
        answer = input(f'Are you sure you want to delete all posts at category {options["category"]}? yes/no')

        if answer != 'yes':
            self.stdout.write(self.style.ERROR('Canceled'))
            return
        try:
            postCategory = Category.objects.get(name=options['category'])
            Post.objects.filter(postCategory=postCategory).delete()
            self.stdout.write(self.style.SUCCESS(f'Succesfully deleted all news from category {postCategory.name}')) # в случае неправильного подтверждения говорим, что в доступе отказано
        except Post.DoesNotExist:
            self.stdout.write(self.style.ERROR(f'Could not find category {postCategory.name}'))