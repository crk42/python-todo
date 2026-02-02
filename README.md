# Python Todo App

A simple and robust Todo List web application built with Python and Flask. This application allows users to manage their daily tasks efficiently, with data persisted in a SQLite database.

## Features

- **Add Tasks**: Easily create new tasks to keep track of what needs to be done.
- **View Tasks**: See all your tasks in a clear list view.
- **Mark as Complete**: Toggle the status of tasks between complete and incomplete.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Data Persistence**: All changes are saved automatically to a SQLite database (`todo.db`).

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, Jinja2 Templates

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd python-todo
    ```

2.  **Install dependencies:**
    It is recommended to use a virtual environment.
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```

2.  **Access the app:**
    Open your web browser and navigate to `http://127.0.0.1:5000`.

3.  **Database initialization:**
    The application will automatically check for and create the `todo.db` database and necessary tables on the first run.

## Project Structure

- `app.py`: The main Flask application file containing routes and database logic.
- `requirements.txt`: List of Python dependencies.
- `static/`: Directory for static assets like CSS and JavaScript files.
- `templates/`: Directory for HTML templates.
- `todo.db`: SQLite database file (created after running the app).

## License

This project is open source and available under the [MIT License](LICENSE).
