# Test Task for ANC Company

# Installation

1. Clone the repository:

* Clone with SSH run: `git clone https://github.com/Danil1994/ANC_test_tsak.git`
* Clone with HTTPS run: `git clone git@github.com:Danil1994/ANC_test_tsak.git`

2. Navigate to your project folder: `path/to/the/anc_test_task`.
3. Load your environment variables:
4. Create a .env file based on .env.example.
5. Provide all the required information such as passwords, secret keys, etc.
6. Activate your virtual environment.
7. Install requirements run `pip install -r requirements.txt`.

8. Database configuration:
   By default, this project uses SQLite.
   If you want to use another database, configure your database settings in settings.py.
9. Run migrations : python manage.py migrate.
10. Create fake data run ` python -m main_app.create_fake_data` and take a cup of coffee it`s take great time :)

## Run

1. Run server: `python manage.py runserver`
2. Go to link `http://localhost:8000` in your browser.

# Usage

This web application helps you manage your staff information effectively.

* Authentication:

Before accessing the main features, users must either log in or sign up.

* Main Page:
  The main page provides a brief introduction to the web application.

* Top Management:
  Displays a hierarchical tree structure of your employees.
  Top-level managers are shown first, followed by their subordinates.
  Clicking on an employee's name reveals their subordinates.
* Employee List:
  Shows comprehensive information about all employees, including first name, last name, manager, email, etc.
  Allows sorting the table by clicking on column headers.
  Provides the option to create a new employee.

* Employee Details(click on the employee in the list):
  Shows detailed information about a specific employee.
  Allows updating or deleting employee information.

All info about commit contain in the 'dev' branch. 'master' branch has only main commits.