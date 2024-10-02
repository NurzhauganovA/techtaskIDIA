Задание для кандидата

1. Ознакомится с туториалом Odoo https://www.odoo.com/documentation/16.0/developer/tutorials/getting_started.html
2. Установить Odoo:
- Склонировать Odoo. `git clone https://github.com/odoo/odoo.git --depth 1 --branch 16.0`
- Установить Postgresql
- Запуск через `python odoo-bin -d <db_name> -r <db_user> -w <db_password>`
4. Создать кастомный аддон с моделькой товар (Product)
Поля модельки - Название, цвет, дата поставки, цена, количество, размеры (высота, ширина, глубина)
5. Сделать список товаров используя Tree View
6. Сделать деталку товара используя Form View
7. Добавить computed field объём, который считается из размеров
8. Добавить валидацию цены (цена не может быть отрицательной)
9. компьютер көрінбей тұры керек