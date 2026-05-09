<div align="center">

<img src="https://img.shields.io/badge/SmartSupport-Campus%20Maintenance%20Portal-2563EB?style=for-the-badge&logo=tools&logoColor=white" alt="SmartSupport Banner" />

# SmartSupport : Campus Maintenance Ticketing System

**Streamlining campus issue reporting and resolution for students and administrators**

[![Django](https://img.shields.io/badge/Django-092E20?style=flat-square&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?style=flat-square&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)](https://sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

</div>

---

## Overview

SmartSupport is a Django-based campus maintenance portal that bridges the gap between students and facility administrators. Students can instantly report issues  broken fans, damaged benches, faulty equipment  while admins track, verify, and resolve them through a clean dashboard.

> No more lost complaints or ignored maintenance requests. Every issue raised gets tracked to resolution.

---

## Features

| Feature | Description |
|---------|-------------|
|  **Raise Tickets** | Students submit issues with a title, description, and optional photo |
|  **Admin Dashboard** | Centralized view of all submitted tickets for administrators |
|  **Status Tracking** | Tickets flow through **Pending → Accepted → Resolved** stages |
|  **Role-Based Login** | Separate authentication flows for Students and Admins |
|  **Image Upload** | Attach photos to provide better visual context for issues |

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| **Backend** | Django (Python) |
| **Frontend** | HTML, CSS, Bootstrap |
| **Database** | SQLite (Django default) |
| **Authentication** | Django built-in auth system |
| **Media Storage** | Local filesystem (`/media`) |

---

## Project Structure

```
SmartSupport/
│
├── SmartSupport/           # Django project configuration
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── ticket/                 # Core application
│   ├── templates/          # HTML templates
│   ├── static/             # CSS, JS, and static assets
│   ├── models.py           # Ticket data model
│   ├── views.py            # View logic and request handling
│   └── urls.py             # App-level URL routing
│
├── media/                  # User-uploaded images
├── db.sqlite3              # SQLite database
├── requirements.txt
└── manage.py
```

---

## Ticket Lifecycle

```
Student Submits Issue
        │
        ▼
  ┌─────────────┐
  │   PENDING   │  ← Ticket created, awaiting review
  └──────┬──────┘
         │  Admin reviews
         ▼
  ┌─────────────┐
  │  ACCEPTED   │  ← Issue acknowledged, work in progress
  └──────┬──────┘
         │  Issue fixed
         ▼
  ┌─────────────┐
  │  RESOLVED   │  ← Ticket closed
  └─────────────┘
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip

---

### 1. Clone the Repository

```bash
git clone https://github.com/JustCodeIT199/SmartSupport.git
cd SmartSupport
```

### 2. Set Up a Virtual Environment

```bash
python -m venv env

# macOS / Linux
source env/bin/activate

# Windows
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create an Admin Superuser

```bash
python manage.py createsuperuser
```

### 6. Run the Development Server

```bash
python manage.py runserver
```

---

### Access Points

| Role | URL |
|------|-----|
| Student Portal | `http://127.0.0.1:8000/` |
| Admin Panel | `http://127.0.0.1:8000/admin/` |

---

## Screenshots

> _Add screenshots here to showcase the student ticket form, admin dashboard, and status tracking views._

---

## Roadmap

- [ ] Email notifications on ticket status updates
- [ ] Student ticket history and personal dashboard
- [ ] Priority levels (Low / Medium / High / Critical)
- [ ] Admin assignment  assign tickets to specific staff
- [ ] Analytics dashboard (open vs resolved ticket trends)
- [ ] Mobile-responsive UI improvements

---

## Contributing

Contributions are welcome! To get started:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m "Add: your feature description"`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request

Please ensure your code follows Django best practices and includes relevant comments.

---

## Authors

- [@Om Sawant](https://github.com/JustCodeIT199)
- [@Malhar-bhoir](https://github.com/Malhar-bhoir)

---

## License

This project is open-source and available under the [MIT License](LICENSE).

---

<div align="center">

Built with ❤️ to make campus life a little smoother

</div>
