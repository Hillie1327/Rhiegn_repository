# 🎯 Hillie Rhiegn Batan Django Portfolio

> A personal portfolio web application built with Django — showcasing projects, skills, and professional experience.

---

---

## 🚀 Features

- **Dynamic Project Showcase** — Add, edit, and manage projects via Django Admin
- **Skills Section** — Display technologies and proficiency levels
- **Contact Form** — Email integration for visitor messages
- **Responsive Design** — Mobile-first layout
- **SEO Ready** — Meta tags and Open Graph support
- **Admin Dashboard** — Full CMS via Django's built-in admin

---

## 🛠 Tech Stack

| Layer      | Technology              |
|------------|-------------------------|
| Backend    | Python 3.11+, Django 4.x |
| Database   | PostgreSQL (prod) / SQLite (dev) |
| Frontend   | HTML5, CSS3, JavaScript |
| Styling    | Bootstrap 5 / Tailwind CSS |
| Deployment | Railway / Render / Heroku |
| Storage    | AWS S3 / Cloudinary (media files) |

---

## 📁 Project Structure

```
Reyn_project/
│
├── Reyn_project/               # Main Django project
│   ├── settings
│   ├── urls.py
│   └── wsgi.py
│
├── Reyn_app/
│   ├── core/                # Home, About pages
│   ├── projects/            # Project listings and detail
│   ├── skills/              # Skills and technologies
│   └── contact/             # Contact form + email
│
├── templates/               # HTML templates
│   ├── indexh.html
│
├── static/                  # CSS, JS, images
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/                   # User-uploaded files
├── requirements/
│   ├── base.txt
│   ├── development.txt
│   └── production.txt
│
├── .env.example
├── manage.py
└── README.md
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.11+
- pip
- virtualenv or venv
- PostgreSQL (for production)

---

### 1. Clone the Repository

```bash
git clone https://github.com/Hillie1327/Rhiegn_repository.git
cd Rhiegn-reposiory
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS/Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DATABASE_URL=sqlite:///db.sqlite3

# Email settings (for contact form)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=your-app-password

# Optional: Cloudinary for media
CLOUDINARY_URL=cloudinary://...
```

### 5. Run Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser

```bash
python manage.py createsuperuser
```

### 7. Load Sample Data (Optional)

```bash
python manage.py loaddata fixtures/sample_data.json
```

### 8. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)  
Admin: [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 🗄️ Database Models

### Project

```python
class Project(models.Model):
    title        = models.CharField(max_length=200)
    description  = models.TextField()
    tech_stack   = models.ManyToManyField('Skill')
    github_url   = models.URLField(blank=True)
    live_url     = models.URLField(blank=True)
    thumbnail    = models.ImageField(upload_to='projects/')
    featured     = models.BooleanField(default=False)
    created_at   = models.DateTimeField(auto_now_add=True)
```

### Skill

```python
class Skill(models.Model):
    name         = models.CharField(max_length=100)
    icon         = models.CharField(max_length=50)   # e.g. 'fa-python'
    proficiency  = models.IntegerField(default=80)   # percentage
    category     = models.CharField(max_length=50)   # e.g. 'Backend'
```

### ContactMessage

```python
class ContactMessage(models.Model):
    name         = models.CharField(max_length=100)
    email        = models.EmailField()
    subject      = models.CharField(max_length=200)
    message      = models.TextField()
    sent_at      = models.DateTimeField(auto_now_add=True)
    is_read      = models.BooleanField(default=False)
```

---

## 🌐 Deployment

### Deploy to Render

1. Push your code to GitHub
2. Create a new **Web Service** on [Render](https://render.com)
3. Set environment variables in the Render dashboard
4. Set build command:
   ```bash
   pip install -r requirements/production.txt && python manage.py migrate
   ```
5. Set start command:
   ```bash
   gunicorn portfolio.wsgi:application
   ```

### Deploy to Railway

```bash
railway login
railway init
railway up
```

### Collect Static Files (Before Deploy)

```bash
python manage.py collectstatic --noinput
```

---

## 🧪 Running Tests

```bash
python manage.py test
```

With coverage:

```bash
pip install coverage
coverage run manage.py test
coverage report
```

---

## 🔒 Security Checklist (Production)

- [ ] `DEBUG = False`
- [ ] `SECRET_KEY` stored in environment variable
- [ ] `ALLOWED_HOSTS` properly configured
- [ ] HTTPS enforced (`SECURE_SSL_REDIRECT = True`)
- [ ] Static and media files served via CDN
- [ ] Database credentials not hardcoded
- [ ] `CSRF_COOKIE_SECURE = True`
- [ ] `SESSION_COOKIE_SECURE = True`

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

**Your Name**  
📧 hillierhiegnbatan@email.com  
🌐 [hillierhiengnbatan.com](https://hillierhiengnbatan.com)  
💼 [LinkedIn](https://linkedin.com/in/yourprofile)  
🐙 [GitHub](https://github.com/Hillie)

---

<p align="center">Made with ❤️ and Django</p>
