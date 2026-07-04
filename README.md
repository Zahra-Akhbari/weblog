# Django Weblog

A simple and modern blog application built with **Django** and **Bootstrap 5**. This project demonstrates authentication, CRUD operations, categories, tags, comments, search, image upload, and pagination.

---

## Features

* User Registration & Login
* Authentication System
* Create, Read, Update and Delete (CRUD)
* Categories
* Tags
* Comments System
* Search Posts
* Pagination
* Image Upload
* Bootstrap 5 Responsive UI
* Dashboard for Authors
* Django Messages Framework
* Permission-based Access Control

---

## Technologies Used

* Python
* Django
* SQLite
* Bootstrap 5
* HTML5
* CSS3

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Zahra-Akhbari/weblog.git
```

Go to the project directory:

```bash
cd weblog
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Apply migrations:

```bash
python manage.py migrate
```

Create a superuser:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open your browser:

```
http://127.0.0.1:8000/
```

---

## Project Structure

```
weblog/
│
├── blog/
├── config/
├── media/
├── static/
├── templates/
├── manage.py
└── requirements.txt
```


## Future Improvements

* Django REST Framework API
* User Profile
* Rich Text Editor
* Like & Bookmark System
* Deployment

---

## Author

Developed by Nazanin Zahra
