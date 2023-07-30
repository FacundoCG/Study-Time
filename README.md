# Study Time

Study Time is a powerful planner designed to help you manage your time effectively, making it the ideal tool for students attending classes or working on assignments. With Study Time, you can effortlessly keep track of your formal hours (class hours) and informal hours (homework or self-study time), ensuring that you stay organized and make the most of every moment.

## Features

- Create records of your study sessions.
- Sign up users and manage user authentication.
- Login and logout users securely.
- Edit and delete study records to maintain accuracy.
- Filter study records by month or year for easy review.

## Technologies Used

- Django
- Python
- CSS
- Bootstrap
- HTML

## Database

Study Time utilizes SQLite as its database, ensuring secure and efficient data storage for your tasks and user information.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required packages from `requirements.txt` using the following command: pip install -r requirements.txt
4. Set up your SQLite database with the necessary configurations.
5. Run the migration to set up the database schema: python manage.py migrate
6. Start the development server: python manage.py runserver
7. Access the application by navigating to `http://localhost:8000/` in your web browser.

## Notes

- Study Time extensively utilizes Django's class-based views to provide an organized and maintainable codebase. The project also leverages Django's powerful authentication functionalities to ensure secure user accounts.
- Create a user account to access all the features of Study Time.


Feel free to explore the code and contribute to the development of Study Time. Happy studying! 📅📚

**Website Link:** [https://studytime.pythonanywhere.com/](https://studytime.pythonanywhere.com/)
