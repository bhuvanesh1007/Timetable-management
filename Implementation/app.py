from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Database connection function
def connect_db():
    return sqlite3.connect('timetable.db')

# Create timetable table
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS timetable (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        course TEXT NOT NULL,
                        faculty TEXT NOT NULL,
                        time TEXT NOT NULL)''')
    conn.commit()
    conn.close()

# API to fetch timetable
@app.route('/timetable', methods=['GET'])
def get_timetable():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM timetable")
    data = cursor.fetchall()
    conn.close()
    return jsonify([{"id": row[0], "course": row[1], "faculty": row[2], "time": row[3]} for row in data])

# API to add a new timetable entry
@app.route('/timetable', methods=['POST'])
def add_timetable():
    new_entry = request.json
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO timetable (course, faculty, time) VALUES (?, ?, ?)",
                   (new_entry['course'], new_entry['faculty'], new_entry['time']))
    conn.commit()
    conn.close()
    return jsonify({"message": "Timetable entry added"}), 201

# Home route
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
