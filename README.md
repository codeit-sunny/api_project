# Django REST API CRUD Project

## Overview
This is a simple REST API built using **Django** and **Django REST Framework**.  
It demonstrates **full CRUD operations** (Create, Read, Update, Delete) for managing employees.

---

## Features
- List all employees (GET)  
- Add a new employee (POST)  
- Update existing employee (PUT)  
- Delete an employee (DELETE)  
- JSON responses for all API requests  

---

## Tech Stack
- **Backend:** Django, Django REST Framework  
- **Database:** SQLite (local development)  
- **API Testing:** Postman / Thunder Client  

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/employees/` | Get all employees |
| POST | `/api/create/` | Create a new employee |
| PUT | `/api/update/<id>/` | Update an existing employee |
| DELETE | `/api/delete/<id>/` | Delete an employee |

---

## Installation
1. Clone the repo:
```bash
git clone https://github.com/your-username/django-rest-api.git
