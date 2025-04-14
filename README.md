
# 📝 Task Service - FastAPI

A simple and efficient task management REST API built with **FastAPI**, using **PostgreSQL**, **SQLAlchemy**, and **Pydantic**.

---

## ✅ Objective

Implement a Task Service to:

- ✅ Create a task  
- ✅ Retrieve a task by ID  
- ✅ Update a task by ID  
- ✅ Delete a task by ID  
- ✅ Get all tasks by a specific user ID  

---

## ⚙️ Tech Stack

| Technology     | Purpose                               |
|----------------|----------------------------------------|
| FastAPI        | Web framework for building REST APIs   |
| SQLAlchemy     | ORM (Object Relational Mapper)         |
| PostgreSQL     | Relational database                    |
| Pydantic       | Data validation and serialization      |
| Uvicorn        | ASGI server to run the FastAPI app     |
| dotenv         | Load environment variables from `.env` |

---

## 📁 Project Structure

```
fastapi-task-service/
├── app/
│   ├── __init__.py
│   ├── main.py          # Entry point of the application
│   ├── database.py      # Handles DB connection setup
│   ├── models.py        # SQLAlchemy DB models
│   ├── schemas.py       # Pydantic request/response models
│   └── crud.py          # All DB-related logic (CRUD)
├── .env                 # Environment config
├── requirements.txt     # Python packages
```

---

## 🔧 Setup Instructions

### 1️⃣ Environment Configuration

Create a `.env` file in the root directory:

```env
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/Users
```

### 2️⃣ Install Dependencies

```bash
pip install fastapi uvicorn sqlalchemy psycopg2-binary python-dotenv
```

### 3️⃣ Run the App

```bash
uvicorn app.main:app --reload
```

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---

## 🔗 API Endpoints

| Method | Endpoint                    | Description               |
|--------|-----------------------------|---------------------------|
| POST   | `/tasks/`                   | Create a new task         |
| GET    | `/tasks/{task_id}`          | Retrieve a task by ID     |
| PUT    | `/tasks/{task_id}`          | Update a task by ID       |
| DELETE | `/tasks/{task_id}`          | Delete a task by ID       |
| GET    | `/tasks/user/{user_id}`     | Get all tasks for a user  |

---

## 📦 Sample Payloads

### ▶️ Create Task

```json
{
  "title": "Build Task Service",
  "description": "Develop all endpoints for managing tasks",
  "user_id": 1
}
```

### 🔁 Update Task

```json
{
  "title": "Refactor Task Service",
  "description": "Add more test cases and validations"
}
```

---

## 🧱 Optional: Database Migrations with Alembic

```bash
alembic init alembic
alembic revision --autogenerate -m "create tasks table"
alembic upgrade head
```

---

## ✨ Key Highlights

- Modular codebase following separation of concerns
- Secure handling of DB credentials using `.env`
- Built-in validation with Pydantic models
- Auto-generated documentation via Swagger UI

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Author

Crafted with 💻 using FastAPI.
