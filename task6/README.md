# Online Course Management API

FastAPI + MySQL + SQLAlchemy + JWT project.

## Current implementation

- MySQL database connection
- SQLAlchemy models for User, Course and Enrollment
- User registration
- Password hashing
- Login
- JWT access token
- Current user API
- Role-based authorization
- Course creation
- Course listing
- Filtering
- Searching
- Sorting
- Pagination
- Course update/PATCH
- Soft delete

## Setup

1. Create MySQL database:

```sql
CREATE DATABASE course_management_db;
```

2. Open `database/connection.py` and replace `YOUR_PASSWORD`.

3. Install packages:

```bash
pip install -r requirements.txt
```

4. Run:

```bash
python -m uvicorn main:app --reload
```

5. Swagger:

`http://127.0.0.1:8000/docs`

## Next modules

- Enrollment APIs
- Admin user APIs
- Admin statistics
- Additional error handling
- Complete testing
