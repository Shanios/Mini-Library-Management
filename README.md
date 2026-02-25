
📚 Mini Library Management API


This is a small Library Management System built using Django, Django REST Framework, SimpleJWT, and SQLite.

The goal of this project is to create a backend system where:

Admin can create users and manage books

Registered users can log in

Users can borrow and return books

Borrow history is recorded

Authentication is handled securely using JWT tokens


Even though the task required only APIs, I also added:

A simple HTML interface for role selection (Admin/User)

A user dashboard

Pagination for books (Bonus feature)



---

🛠 Tech Stack

Django

Django REST Framework

SimpleJWT (JWT Authentication)

SQLite (default database)


Database used: SQLite (as specified in the task)


---

⚙️ How To Run This Project

Make sure Python is installed.

1️⃣ Go to project folder

Open Command Prompt and navigate to:

D:\Task_Submission\library_project


---

2️⃣ Create Virtual Environment

python -m venv venv
venv\Scripts\activate


---

3️⃣ Install Required Packages

If you don’t have a requirements file:

pip install django djangorestframework djangorestframework-simplejwt

(If a requirements.txt exists, use: pip install -r requirements.txt)


---

4️⃣ Apply Migrations

python manage.py makemigrations
python manage.py migrate

This will create the SQLite database file:

db.sqlite3


---

5️⃣ Create Admin User

python manage.py createsuperuser

This admin will:

Create users

Add books

Manage borrow records



---

6️⃣ Start the Server

python manage.py runserver

Project runs at:

http://127.0.0.1:8000/


---

🔐 Important: User Registration Policy

This system does NOT allow public user registration.

Only the Admin can create users via:

http://127.0.0.1:8000/admin/

If a user who is NOT created by the admin tries to log in, they will receive:

No active account found with the given credentials

This ensures controlled access and prevents unauthorized users from entering the system.


---

🔑 Authentication (JWT Based)

Login Endpoint:

POST /login/

Example Request:

{
  "username": "user1",
  "password": "password"
}

Response:

{
  "refresh": "....",
  "access": "...."
}

For accessing protected endpoints, include:

Authorization: Bearer <access_token>

All book and borrow APIs require authentication.


---

📘 API Documentation

📚 Books

Base URL:

/books/

Method	Endpoint	Access

GET	/books/	Authenticated users
POST	/books/	Admin only
GET	/books/<id>/	Authenticated
PUT/PATCH	/books/<id>/	Admin only
DELETE	/books/<id>/	Admin only (if not borrowed)


Book Fields:

id

title

author

isbn

total_copies

available_copies


If any copy of the book is borrowed, it cannot be deleted.

Pagination is enabled for the book list (Bonus feature).


---

📖 Borrow & Return

Base URL:

/borrow/

Method	Endpoint	Description

POST	/borrow/<book_id>/	Borrow a book
POST	/borrow/return/<book_id>/	Return a book
GET	/borrow/my-borrows/	View user borrow history
GET	/borrow/all/	View all borrow records (Admin only)


Rules:

A user cannot borrow the same book twice without returning it.

A book cannot be borrowed if no copies are available.

Returning a book increases available copies.

Admin can return books on behalf of users.

Borrow history is permanently recorded (with borrowed_at and returned_at timestamps).



---

🖥 HTML Interface (Added Enhancement)

Although not required in the task, I added:

Role selection page (/)

User login page

Dashboard page

Interactive borrow system

Book listing with borrow button

Pagination support


This does not interfere with the API architecture.
The backend remains fully REST-based and JWT-protected.


---

👨‍💼 Admin Panel

Accessible at:

/admin/

Admin can:

Create users

Add/edit/delete books

View borrow records

See active vs returned books

Return books manually



---

📌 Project Highlights

✔ JWT-based authentication
✔ Admin-controlled user system
✔ Borrow & return tracking
✔ SQLite database (as required)
✔ Pagination (Bonus feature)
✔ Clean role-based access control
✔ Admin override capability


---

🧠 Final Notes

This project strictly follows:

Controlled user access (no public registration)

Role-based permission management

RESTful API design

Proper inventory handling

Borrow history tracking


Even though a frontend was not required, a minimal HTML interface was added to demonstrate system interaction in a more user-friendly way.
