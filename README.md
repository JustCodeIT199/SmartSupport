# SmartSupport 🎓🛠️

SmartSupport is a Django-based web application designed to simplify the process of reporting and managing campus maintenance issues. Students can raise tickets (e.g., broken fan, damaged bench), and admins can verify, update, and resolve them efficiently.

## 🔧 Features

- 🎫 **Raise Tickets**: Students can submit issues with title, description, and optionally attach an image.
- 📋 **Ticket Dashboard**: Admins can view all submitted tickets.
- ✅ **Status Tracking**: Tickets move through statuses: *Pending*, *Accepted*, *Resolved*.
- 🔐 **Login System**: Separate login for Admin and Student.
- 📷 **Image Upload**: Students can upload photos to provide better issue context.

## 🚀 Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite (Default Django DB)
- **Authentication**: Django built-in auth system

## 📁 Project Structure

SmartSupport/
├── SmartSupport/           # Django project settings
├── ticket/                 # Main app handling tickets
│   ├── templates/          # HTML templates
│   ├── static/             # CSS/JS/Images
│   ├── models.py           # Ticket model
│   ├── views.py            # View logic
│   └── urls.py             # App URLs
├── media/                  # Uploaded images
├── db.sqlite3              # SQLite database
└── manage.py

🧪 How to Run Locally
Clone the repository
git clone https://github.com/JustCodeIT199/SmartSupport.git
cd SmartSupport

Set up a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate  
# On Windows: env\Scripts\activate

Install dependencies
pip install -r requirements.txt

Apply migrations
python manage.py makemigrations
python manage.py migrate

Create a superuser for admin access
python manage.py createsuperuser

Run the server
python manage.py runserver

Access the site
Student Page: http://127.0.0.1:8000/
Admin Panel: http://127.0.0.1:8000/admin/

📸 Screenshots


✍️ Author
JustCodeIT199

🤝 Contributing
Pull requests are welcome! If you have ideas to improve the app, feel free to fork and contribute.

📜 License
This project is open-source under the MIT License.









