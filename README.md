# Technical Task company "IDIA Market"

## Project structure

```
.
├── /
│   ├── custom_addons/          # Catalog for Odoo custom modules
│   ├── init_db/                # Script for database initialization
│   │   └── init.sql            # SQL file for creating user and DB
│   ├── src/                    # Main project files
│   │   └── docker-compose.yml  # Docker Compose configuration to run Odoo and PostgreSQL
├── README.md                   # Project documentation

```

## How to run the project

### Шаг - 1. Clone rep
```bash
git clone https://github.com/NurzhauganovA/techtaskIDIA.git
```

### Шаг - 2. Run docker-compose file
```bash
cd techtaskIDIA/src
docker compose -f docker-compose.yml up --build
```

### Шаг - 3. Follow the link
```bash
http://127.0.0.1:8069
```
