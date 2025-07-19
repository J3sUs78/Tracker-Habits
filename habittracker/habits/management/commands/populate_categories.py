from django.core.management.base import BaseCommand
from habits.models import Category

class Command(BaseCommand):
    help = 'Pobla la base de datos con categorías predefinidas'

    def handle(self, *args, **options):
        categories_data = [
            {
                'name': '🏥 Salud y Bienestar',
                'description': 'Hábitos relacionados con la salud física y mental'
            },
            {
                'name': '⚡ Productividad',
                'description': 'Hábitos para mejorar la eficiencia y organización'
            },
            {
                'name': '📚 Aprendizaje',
                'description': 'Hábitos para el desarrollo personal y profesional'
            },
            {
                'name': '💰 Finanzas',
                'description': 'Hábitos para el manejo del dinero y ahorro'
            },
            {
                'name': '❤️ Relaciones',
                'description': 'Hábitos para mejorar las relaciones personales'
            },
            {
                'name': '💪 Ejercicio',
                'description': 'Hábitos de actividad física y deporte'
            },
            {
                'name': '🥗 Alimentación',
                'description': 'Hábitos de nutrición y alimentación saludable'
            },
            {
                'name': '🧘 Meditación',
                'description': 'Hábitos de mindfulness y relajación'
            },
            {
                'name': '🧹 Limpieza',
                'description': 'Hábitos de organización y limpieza personal'
            },
            {
                'name': '🎨 Creatividad',
                'description': 'Hábitos para desarrollar la creatividad y hobbies'
            }
        ]

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