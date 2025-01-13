from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/multicam')
def multi_cam():
    return render_template('multicam.html')

# Route for the closures page
@app.route('/closures')
def closures():
    conn = sqlite3.connect('closures.db')
    cursor = conn.cursor()
    cursor.execute("SELECT closure_name, closure_date FROM closures")
    closures_data = cursor.fetchall()
    conn.close()
    
    return render_template("closures.html", closures=closures_data)

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Get data
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # connect to the database
    conn = sqlite3.connect('contact.db')
    cursor = conn.cursor()

    # insert the contact data
    cursor.execute('INSERT INTO contacts (name, email, message) VALUES (?, ?, ?)', (name, email, message))
    conn.commit()
    conn.close()

    # show the notif
    return render_template('contact.html', success=True)

if __name__ == '__main__':
    app.run(debug=True)


