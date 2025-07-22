from django.core.management.base import BaseCommand
from habits.models import Category
from habits.constants import DEFAULT_CATEGORIES

class Command(BaseCommand):
    help = 'Pobla la base de datos con categorías predefinidas'

    def handle(self, *args, **options):
        categories_data = DEFAULT_CATEGORIES

        created_count = 0
        for category_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=category_data['name'],
                defaults={'description': category_data['description']}
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Categoría creada: {category.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Se crearon {created_count} categorías nuevas')
        ) 