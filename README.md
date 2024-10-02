# Technical Task company "IDIA Market"

## Project structure

```
.
├── /
│   ├── custom_addons/        # Каталог для кастомных модулей Odoo
│   ├── init_db/              # Скрипт для инициализации базы данных
│   │   └── init.sql          # SQL файл для создания пользователя и БД
│   ├── src/                  # Основные файлы проекта
│   │   └── docker-compose.yml # Docker Compose конфигурация для запуска Odoo и PostgreSQL
├── README.md                 # Документация проекта

```

## How to run the project

### Шаг - 1. Clone rep
```bash
git clone https://github.com/NurzhauganovA/techtaskIDIA.git
cd techtaskIDIA/src
```

### Шаг - 2. Run docker-compose file
```bash
docker compose -f docker-compose.yml up --build
```

### Шаг - 3. Follow the link
```bash
http://127.0.0.1:8069
```
