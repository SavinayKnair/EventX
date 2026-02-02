
# TCS iON AIP 135: Real-Time End-to-End Event Management with Automated Build

[![Django](https://img.shields.io/badge/Framework-Django%205.0-green.svg)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Language-Python%203.11+-blue.svg)](https://www.python.org/)
[![Bootstrap](https://img.shields.io/badge/Frontend-Bootstrap%205.3-purple.svg)](https://getbootstrap.com/)

## 👤 Internship Profile
- **Intern Name:** Savinay K
- **Campus ID:** 31437
- **Registration No:** 23BBCDAI181
- **University:** Yenepoya University, Bangalore
- **Project Domain:** Full Stack Web Development (Real-Time Systems)

---

## 🚀 Project: EventX
**EventX** is a high-performance event management solution developed to streamline the lifecycle of community and institutional events. It replaces manual coordination with an automated, admin-moderated digital workflow.



### ✨ Key Features
- **Glassmorphism UI**: A modern, premium interface with blur effects and scroll animations.
- **Role-Based Access**: 
  - **Users**: Can create events, upload images, and track approval status.
  - **Administrators**: Full "Command Center" to approve, reject, or feature events.
- **Dynamic Badge System**: Real-time category tagging (e.g., Marriage, Party, Corporate) displayed on event cards.
- **Real-Time Data Flow**: Instant updates from the user submission form to the Admin Dashboard.
- **Responsive Design**: Fully optimized for mobile, tablet, and desktop viewing.

---

## 🏗️ System Architecture
The project is built using the **Model-View-Template (MVT)** architecture, ensuring a clean separation between data logic, business logic, and the user interface.



### Technical Stack
| Layer | Technology |
| :--- | :--- |
| **Backend** | Python 3.x, Django Framework |
| **Frontend** | HTML5, CSS3 (Custom Glassmorphism), JavaScript (ES6) |
| **Styling** | Bootstrap 5.3, FontAwesome 6, Google Fonts (Outfit) |
| **Database** | SQLite3 (Relational) |
| **Tools** | VS Code, Git/GitHub, Popsy Illustrations |

---

## 📂 Project Structure
```text
event_management_system/
├── core/                  # Project configuration and URL routing
├── events/                # Main application (Models, Views, logic)
├── media/                 # Storage for user-uploaded event banners
├── static/                # Custom CSS animations and JS effects
├── templates/             # Premium HTML templates using DTL
├── Documentation/         # Internship reports and architecture diagrams
├── manage.py              # Django management script
└── requirements.txt       # Automated dependency manifest

```

---

## 🛠️ Installation & Automated Build

Follow these steps to set up the project locally with the automated build process:

1. **Clone the Repository**
```bash
git clone [https://github.com/YOUR_USERNAME/EventX-TCS-iON.git](https://github.com/YOUR_USERNAME/EventX-TCS-iON.git)
cd event_management_system

```


2. **Setup Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
# venv\Scripts\activate  # Windows

```


3. **Install Dependencies** (Automated Build)
```bash
pip install -r requirements.txt

```


4. **Initialize Database**
```bash
python manage.py makemigrations
python manage.py migrate

```


5. **Launch Application**
```bash
python manage.py runserver

```


Access the app at: `http://127.0.0.1:8000/`

---

## 🔐 Security & Validation

* **CSRF Protection**: All forms are secured using Cross-Site Request Forgery tokens.
* **Staff Authentication**: Only authorized staff can access the moderation dashboard.
* **Form Validation**: Server-side validation for date formats and image uploads.

---

## 📝 Conclusion

This project demonstrates a full-stack approach to solving real-world event coordination challenges. By implementing a managed approval workflow, **EventX** ensures content quality and security while providing an elite user experience.

*Submitted as part of the TCS iON Academic Internship Program 2026.*
