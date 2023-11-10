# Flask Task Master Project README

Welcome to the Flask Task Master project! This project is a simple web application for managing your tasks. You can add, view, edit, and mark tasks as done. Below, you'll find information on how to set up and run this project.

## Prerequisites

Before you get started, make sure you have the following installed:

- [Python](https://www.python.org/) (3.6 or higher)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- A modern web browser

## Getting Started

1. Clone this repository to your local machine.
```bash
git clone https://github.com/yourusername/flask-task-master.git
```
2.Navigate to the project directory:
```bash
   cd flask-task-master
```
3.Create a virtual environment (recommended but optional):
```bash
   python3 -m venv venv
   source venv/bin/activate
```
4.Install project dependencies:
```bash
   pip install -r requirements.txt
```
## Running the Application
```bash
   flask run
```
This will start the development server, and you can access the application in your web browser at http://localhost:5000.

## Usage
- Open your web browser and go to http://localhost:5000.
- You will see the Task Master web interface.
- You can add new tasks using the input field and "Add Task" button.
- Existing tasks are displayed in a table, and you can mark them as done or edit them.
- To mark a task as done, click the "Mark done" button.
- To edit a task, click the "Edit" button.
- To delete a task, simply click the "Mark done" button.
## Project Structure
- app.py: The main Flask application.
- models.py: Defines the Todo class for managing tasks in the database.
- templates/index.html: The HTML template for the main page.
- templates/layout.html: The base HTML template.
- static/style.css: The CSS file for styling the application.
- migrations/: Directory containing database migration scripts.
- requirements.txt: List of project dependencies.
## Contributing
If you would like to contribute to this project, please feel free to submit a pull request or open an issue on the project's GitHub repository.

Thank you for using Flask Task Master! If you have any questions or encounter any issues, don't hesitate to reach out. Enjoy managing your tasks with this application!




