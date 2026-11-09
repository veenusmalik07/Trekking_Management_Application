# 🏔️ Trekking Management Application (TMA)

A full-stack web application designed to simplify and manage trekking activities, bookings, trek organizers, and staff assignments through a centralized platform.

<img width="1782" height="836" alt="image" src="https://github.com/user-attachments/assets/a85ab76c-6ea3-4990-8087-02f2a42b6df9" />
<img width="1795" height="881" alt="image" src="https://github.com/user-attachments/assets/9428a0f4-515d-4ed4-96bf-293c1574ace0" />
<img width="1777" height="877" alt="image" src="https://github.com/user-attachments/assets/7eafb143-3e6e-4d19-8882-68a8c95cacc7" />
<img width="1792" height="886" alt="image" src="https://github.com/user-attachments/assets/ec9f51a3-5731-4426-b43c-2866cce0a9bc" />
<img width="1786" height="892" alt="image" src="https://github.com/user-attachments/assets/b20c9d2a-42da-4889-839a-352132540ec1" />
<img width="1775" height="892" alt="image" src="https://github.com/user-attachments/assets/752b30b3-d3dd-4462-9221-d802d5891e24" />
<img width="1777" height="892" alt="image" src="https://github.com/user-attachments/assets/29a11634-db48-43f5-a316-ecc4cdf755fe" />
<img width="1790" height="895" alt="image" src="https://github.com/user-attachments/assets/55c42a23-1d20-44c6-ab4d-ffc88e6a955a" />
<img width="1786" height="886" alt="image" src="https://github.com/user-attachments/assets/d6039894-ed90-482f-835b-deb432195e5a" />
<img width="1790" height="887" alt="image" src="https://github.com/user-attachments/assets/871f8409-1fc2-4d03-8934-d14766f3d5a7" />


## 📌 About the Project

The **Trekking Management Application (TMA)** is a web-based platform that helps users discover and book trekking experiences while allowing administrators and trek staff to manage trekking operations efficiently.

The application provides role-based access for three types of users: Admin, Trek Staff, and Customers.

It aims to make trek planning, booking management, and coordination between users and trekking organizers easier and more organized.

## ✨ Key Features

### 👤 User Module
- User registration and login.
- Browse available trekking activities.
- View trek details and requirements.
- Book trekking experiences.
- View booking information.
- Explore trek image galleries.

### 🛠️ Admin Module
- Admin dashboard.
- Manage trekking activities.
- Add, update, and delete trek details.
- Manage user information.
- View and manage bookings.
- Assign staff to trekking activities.
- Manage trek requirements and galleries.

### 🧑‍💼 Trek Staff Module
- Staff login and authentication.
- View assigned trekking activities.
- Access relevant booking information.
- Manage assigned trek responsibilities.

### ⚙️ Additional Features
- JWT-based authentication.
- Role-Based Access Control (RBAC).
- Redis caching for improved performance.
- Celery for background task processing.
- Responsive user interface.
- Trek fitness and age requirements.

## 🧰 Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend development |
| Flask | REST API development |
| Vue.js | Frontend development |
| SQLite | Database management |
| Redis | Caching and message broker |
| Celery | Background task processing |
| Bootstrap | UI styling |
| Jinja2 | Application entry-point templating |
| JWT | Authentication and authorization |

## 🏗️ Application Architecture

The application follows a client-server architecture.

- **Frontend:** Vue.js handles the user interface and interactions.
- **Backend:** Flask provides REST APIs and handles business logic.
- **Database:** SQLite stores application data.
- **Caching:** Redis improves data retrieval performance.
- **Background Processing:** Celery handles asynchronous and scheduled tasks.

## 📂 Project Structure

```text
Trekking-Management-Application/
│
├── backend/
│   ├── app.py
│   ├── models.py
│   ├── celery_config.py
│   ├── tasks.py
│   ├── mails.py
│   ├── schedule.py
│   └── ...
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   ├── views/
│   │   ├── router/
│   │   └── ...
│   ├── public/
│   └── package.json
│
├── instance/
│   └── ...
│
├── requirements.txt
├── README.md
└── .gitignore
```

*Note: Adjust the folder structure above to match your actual repository.*

## 🚀 Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
cd Trekking-Management-Application
```

### 2. Backend Setup

Create and activate a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Start Redis

Make sure Redis is installed and running.

### 4. Start the Flask Backend

```bash
python app.py
```

### 5. Start Celery Worker

```bash
celery -A tasks.celery worker --loglevel=info
```

### 6. Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

## 🔐 Security

- JWT-based user authentication.
- Role-based authorization.
- Protected application routes.
- Secure handling of user credentials.

## 🎯 Project Objectives

- Simplify trekking activity management.
- Provide an organized booking system.
- Improve coordination between administrators, staff, and customers.
- Reduce manual operational tasks.
- Build a scalable and maintainable web application.

## 👩‍💻 Author

**Veenus Malik**

IIT Madras – BS in Data Science

---

⭐ If you find this project interesting, consider giving the repository a star!
