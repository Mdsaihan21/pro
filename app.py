from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS employee(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Add Employee
@app.route('/add', methods=['POST'])
def add_employee():

    data = request.json

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO employee(name) VALUES(?)",
        (data['name'],)
    )

    conn.commit()
    conn.close()

    return jsonify({
        "message":"Employee Added Successfully"
    })

# Get Employee List
@app.route('/employees')
def employees():

    conn = sqlite3.connect("employee.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM employee")

    data = cursor.fetchall()

    conn.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)