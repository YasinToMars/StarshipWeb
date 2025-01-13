from flask import Flask, render_template
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Route to display contact messages
@app.route('/')
def display_messages():
    # Connect to the database
    conn = sqlite3.connect('./contact.db')
    cursor = conn.cursor()

    # Fetch all contact messages
    cursor.execute('SELECT name, email, message FROM contacts')
    messages = cursor.fetchall()
    conn.close()

    # Pass the messages to the template
    return render_template('display.html', messages=messages)


# Entry point for the application
if __name__ == '__main__':
    app.run(debug=True, port=5001)