<img width="1920" height="1080" alt="Screenshot 2026-10-08 120255" src="https://github.com/user-attachments/assets/092f156a-c2cb-4639-8f78-3b2028f4bc1f" />
<img width="1920" height="1080" alt="Screenshot 2026-10-08 120308" src="https://github.com/user-attachments/assets/d3767bde-7d24-494a-8c85-db86a98d5fbd" />

# Online Course Management API

A RESTful Online Course Management API built using **FastAPI, MySQL, SQLAlchemy, Pydantic, and JWT Authentication**.

The API supports user authentication, role-based authorization, course management, student enrollment, and admin operations.

---

## 1. Technologies Used

- Python
- FastAPI
- MySQL
- SQLAlchemy
- Pydantic
- JWT Authentication
- Passlib
- Bcrypt
- Uvicorn
- PyMySQL
- Swagger UI

---

## 2. User Roles

The application supports three roles:

- **Admin**
- **Instructor**
- **Student**

Each role has different permissions.

### Admin
- Manage users
- Activate/deactivate users
- Create, update and delete courses
- View all enrollments
- View statistics

### Instructor
- Create courses
- View courses
- Update own courses
- Delete own courses
- View enrollments for own courses

### Student
- View courses
- Enroll in courses
- View enrolled courses
- Access authenticated APIs

---

## 3. Project Structure

```text
course_management/
│
├── main.py
├── requirements.txt
├── README.md
│
├── database/
│   ├── __init__.py
│   ├── connection.py
│   └── models.py
│
├── schemas/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
│
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   ├── course.py
│   ├── enrollment.py
│   └── admin.py
│
├── services/
│   ├── __init__.py
│   ├── auth.py
│   ├── user.py
│   ├── course.py
│   └── enrollment.py
│
├── dependencies/
│   ├── __init__.py
│   └── auth.py
│
└── utils/
    ├── __init__.py
    ├── password.py
    └── jwt.py
```

---

## 4. Database Configuration

Create the MySQL database:

```sql
CREATE DATABASE course_management_db;
```

Update the database connection in:

```text
database/connection.py
```

Example:

```python
DATABASE_URL = "mysql+pymysql://root:YOUR_PASSWORD@localhost/course_management_db"
```

Replace:

```text
YOUR_PASSWORD
```

with your MySQL password.

The application automatically creates the required tables when the application starts.

---

## 5. Database Tables

### Users

```text
user_id
name
email
password_hash
role
is_active
created_at
updated_at
```

### Courses

```text
course_id
title
description
category
price
instructor_id
is_active
created_at
updated_at
```

### Enrollments

```text
enrollment_id
student
