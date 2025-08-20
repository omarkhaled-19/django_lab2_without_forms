# 🛍️ Django Lab2 – Products App (Without Django Forms)

This project is a simple Django application to manage products.  
It demonstrates **CRUD operations** (Create, Read, Delete) with **MySQL** integration, and allows image uploads for products.  

The key difference is that this project is built **without Django Forms** — instead, plain HTML forms and `request.POST`/`request.FILES` are used.

---

## 📖 Table of Contents
1. [Prerequisites](#-prerequisites)  
2. [Project Setup](#-project-setup)  
3. [Database Setup](#-database-setup)  
4. [Django Settings](#-django-settings)  
5. [Apply Migrations](#-apply-migrations)  
6. [Run the Development Server](#-run-the-development-server)  
7. [Media Files Setup](#-media-files-setup)  
8. [Django Admin Setup](#-django-admin-setup)  
9. [Quick Recap](#-quick-recap)  
10. [Notes](#-notes)  

---

## ✅ Prerequisites

Before you begin, make sure the following are installed on your machine:

- **Python 3.8+**  
- **pip** (Python package manager)  
- **MySQL Server** installed and running  

### Python Packages Required:
```bash
pip install django pillow mysqlclient
