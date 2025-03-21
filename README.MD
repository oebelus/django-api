# Prescription Management Platform

A Django-based platform for physicians to manage people and create prescriptions using a medication database.

## Features
- User authentication for physicians.
- person management (add, update, view).
- Prescription management (create, update, view).
- Medication database integration.
- Search functionality for medications.
- Basic reporting (e.g., prescriptions by person).

## API Endpoints
- Authentication: `/api/login/`, `/api/register/`.
- people: `/api/people/`, `/api/people/<id>/`.
- Medications: `/api/medications/`, `/api/medications/?search=<query>`.
- Prescriptions: `/api/prescriptions/`, `/api/prescriptions/<id>/`.
