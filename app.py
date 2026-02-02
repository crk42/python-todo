from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
DB_NAME = "todo.db"

def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS todo (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                complete BOOLEAN NOT NULL CHECK (complete IN (0, 1))
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    query = request.args.get('q')
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        if query:
            cursor.execute("SELECT * FROM todo WHERE title LIKE ?", ('%' + query + '%',))
        else:
            cursor.execute("SELECT * FROM todo")
        todos = cursor.fetchall() # Returns list of tuples (id, title, complete)
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add():
    title = request.form.get('title')
    if title:
        with sqlite3.connect(DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("INSERT INTO todo (title, complete) VALUES (?, ?)", (title, False))
            conn.commit()
    return redirect(url_for('index'))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        # First check current status to toggle it
        cursor.execute("SELECT complete FROM todo WHERE id = ?", (todo_id,))
        result = cursor.fetchone()
        if result:
            new_status = not result[0]
            cursor.execute("UPDATE todo SET complete = ? WHERE id = ?", (new_status, todo_id))
            conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todo WHERE id = ?", (todo_id,))
        conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
