#  Hospital Management System API

A RESTful Hospital Management System built using **FastAPI**, **SQLAlchemy**, and **SQLite** with JWT Authentication and Role-Based Access Control.

---

##  Features

### Authentication
- User Registration
- User Login
- JWT Authentication
- Password Hashing using bcrypt

### Role-Based Access Control
- Admin
- Doctor
- Patient

### Patient Management
- Create Patient
- Get All Patients
- Get Patient by ID
- Update Patient
- Delete Patient
- Search Patients
- Pagination

### Doctor Management
- Create Doctor
- Get All Doctors
- Get Doctor by ID
- Update Doctor
- Delete Doctor

### Appointment Management
- Book Appointment
- View Appointments
- Update Appointment
- Cancel Appointment

### Prescription Management
- Create Prescription
- View Prescriptions
- Update Prescription
- Delete Prescription

### Additional Features
- SQLAlchemy ORM Relationships
- Logging
- Global Exception Handling
- Unit Testing using pytest
- Environment Variables (.env)

---

#  Technologies Used

- Python 3.9
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic
- JWT (python-jose)
- Passlib (bcrypt)
- pytest
- Uvicorn
- python-dotenv

---

#  Project Structure

```
hms_project/
│
├── app/
│   ├── core/
│   ├── db/
│   ├── dependencies/
│   ├── models/
│   ├── routers/
│   ├── schemas/
│   ├── services/
│   └── main.py
│
├── tests/
├── .env
├── pytest.ini
├── requirements.txt
└── README.md
```

---

#  Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/hospital-management-system.git

cd hospital-management-system
```

---

## Create Virtual Environment

### macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Environment Variables

Create a `.env` file:

```env
DATABASE_URL=sqlite:///./hms.db
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## Run the Application

```bash
python -m uvicorn app.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

#  Authentication

1. Register a user.
2. Login using `/auth/login`.
3. Copy the JWT access token.
4. Click **Authorize** in Swagger.
5. Enter:

```
Bearer <your_token>
```

6. Access protected APIs.

---

# Running Tests

Run all unit tests:

```bash
pytest
```

Expected output:

```
3 passed
```

---

#  API Endpoints

## Authentication

| Method | Endpoint |
|---------|----------|
| POST | /auth/login |

---

## Users

| Method | Endpoint |
|---------|----------|
| POST | /users/register |

---

## Patients

| Method | Endpoint |
|---------|----------|
| POST | /patients/ |
| GET | /patients/ |
| GET | /patients/search |
| GET | /patients/{id} |
| PUT | /patients/{id} |
| DELETE | /patients/{id} |

---

## Doctors

| Method | Endpoint |
|---------|----------|
| POST | /doctors/ |
| GET | /doctors/ |
| GET | /doctors/{id} |
| PUT | /doctors/{id} |
| DELETE | /doctors/{id} |

---

## Appointments

| Method | Endpoint |
|---------|----------|
| POST | /appointments/ |
| GET | /appointments/ |
| GET | /appointments/{id} |
| PUT | /appointments/{id} |
| DELETE | /appointments/{id} |

---

## Prescriptions

| Method | Endpoint |
|---------|----------|
| POST | /prescriptions/ |
| GET | /prescriptions/ |
| GET | /prescriptions/{id} |
| PUT | /prescriptions/{id} |
| DELETE | /prescriptions/{id} |

---

# API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Open:

```
http://127.0.0.1:8000/docs
```

---

#  Future Improvements

- PostgreSQL Support
- Docker
- Alembic Database Migrations
- Email Notifications
- File Uploads
- Deployment to Render or Railway

---

#  Author

Developed by **Sushitha Abhilash**

Backend Developer | Python | FastAPI | SQLAlchemy