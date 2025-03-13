import sqlite3

conn = sqlite3.connect('timetable.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS timetable (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    course TEXT,
                    faculty TEXT,
                    time TEXT)''')

cursor.execute("INSERT INTO timetable (course, faculty, time) VALUES ('Math', 'Dr. Smith', '10:00 AM')")
cursor.execute("INSERT INTO timetable (course, faculty, time) VALUES ('Physics', 'Dr. Johnson', '11:00 AM')")

conn.commit()
conn.close()

print("Database setup complete!")
