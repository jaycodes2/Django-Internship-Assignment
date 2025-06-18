# FULL-STACK DJANGO API PLATFORM

This is a powerful Django backend stack featuring:

- Django REST Framework APIs (Public & Protected)  
- Token and Web-based Authentication  
- Celery + Redis background task execution  
- User Registration Email (via Celery)  
- Telegram Bot Integration (collect usernames)

---

## TECH STACK

- Python 3.12  
- Django 5+  
- Django REST Framework  
- Celery with Redis  
- Telegram Bot API  
- SQLite / PostgreSQL (optional for production)

---

## PROJECT SETUP

1. Clone the repo  
   ```bash
   git clone https://github.com/yourusername/myproject.git  
   cd myproject  
   ```

2. Create & activate virtual environment  

   **Windows:**  
   ```bash
   python -m venv venv  
   venv\Scripts\activate  
   ```

   **Ubuntu/macOS:**  
   ```bash
   python3 -m venv venv  
   source venv/bin/activate  
   ```

3. Install requirements  
   ```bash
   pip install -r requirements.txt  
   ```

4. Setup `.env` file  
   Create a `.env` file in the root directory with:

   ```env
   SECRET_KEY=your-django-secret-key  
   DEBUG=True  
   TELEGRAM_BOT_TOKEN=your-telegram-bot-token  
   EMAIL_HOST=smtp.example.com  
   EMAIL_PORT=587  
   EMAIL_USE_TLS=True  
   EMAIL_HOST_USER=your_email@example.com  
   EMAIL_HOST_PASSWORD=yourpassword  
   ```

---

## ENVIRONMENT VARIABLES USED

- `SECRET_KEY` – Django secret key  
- `DEBUG` – True or False  
- `TELEGRAM_BOT_TOKEN` – Telegram bot token  
- `EMAIL_*` – SMTP config for sending emails

---

## HOW TO RUN LOCALLY

1. Run Django server  
   ```bash
   python manage.py migrate  
   python manage.py createsuperuser  
   python manage.py runserver  
   ```

2. Start Redis server  
   - **Windows:** `redis-server`  
   - **Ubuntu:** `sudo service redis-server start`  

3. Start Celery worker  
   ```bash
   celery -A myproject worker --loglevel=info  
   ```

4. Start Telegram bot  
   ```bash
   python api/telegram_bot.py  
   ```

---

## AUTHENTICATION

### TOKEN BASED:
**POST** `/api/token/`  
```json
{
  "username": "youruser",  
  "password": "yourpass"  
}
```

Use returned token in headers:  
`Authorization: Bearer <access_token>`

---

## API ENDPOINTS

| Method | Endpoint              | Description              |
|--------|-----------------------|--------------------------|
| GET    | /api/public/          | Public endpoint          |
| GET    | /api/protected/       | Requires JWT             |
| POST   | /api/register/        | Register user & send mail|
| POST   | /api/token/           | Get JWT token            |
| POST   | /api/token/refresh/   | Refresh access token     |
| GET    | /login/               | Web login                |
| GET    | /logout/              | Logout                   |

---

## CELERY BACKGROUND TASK

Triggered when user registers.  
Sends a welcome email using Celery (async task) and your SMTP credentials.

---

## TELEGRAM BOT

1. Create bot from [@BotFather](https://t.me/BotFather)  
2. Add bot token to `.env` as `TELEGRAM_BOT_TOKEN`  
3. Run it:  
   ```bash
   python api/telegram_bot.py  
   ```

### Behavior:  
On `/start` command, stores user ID, username, and first name to the DB.

---

## FUTURE IMPROVEMENTS

- Admin panel for Telegram users  
- Frontend integration  
- Docker support  
- Telegram webhook instead of polling  
- Advanced logging  

---

## CREDITS

Built by **[Your Name]**  
For educational and testing purposes.