import unittest
import os
import sqlite3
import app

class TestTodoApp(unittest.TestCase):

    def setUp(self):
        # Configure app to use a test database
        app.DB_NAME = "test_todo.db"
        self.app = app.app.test_client()
        self.app.testing = True

        # Initialize the test database
        app.init_db()
        # Ensure clean state
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM todo")
            conn.commit()

    def tearDown(self):
        # Close database connections and remove the test database file
        if os.path.exists(app.DB_NAME):
            try:
                os.remove(app.DB_NAME)
            except PermissionError:
                # On Windows, file might still be locked. 
                # We ensure clean state in setUp, so this is ensuring we don't leave junk.
                pass

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'My Tasks', response.data)

    def test_add_todo(self):
        response = self.app.post('/add', data=dict(title='Test Task'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Test Task', response.data)

        # Verify it's in the database
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todo WHERE title = ?", ('Test Task',))
            task = cursor.fetchone()
            self.assertIsNotNone(task)
            self.assertEqual(task[1], 'Test Task')
            self.assertEqual(task[2], 0) # Not completed

    def test_update_todo(self):
        # Add a task first
        self.app.post('/add', data=dict(title='Task to Update'), follow_redirects=True)
        
        # Get its ID
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM todo WHERE title = ?", ('Task to Update',))
            task_id = cursor.fetchone()[0]

        # Toggle complete
        response = self.app.get(f'/update/{task_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
        # Verify it's completed in DB
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT complete FROM todo WHERE id = ?", (task_id,))
            completed = cursor.fetchone()[0]
            self.assertTrue(completed)

    def test_delete_todo(self):
        # Add a task first
        self.app.post('/add', data=dict(title='Task to Delete'), follow_redirects=True)
        
        # Get its ID
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM todo WHERE title = ?", ('Task to Delete',))
            task_id = cursor.fetchone()[0]

        # Delete it
        response = self.app.get(f'/delete/{task_id}', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Task to Delete', response.data)

        # Verify it's gone from DB
        with sqlite3.connect(app.DB_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM todo WHERE id = ?", (task_id,))
            task = cursor.fetchone()
            self.assertIsNone(task)

    def test_search_todo(self):
        # Add tasks
        self.app.post('/add', data=dict(title='Buy Milk'), follow_redirects=True)
        self.app.post('/add', data=dict(title='Walk Dog'), follow_redirects=True)
        self.app.post('/add', data=dict(title='Read Book'), follow_redirects=True)

        # Search for 'Milk'
        response = self.app.get('/?q=Milk')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buy Milk', response.data)
        self.assertNotIn(b'Walk Dog', response.data)
        self.assertNotIn(b'Read Book', response.data)

        # Search for 'k' (should match 'Milk', 'Walk', 'Book')
        response = self.app.get('/?q=k')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Buy Milk', response.data)
        # Walk Dog contains 'k', so it should be in the results.
        self.assertIn(b'Walk Dog', response.data)
        self.assertIn(b'Read Book', response.data)

        # Search for non-existent
        response = self.app.get('/?q=Unicorn')
        self.assertEqual(response.status_code, 200)
        self.assertNotIn(b'Buy Milk', response.data)
        self.assertNotIn(b'Walk Dog', response.data)
        self.assertNotIn(b'Read Book', response.data)

if __name__ == '__main__':
    unittest.main()
