# StudyBuddy

A collaborative study platform where students can create topic-based study rooms, engage in discussions, and connect with others learning the same subjects.

---

## Features

- **Study Rooms**: Create, edit, and delete topic-based rooms for focused discussion
- **Real-time Messaging**: Send, edit, and delete messages within any room
- **Topic Filtering**: Browse and filter rooms by topic from the sidebar
- **User Profiles**: View any user's profile, their created rooms, and topics
- **Authentication**: Register, log in, and log out securely
- **Access Control**: Only room hosts can edit or delete their rooms; only message authors can edit or delete their messages
- **Responsive Design**: Clean, minimal UI with light and dark mode support

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.12, Django 6.0 |
| Database | SQLite |
| Frontend | HTML, CSS, Django Templates |
| Authentication | Django built-in auth system |
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
pip install django python-dotenv
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

## Project Structure

```
StudyBuddy/
├── base/                   # Main Django app
│   ├── models.py           # Rooms, Topic, Message models
│   ├── views.py            # All view functions
│   ├── forms.py            # RoomForm, MessageForm
│   └── urls.py             # App-level URL patterns
├── templates/
│   └── base/               # All HTML templates
├── static/                 # CSS files
├── StudyBuddy/             # Project settings
│   ├── settings.py
│   └── urls.py          
├── .gitignore
└── manage.py
```

---

## Usage

1. Register an account or log in
2. Browse existing study rooms on the homepage
3. Filter rooms by topic using the sidebar
4. Click a room to join the discussion
5. Create your own room with a topic and description
6. Edit your profile via the navbar dropdown

