# Fan-Sport — Интернет-магазин спортивных товаров

Легковесный интернет-магазин спортивных товаров, написанный на Django и Tailwind CSS. Поддерживает регистрацию, авторизацию пользователей, умный бэкенд-поиск по каталогу с фильтрацией цен, личный кабинет, полностью динамическую плавную тёмную тему и интерактивную корзину на LocalStorage с уведомлениями.

---

## Требования к системе
Перед запуском убедитесь, что у вас установлены:
* Python (версии 3.10 или новее)
* PostgreSQL (версии 13 или новее)

---

## Быстрый старт (Инструкция по запуску)

Выполните эти шаги по порядку в терминале вашей операционной системы.

### 1. Подготовка виртуального окружения
Создайте изолированное окружение и активируйте его.

**Для Windows (PowerShell):**
```powershell
python -m venv .venv
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
.venv\Scripts\activate
```

**Для macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Установка библиотек
Установите зависимости проекта строго под вашу версию PostgreSQL:
```bash
python -m pip install -r requirements.txt
```

### 3. Настройка базы данных
1. Откройте клиент PostgreSQL (pgAdmin или консоль psql) и создайте базу данных:
   ```sql
   CREATE DATABASE fansport_db;
   ```
2. Откройте файл `DjangoProject/settings.py` и в блоке `DATABASES` пропишите ваш реальный пароль от PostgreSQL (вместо `ВАШ_ПАРОЛЬ`):
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'fansport_db',
           'USER': 'postgres',
           'PASSWORD': 'ВАШ_ПАРОЛЬ',
           'HOST': '127.0.0.1',
           'PORT': '5432',
       }
   }
   ```

### 4. Применение таблиц и наполнение товарами
Создайте структуру таблиц на русском языке и залейте в базу 20 спортивных товаров с изображениями:
```bash
# Применяем миграции
python manage.py makemigrations
python manage.py migrate

# Запускаем скрипт автозаполнения
python manage.py seed_products
```

### 5. Создание администратора
Создайте профиль администратора для работы с панелью управления:
```bash
python manage.py createsuperuser
```

### 6. Запуск сервера
Запустите сервер разработки:
```bash
python manage.py runserver
```

После этого откройте браузер:
* Главная страница (О компании): http://127.0.0.1:8000/
* Каталог спортивных товаров: http://127.0.0.1:8000/catalog/
* Панель администратора (на русском языке): http://127.0.0.1:8000/admin/