# 🛒 Product Search API
![Product Search API](https://res.cloudinary.com/dncl2sqt9/image/upload/v1748607078/Projects_Cover_2_pi8qkf.png)
A high-performance product search API built with **Django**, **PostgreSQL**, and **Elasticsearch**, supporting:

- Partial keyword matching
- Misspellings
- Mixed language queries (English + Arabic)
- Fast, relevant results using full-text search

---

## 🚀 Features

- 🔎 Smart product search with fuzzy matching
- 🌐 Multilingual support (English/Arabic)
- 🧠 Elasticsearch integration for relevance and speed
- 🐳 Dockerized setup with PostgreSQL and Elasticsearch

---

## 🧱 Tech Stack

- **Backend:** Django 4.x, Django REST Framework
- **Database:** PostgreSQL 15
- **Search Engine:** Elasticsearch 8.5.1
- **Containerization:** Docker + Docker Compose

---

## 📦 Project Structure
``` bash
productapi/
├── Dockerfile
├── docker-compose.yml
├── entrypoint.sh
├── seed.sh
├── wait_for_db.sh
├── manage.py
├── requirements.txt
├── products/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── search.py
│   ├── serializers.py
│   └── templates/products/index.html
└── productapi/
    └── settings.py
```
---

## ⚙️ Setup & Run (Dockerized)

### 1. Clone the repo
``` bash
git clone https://github.com/your-username/product-search-api.git
cd product-search-api
```

### 2. Run the containers
``` bash
docker-compose up --build
```
This will:
- Start PostgreSQL on port 5432
- Start Elasticsearch on port 9200
- Start Django app on port 8000
- Seed initial data


## 🧪 API Endpoints
### 🔗 Postman Published Documentation 👉 https://documenter.getpostman.com/view/34169826/2sB2qXj2no

### Search Products
``` bash
GET /api/search?search=milk
```
**Query Parameters:**

| Param   | Description                     |
|---------|---------------------------------|
| search  | Keyword or phrase (partial OK) |
| page    | (Optional) Page number         |

**Response:**
``` bash
{
    "count": 16,
    "next": "http://localhost:8000/api/search/?page=2&search=mlik",
    "previous": null,
    "facets": {},
    "results": [
        {
            "name": "Milk 43",
            "brand": "Almarai",
            "category": "Bakery",
            "price": 29.52,
            "nutrition_facts": "High in fiber",
            "description": "This is a description for product 43",
            "stock": 80
        },
        {
            "name": "Milk 51",
            "brand": "Unilever",
            "category": "Beverages",
            "price": 34.28,
            "nutrition_facts": "High in fiber",
            "description": "This is a description for product 51",
            "stock": 604
        },]
}
```
---

## 🖥 Frontend

Open your browser:
``` bash
http://localhost:8000/
```
The UI allows you to search and browse products live.

---

## 📦 Environment Variables

All required env variables are already handled inside docker-compose.yml.

If deploying outside Docker, ensure:

- DATABASE_URL
- ELASTICSEARCH_DSL
- DEBUG
- ALLOWED_HOSTS

are set.

---

## 📄 License

MIT License

---

## 🙋‍♀️ Author

Made with ❤️ by [Heba Khamis](https://github.com/heba-khamis-ramadan)