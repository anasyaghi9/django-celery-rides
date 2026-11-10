# Django + Celery | Background Tasks & Scheduled Email Notifications

A Django project demonstrating the integration of **Celery and Redis** to handle asynchronous background tasks and scheduled operations using Celery Beat.

The project explores how to offload time-consuming operations from Django's request-response cycle, improving application responsiveness and providing a foundation for scalable background processing.

## 🚀 Technologies Used

- **Python** – Backend programming language.
- **Django** – Web application framework.
- **Celery** – Distributed task queue for asynchronous task execution.
- **Redis** – Message broker for communication between Django and Celery workers.
- **Celery Beat** – Periodic task scheduler.
- **Django Email Backend** – Email delivery integration.

## ✨ Key Features

- **Background Task Processing:** Execute tasks independently of HTTP requests.
- **Asynchronous Email Sending:** Send emails through Celery workers instead of blocking Django views.
- **Periodic Task Scheduling:** Schedule recurring tasks using Celery Beat.
- **Redis Integration:** Use Redis as the message broker.
- **Worker Management:** Configure Celery workers to process queued tasks.

## 🏗️ Project Architecture

The application follows this workflow:

```text
Django Application
       |
       | Dispatch Task
       v
   Redis Broker
       |
       v
  Celery Worker
       |
       v
  Execute Task
       |
       v
   Send Email


    Celery Beat
       |
       | Schedule Periodic Tasks
       v
   Redis Broker
```

## 📂 Project Structure

```text
django-celery-rides/
│
├── django_celery_project/
│   ├── __init__.py
│   ├── celery.py
│   ├── settings.py
│   └── ...
│
├── mainapp/
│
├── send_mail_app/
│   ├── migrations/
│   ├── tasks.py
│   ├── views.py
│   ├── models.py
│   └── ...
│
├── manage.py
└── .gitignore
```

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/anasyaghi9/django-celery-rides.git

cd django-celery-rides
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Linux / macOS:

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install django celery redis
```

### 4. Configure Redis

Make sure Redis is installed and running.

Default Redis broker URL:

```python
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
```

### 5. Configure Email Settings

Configure your email backend and SMTP credentials in Django settings.

Keep sensitive credentials in environment variables rather than committing them to GitHub.

### 6. Apply Migrations

```bash
python manage.py migrate
```

## ▶️ Running the Project

Run each service in a separate terminal.

**Terminal 1 – Start Django:**

```bash
python manage.py runserver
```

**Terminal 2 – Start Celery Worker:**

```bash
celery -A django_celery_project worker -l info --pool=solo
```

**Terminal 3 – Start Celery Beat:**

```bash
celery -A django_celery_project beat -l info
```

> Note: `--pool=solo` is used here for local Windows development. Linux production deployments can use the appropriate worker pool, such as prefork.

## 📚 What I Learned

Through this project, I explored several important backend engineering concepts:

- Understanding Celery architecture and distributed task processing.
- The difference between synchronous and asynchronous execution.
- CPU-bound vs. I/O-bound workloads.
- Concurrency models: Multithreading, Multiprocessing, and Asynchronous Programming.
- Celery execution pools: Prefork, Threads, Solo, and others.
- Worker processes, concurrency configuration, and task execution.
- Message Brokers, Queues, and Result Backends.
- Task States and Worker Management.
- Periodic task scheduling with Celery Beat.
- Integrating background processing into Django applications.

## 🎯 Project Goal

The main goal of this project was to move beyond theoretical understanding and gain practical experience integrating Celery into a Django application, with a focus on background processing, scheduled tasks, and asynchronous email delivery.

---

**Author:** Anas Atallah Yaghi

**GitHub:** [@anasyaghi9](https://github.com/anasyaghi9)

**Repository:** [django-celery-rides](https://github.com/anasyaghi9/django-celery-rides)
