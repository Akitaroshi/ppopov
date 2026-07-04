from django.core.management.base import BaseCommand
from library.models import Product, Category

class Command(BaseCommand):
    help = 'Наполняет базу данных Категориями и 20 спортивными товарами'

    def handle(self, *args, **options):
        # Очищаем старые категории и товары перед наполнением
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем категории спорт-товаров
        cat_shoes = Category.objects.create(name="Обувь", slug="shoes")
        cat_equip = Category.objects.create(name="Инвентарь", slug="equip")
        cat_wear = Category.objects.create(name="Одежда", slug="wear")

        products_data = [
            # === КАТЕГОРИЯ: ОБУВЬ ===
            {"category": cat_shoes, "name": "Беговые кроссовки Nike Air", "description": "Легкие кроссовки с амортизацией для пробежек.", "price": 8990.00, "image_url": "https://images.unsplash.com/photo-1542291026-7eec264c27ff?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_shoes, "name": "Кеды Converse Classic", "description": "Классические кеды для тренировок и прогулок в теплое время.", "price": 5490.00, "image_url": "https://images.unsplash.com/photo-1595950653106-6c9ebd614d3a?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_shoes, "name": "Футбольные бутсы Adidas", "description": "Бутсы с шипами для отличного сцепления на поле.", "price": 7990.00, "image_url": "https://images.unsplash.com/photo-1543326727-cf6c39e8f84c?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_shoes, "name": "Баскетбольные кроссовки Jordan", "description": "Стильные кроссовки с поддержкой голеностопа.", "price": 12990.00, "image_url": "https://images.unsplash.com/photo-1546519638-68e109498ffc?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_shoes, "name": "Шлепанцы для бассейна Arena", "description": "Нескользящая подошва, быстросохнущие материалы.", "price": 1490.00, "image_url": "https://images.unsplash.com/photo-1603561591411-07134e71a2a9?auto=format&fit=crop&w=600&q=80"},
            
            # === КАТЕГОРИЯ: ИНВЕНТАРЬ ===
            # Исправлена ссылка для Баскетбольного мяча:
            {"category": cat_equip, "name": "Баскетбольный мяч Wilson", "description": "Мяч из износостойкой композитной кожи.", "price": 2890.00, "image_url": "https://images.unsplash.com/photo-1519766304817-4f37bda74a27?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Теннисная ракетка Wilson", "description": "Легкая и прочная ракетка для точных ударов.", "price": 12500.00, "image_url": "https://images.unsplash.com/photo-1626224583764-f87db24ac4ea?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Коврик для йоги Reebok", "description": "Нескользящая мягкая поверхность, толщина 4 мм.", "price": 1990.00, "image_url": "https://images.unsplash.com/photo-1601925260368-ae2f83cf8b7f?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Набор стальных гантелей (2x10 кг)", "description": "Удобные гантели с надежной фиксацией дисков.", "price": 4500.00, "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Бутылка для воды спортивная", "description": "Пищевой BPA-free пластик, герметичный клапан.", "price": 890.00, "image_url": "https://images.unsplash.com/photo-1602143407151-7111542de6e8?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Фитнес-браслет Xiaomi Band", "description": "Мониторинг тренировок, пульса и сна.", "price": 3990.00, "image_url": "https://images.unsplash.com/photo-1575311373937-040b8e1fd5b6?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Спортивный рюкзак", "description": "Рюкзак с влагозащитным карманом для обуви.", "price": 3200.00, "image_url": "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Очки для плавания Arena", "description": "Защита от запотевания и УФ-лучей.", "price": 1490.00, "image_url": "https://images.unsplash.com/photo-1576013551627-0cc20b96c2a7?auto=format&fit=crop&w=600&q=80"},
            # Исправлена ссылка для Шлема:
            {"category": cat_equip, "name": "Шлем велосипедный Rockbros", "description": "Легкий шлем с регулировкой размера.", "price": 2490.00, "image_url": "https://images.unsplash.com/photo-1507136566006-cfc505b114fc?auto=format&fit=crop&w=600&q=80"},
            # Исправлена ссылка для Скакалки:
            {"category": cat_equip, "name": "Скоростная скакалка", "description": "Металлический трос со встроенными подшипниками.", "price": 750.00, "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Перчатки для турника", "description": "Защищают ладони от мозолей и проскальзывания.", "price": 990.00, "image_url": "https://images.unsplash.com/photo-1583454110551-21f2fa2afe61?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_equip, "name": "Массажный валик Roller", "description": "Идеально подходит для МФР-самомассажа дома.", "price": 1200.00, "image_url": "https://images.unsplash.com/photo-1600881333168-2ef49b341f30?auto=format&fit=crop&w=600&q=80"},
            
            # === КАТЕГОРИЯ: ОДЕЖДА ===
            {"category": cat_wear, "name": "Спортивный костюм кофта/брюки", "description": "Комфортный трикотажный костюм.", "price": 5500.00, "image_url": "https://images.unsplash.com/photo-1517838277536-f5f99be501cd?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_wear, "name": "Футболка беговая влагоотводящая", "description": "Синтетический материал для сухости кожи.", "price": 1190.00, "image_url": "https://images.unsplash.com/photo-1476480862126-209bfaa8edc8?auto=format&fit=crop&w=600&q=80"},
            {"category": cat_wear, "name": "Ветровка спортивная", "description": "Легкая куртка для защиты от ветра и дождя.", "price": 4200.00, "image_url": "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?auto=format&fit=crop&w=600&q=80"},
        ]

        for item in products_data:
            Product.objects.create(**item)

        self.stdout.write(self.style.SUCCESS('База данных успешно наполнена 20 товарами с рабочими картинками!'))