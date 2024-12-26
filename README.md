# Student Management Application

This Django-based application provides a management system for student functionalities, including user registration, login, dashboard access, exam management, and result viewing.

## Features

- **User Registration and Login**: Students can register and log in to access their personalized dashboard.
- **Student Dashboard**: Displays key metrics, such as the total number of courses and questions available.
- **Exam Management**: Students can view available exams, start an exam, and answer questions.
- **Result Management**: Students can view and check their exam results.

---

## Code Structure

### URLs Configuration (`urls.py`)
The `urlpatterns` defines the routing for the application:

- **Authentication**:
  - `/studentlogin`: Login view for students.
  - `/studentsignup`: Registration view for students.

- **Dashboard and Exams**:
  - `/student-dashboard`: Displays student dashboard with total courses and questions.
  - `/student-exam`: Lists available exams for students.
  - `/take-exam/<int:pk>`: Prepares a student to take an exam for the selected course.
  - `/start-exam/<int:pk>`: Starts the selected exam and presents questions to the student.

- **Result Management**:
  - `/calculate-marks`: Calculates the marks obtained by the student after an exam.
  - `/view-result`: Displays all available results.
  - `/check-marks/<int:pk>`: Checks marks for a specific course.
  - `/student-marks`: Displays the marks overview for the student.

### Views (`views.py`)
The `views.py` file handles the business logic and user interface rendering:

1. **Authentication and Navigation**:
   - `studentclick_view`: Handles navigation for unauthenticated users.
   - `student_signup_view`: Manages student registration.

2. **Dashboard and Exams**:
   - `student_dashboard_view`: Displays metrics for logged-in students.
   - `student_exam_view`: Lists available courses and exams.
   - `take_exam_view`: Prepares the student to take an exam.
   - `start_exam_view`: Starts the exam and displays questions.

3. **Result Calculation and Display**:
   - `calculate_marks_view`: Computes marks based on student responses.
   - `view_result_view`: Shows all exam results for a student.
   - `check_marks_view`: Displays marks for a specific course.
   - `student_marks_view`: Lists overall marks for the student.

### Models (`models.py`)
The `Student` model extends the `User` model to include:

- Address
- Mobile Number

It provides methods to retrieve the full name of a student and a string representation.

### Forms (`forms.py`)
Defines two forms:

- `StudentUserForm`: Captures user details (first name, last name, username, and password).
- `StudentForm`: Captures additional student-specific details (address, mobile number).

---

## Setup and Installation

### Prerequisites
- Python 3.x
- Django 3.x or later
- A database system (SQLite is used by default in Django)

### Steps

1. Clone the repository.
   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory.
   ```bash
   cd student_management_app
   ```

3. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations.
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server.
   ```bash
   python manage.py runserver
   ```

6. Access the application at `http://127.0.0.1:8000/`.
