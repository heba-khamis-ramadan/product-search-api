from django.core.management.base import BaseCommand
from products.models import Product
import random

class Command(BaseCommand):
    help = 'Seed the database with dummy products (English and Arabic names)'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding products...')

        english_names = ['Milk', 'Bread', 'Cheese', 'Juice', 'Rice', 'Water', 'Yogurt', 'Chocolate', 'Chips', 'Coffee']
        arabic_names = ['حليب', 'خبز', 'جبن', 'عصير', 'أرز', 'ماء', 'زبادي', 'شوكولاتة', 'بطاطس', 'قهوة']
        brands = ['Nestle', 'Kellogg', 'Heinz', 'PepsiCo', 'Unilever', 'Danone', 'Almarai']
        categories = ['Snacks', 'Beverages', 'Cereal', 'Dairy', 'Bakery']
        nutrition_facts = [
            'High in fiber',
            'Low sugar',
            'Rich in protein',
            'Contains calcium',
            'Low fat',
            'خالي من السكر',
            'غني بالبروتين',
            'يحتوي على الكالسيوم',
        ]

        for i in range(1, 201):  # Create 200 dummy products
            is_arabic = random.choice([True, False])
            name = f"{random.choice(arabic_names) if is_arabic else random.choice(english_names)} {i}"

            product = Product.objects.create(
                name=name,
                brand=random.choice(brands),
                category=random.choice(categories),
                price=round(random.uniform(1.0, 200.0), 2),
                nutrition_facts=random.choice(nutrition_facts),
                description=f"هذا وصف للمنتج {i}" if is_arabic else f"This is a description for product {i}",
                stock=random.randint(0, 1000)
            )
            self.stdout.write(f"Created: {product.name}")

        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded 200 products!'))
