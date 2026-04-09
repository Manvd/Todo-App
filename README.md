# 📝 Django Todo App with JWT Authentication

A Todo application built using Django and Django REST Framework with JWT authentication. The project uses a modular structure where the API logic is separated from the core Todo models.

---

## 🚀 Features

* User login system
* JWT Authentication
* Protected API routes
* Create, Read, Update, Delete Todos
* Frontend using Django Templates

---

## 🛠️ Tech Stack

* Python
* Django
* Django REST Framework
* HTML, CSS (Django Templates)
* SQLite

---

## 📁 Project Structure

```
todo-project/
├── api/              # Handles serializers, views, and API logic
├── todo/             # Contains models (database structure)
├── templates/        # HTML templates (UI)
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🧠 Architecture

* `todo` app → Defines database models (Todo items)
* `api` app → Handles serializers, views, and API endpoints
* `templates` → Provides basic frontend UI

---

## ⚙️ Setup

Clone the repository:

```bash
git clone https://github.com/your-username/todo-app.git
cd todo-app
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start server:

```bash
python manage.py runserver
```

---

## 📡 API Endpoints

### Auth

* POST /api/auth/login

### Todos (Protected)

* GET /api/todos
* POST /api/todos
* PUT /api/todos/<id>
* DELETE /api/todos/<id>

---

## 🔐 Authentication

Use JWT token in headers:

```
Authorization: Bearer <token>
```

---

## 📌 Notes

* Do not upload `.env` or database files
* Use `requirements.txt` for dependencies
* Make sure migrations are applied before running

---

## 📄 License

This project is open-source and free to use.
