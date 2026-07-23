# TripTrak

TripTrak is a Django-based travel journal application that helps users organize trips and preserve travel memories. Users can create trips, attach notes, upload photos, rate experiences, and manage their travel history through a clean dashboard.

---

## Features

- User authentication
- Create, update and delete trips
- Create travel notes linked to trips
- Upload images for travel memories
- Rate locations and experiences
- Personal dashboard
- Responsive interface built with Tailwind CSS

---

## Tech Stack

- Python
- Django
- SQLite
- Tailwind CSS
- Crispy Forms
- Crispy Tailwind

---

## Project Structure

```
tracktravel/
│
├── config/
├── trip/
├── templates/
├── media/
├── manage.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/yourusername/TripTrak.git
cd TripTrak
```

Create a virtual environment.

```bash
python -m venv env
```

Activate it.

Windows

```bash
env\Scripts\activate
```

Linux/macOS

```bash
source env/bin/activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

Run migrations.

```bash
python manage.py migrate
```

Create an administrator.

```bash
python manage.py createsuperuser
```

Run the development server.

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

## Screenshots

Add screenshots of:

- Landing page
- Login
- Dashboard
- Trip Details
- Notes
- Create Trip
- Create Note

---

## Future Improvements

- Interactive maps
- Search and filtering
- Trip statistics
- Export trips
- Weather integration
- Public trip sharing

---

## License

This project is licensed under the MIT License.