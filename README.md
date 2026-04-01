# University Integration Platform

This project is a mini integration system built using the Django framework and Django REST Framework (DRF) to simulate real-world system-to-system communication. It implements a Hub-and-Spoke architecture to connect three distinct subsystem modules:

### Features
- **Student App:** Manages core student profiles and information.
- **Library App:** Tracks library records and unpaid fines.
- **Payment App:** Records tuition payment transactions.
- **Integration Hub:** Acts as a central router that consumes and consolidates the individual APIs into a singular profile summary, demonstrating Data Transformation and Message Routing patterns.

## Guide To Run
To run the system locally, do the following.
> - **Clone this repository** or download it as a **ZIP file.**
> - When cloning the repository, follow these steps.

### 1. Install Python
- You can get it from here. [Python.org](https://www.python.org/)

### 2. Setting up the Backend
Navigate to the backend directory and run the Django development server:

```bash
# Navigate to the correct directory containing manage.py
cd university_integration

# (Optional but recommended) Create and activate a virtual environment
python -m venv venv

# On Windows:
venv\Scripts\activate

# Install the required frameworks for this project
pip install django djangorestframework

# Run the database migrations to set up the SQLite tables
python manage.py migrate

# Start the development server
python manage.py runserver
```

The backend should now be running at `http://127.0.0.1:8000/`.

### 3. Available Endpoints
To view the data, append any of the following to your localhost URL:

- **Students API:** `/api/students/`
- **Library API:** `/api/library/`
- **Payments API:** `/api/payments/`
- **Integration Hub Summary:** `/api/hub/student-summary/<student_id>/`


### Acknowledgment  
We are grateful to our instructors for their guidance and support throughout the development of this project. 

This work reflects my learning journey as a programmer

## Disclaimer 
<div align="center"> 
  I do not own the images, names, information or references included in this project they are used purely as placeholders. <br> 
  All trademarks, service marks, trade names, and other intellectual property rights belong to their respective owners.  <br><br>

  Made with 💗 by <a href="https://github.com/lurxdel"><strong>Lurxdel</strong></a>
</div>
