# D7 Admin Machine Test

This is a Django-based admin dashboard project with user and partner management.

## Prerequisites
- Python 3.8+
- pip
- (Recommended) Virtualenv or venv

## Setup Instructions

### 1. Clone the Repository
```
git clone <your-repo-url>
cd d7_admin
```

### 2. Create and Activate Virtual Environment

#### On Linux/macOS:
```
python3 -m venv env
source env/bin/activate
```

#### On Windows (cmd):
```
python -m venv env
env\Scripts\activate
```

#### On Windows (PowerShell):
```
python -m venv env
.\env\Scripts\Activate.ps1
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

### 4. Apply Migrations
```
python manage.py migrate
```

### 5. Create Superuser
```
python manage.py createsuperuser
```
Follow the prompts to set username, email, and password.

### 6. Run the Development Server
```
python manage.py runserver
```

Visit [http://localhost/](http://localhost/) in your browser.

### 7. Access the Admin Panel
Go to [http://localhost/admin/](http://localhost/admin/) and log in with your superuser credentials.


## Notes
- Static files are in `static/`
- Templates are in each app's `templates/` folder
- For any issues, ensure your virtual environment is activated and all migrations are applied.

---

Feel free to modify and extend this project as needed!
