To-Do App

A full-featured To-Do List Application built using Python, Django. This project allows users to manage their tasks efficiently with features like task creation, scheduling, automatic rollover and notifications.

---

Features

Create, update, delete tasks
Priority tagging (High, Medium, Low)
View all, completed, and pending tasks

---

Tech Stack

Backend: Django, Django REST Framework
Frontend: HTML, CSS
Database: SQLite 
Tools: Git, GitHub, VS Code


Getting Started
1. Clone the repo

git clone https://github.com/Ramya-Viswanath/to-do-app.git
cd to-do-app

2. Set up virtual environment

python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

3. Run migrations

python manage.py makemigrations
python manage.py migrate

4. Run the server

python manage.py runserverv

📄 License
This project is open-source and available under the MIT License.

Author
Ramya Viswanath
📧 ramya.viswanath99@gmail.com
🌐 GitHub - @Ramya-Viswanath


Project Structure

todoproject: Django project settings and root URL configuration

tasks app: Main application logic for managing to-do tasks

templates: HTML templates for rendering UI

static:	CSS styling used in templates

manage.py:	Tool to run and manage your Django project

db.sqlite3:	Local database (automatically created)
