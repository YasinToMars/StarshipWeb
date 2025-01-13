from flask import Flask, render_template
import sqlite3
import os

# Initialize Flask app
app = Flask(__name__)

# Get the path to the database dynamically
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # Root of the project
DB_PATH = os.path.join(BASE_DIR, 'contact.db')  # Adjust for your database file in the root

# Route to display contact messages
@app.route('/')
def display_messages():
    try:
        # Connect to the database
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()

        # Fetch all contact messages
        cursor.execute('SELECT name, email, message FROM contacts')
        messages = cursor.fetchall()
        conn.close()

        # Pass the messages to the template
        return render_template('display.html', messages=messages)
    except Exception as e:
        return f"An error occurred: {e}"  # For debugging purposes in case of errors


# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)  # Render typically uses port 5000
