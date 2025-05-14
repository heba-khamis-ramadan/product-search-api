# Product Search API

A simple Django-based API for searching products.

## Features

- Product listing and search
- RESTful API endpoints
- Easy to extend

## Requirements

- Python 3.8+
- Django 4.x
- Django REST Framework

## Setup

```bash
git clone https://github.com/yourusername/product-search-api.git
cd product-search-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the Server

```bash
python manage.py migrate
python manage.py runserver
```

## API Endpoints

- `GET /api/products/` — List all products
- `GET /api/products/?search=keyword` — Search products by keyword

## License

MIT