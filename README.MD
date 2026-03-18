# StudyBuddy

A collaborative study platform where students can create topic-based study rooms, engage in discussions, and connect with others learning the same subjects.

---

## Features

- **Study Rooms**: Create, edit, and delete topic-based rooms for focused discussion
- **Real-time Messaging**:  Send, edit, and delete messages within any room
- **Topic Filtering**: Browse and filter rooms by topic from the sidebar
- **User Profiles**:  View any user's profile, their created rooms, and topics
- **Authentication**: Register and log in using email and password via a custom user model
- **Avatar Support**: Upload and display profile pictures
- **REST API**: Expose room data via a dedicated API using Django REST Framework
- **Access Control**: Only room hosts can edit or delete their rooms; only message authors can edit or delete their messages
- **Responsive Design**: Clean, minimal UI with light and dark mode support

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.12, Django 6.0 |
| Database | SQLite |
| Frontend | HTML, CSS (custom), Django Templates |
| Authentication | Custom User model (AbstractUser): email & password login |
| API | Django REST Framework (DRF) |
| Media | Pillow : avatar image uploads |
| Environment | Anaconda (conda env: unity) |

---

## Installation & Setup

### Prerequisites

- Python 3.10+
- pip or conda

### 1. Clone the repository

```bash
git clone https://github.com/16A9DA/studybuddy.git
cd studybuddy
```

### 2. Create and activate a virtual environment

```bash
# Using conda
conda create -n studybuddy python=3.12
conda activate studybuddy

# Or using venv
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows
```

### 3. Install dependencies

```bash
pip install django djangorestframework Pillow
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Create a superuser (optional)

```bash
python manage.py createsuperuser
```

### 6. Run the development server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` in your browser.

---

## Project Structure

```
StudyBuddy/
├── base/                   # Main Django app
│   ├── models.py           # User (custom), Rooms, Topic, Message models
│   ├── views.py            # All view functions
│   ├── forms.py            # RoomForm, MessageForm, UserForm
│   └── urls.py             # App-level URL patterns
├── api/                    # REST API app
│   ├── views.py            # API view functions
│   ├── serializers.py      # DRF serializers
│   └── urls.py             # API URL patterns
├── templates/
│   └── base/               # All HTML templates
├── static/                 # CSS files
├── media/                  # User uploaded files (not committed)
│   └── avatars/            # Profile pictures
├── StudyBuddy/             # Project settings
│   ├── settings.py
│   └── urls.py
├── .gitignore
└── manage.py
```

---

## API Endpoints

The project includes a REST API built with Django REST Framework.

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/` | List all available API routes |
| GET | `/api/rooms/` | Return all study rooms |
| GET | `/api/rooms/:id/` | Return a single room by ID |

### Example Response — `/api/rooms/`

```json
[
  {
    "id": 1,
    "name": "Python Study Room",
    "topic": "Python",
    "host": "rayyan",
    "description": "Let's learn Python together"
  }
]
```

---

## Custom User Model

This project uses a custom user model that extends Django's `AbstractUser`:

- Login is handled via **username and password**
- Users can upload a **profile avatar**
- Additional fields: `bio`, `avatar`, `name`

```python
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    bio    = models.TextField(null=True, blank=True)
    name   = models.CharField(max_length=200, null=True, blank=True)
```

---

## Usage

1. Register an account or log in
2. Browse existing study rooms on the homepage
3. Filter rooms by topic using the sidebar
4. Click a room to join the discussion
5. Create your own room with a topic and description
6. Edit your profile via the navbar dropdown

---

## Preview 

https://studdybuddy-production-a2ca.up.railway.app/

---

## License

This project is for educational purposes.