# Personal-expense-tracker
The Expense Tracker Dashboard is a web application designed to help users monitor and manage their personal finances. It allows users to record expenses, set monthly spending limits, and analyze spending patterns through various summaries. The user-friendly interface ensures effective budgeting and financial planning.

## Features
- Add new expenses with categories and descriptions.
- View past expenses and categorize them.
- View monthly summaries of expenses.
- Set a monthly spending limit.
- User-friendly and colorful interface.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Technologies Used
- *Backend*: Python, Django
- *Frontend*: HTML, CSS (Tailwind CSS), JavaScript
- *Database*: SQLite (default for Django)
- *Version Control*: Git & GitHub

## Installation
Follow these steps to set up the Personal Expense Tracker app on your local machine.

### 1. Clone the Repository
First, clone the repository to your local machine.

```bash
git clone https://github.com/Chandanabl9/Personal-expense-tracker.git

2. Install Dependencies
Navigate to the project directory and create a virtual environment.
Create and activate a virtual environment

cd Personal-expense-tracker
python -m venv venv
source venv/bin/activate 
 # On Windows use 'venv\Scripts\activate'

Install the required Python dependencies
pip install -r requirements.txt

If the requirements.txt file does not exist, you can create it with:
pip freeze > requirements.txt

Ensure that django and any other required packages (like djangorestframework, mysqlclient, or psycopg2 for MySQL/PostgreSQL) are listed.

3. Set up the Database
Django uses SQLite by default

4. Apply Migrations
Run Django's migration command to set up the database schema.
python manage.py migrate

Follow the prompts to set the username, email, and password.
6. Start the Development Server
Run the Django development server:
python manage.py runserver
This will start the server at http://127.0.0.1:8000/.

Usage
Once the application is running, follow these steps to interact with the app:

1. Sign Up:

Create a new user account by providing basic information.

2. Login:

Use your credentials to log in.

3. Add Expenses:

Record new expenses with categories and descriptions.

4. View Expenses:

View your past expenses and categorize them.

5. Monthly Summary:

Analyze your expenses for the current month.

6. Set Monthly Limit:

Set a limit for your monthly expenses to help manage your budget.

Contributing

If you would like to contribute to this project, feel free to fork the repository and submit pull requests. Here's how you can contribute:

1. Fork the repository.

2. Create a new branch (git checkout -b feature-branch).

3. Make your changes and commit them (git commit -m 'Add new feature').

4. Push to the branch (git push origin feature-branch).

5. Submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.

### Instructions for Usage:
- Replace the clone URL with the actual repository URL if it's different.
- Update the requirements.txt file if additional dependencies are required for the Django project.
- Follow the steps for database setup depending on the database you're using (SQLite, MySQL, or PostgreSQL).
