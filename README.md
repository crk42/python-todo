# Python Todo App

A simple and robust Todo List web application built with Python and Flask. This application allows users to manage their daily tasks efficiently, with data persisted in a SQLite database.

## Features

- **Add Tasks**: Easily create new tasks to keep track of what needs to be done.
- **View Tasks**: See all your tasks in a clear list view.
- **Real-time Search**: Filter tasks instantly as you type without page reloads.
- **Mark as Complete**: Toggle task completion status using checkboxes - click anywhere on the task text or checkbox.
- **Delete Tasks**: Remove tasks that are no longer needed.
- **Data Persistence**: All changes are saved automatically to a SQLite database (`todo.db`).
- **Modern UI**: Orange-themed interface with smooth animations and responsive design.

## Technologies Used

- **Backend**: Python, Flask
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript, Jinja2 Templates

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
- `algorithms.py`: Implementation of binary search and bubble sort algorithms.
- `main.py`: Entry point to demonstrate algorithm functionality.
- `requirements.txt`: List of Python dependencies.
- `static/`: Directory for static assets like CSS files.
- `templates/`: Directory for HTML templates.
- `test_algorithms.py`: Unit tests for algorithms.
- `test_app.py`: Unit tests for Flask application.
- `todo.db`: SQLite database file (created after running the app).

## Testing

Run the unit tests to validate functionality:
```bash
python -m unittest discover
```

The test suite includes:
- Algorithm tests (binary search, bubble sort)
- Application tests (add, update, delete, search tasks)

## License

This project is open source and available under the [MIT License](LICENSE).
