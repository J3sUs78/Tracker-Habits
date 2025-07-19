from django.core.management.base import BaseCommand
from habits.models import Category

class Command(BaseCommand):
    help = 'Agrega emojis a las categorías existentes'

    def handle(self, *args, **options):
        categories_emojis = {
            'Salud y Bienestar': '🏥',
            'Productividad': '⚡',
            'Aprendizaje': '📚',
            'Finanzas': '💰',
            'Relaciones': '❤️',
            'Ejercicio': '💪',
            'Alimentación': '🥗',
            'Meditación': '🧘',
            'Limpieza': '🧹',
            'Creatividad': '🎨'
        }

        updated_count = 0
        for category_name, emoji in categories_emojis.items():
            try:
                category = Category.objects.get(name=category_name)
                # Actualizar el nombre con el emoji
                category.name = f"{emoji} {category_name}"
                category.save()
                updated_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Categoría actualizada: {category.name}')
                )
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f'Categoría no encontrada: {category_name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Se actualizaron {updated_count} categorías con emojis')
        ) 