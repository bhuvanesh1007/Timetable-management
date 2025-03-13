from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///timetable.db'
db = SQLAlchemy(app)

class Timetable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    course = db.Column(db.String(100), nullable=False)
    faculty = db.Column(db.String(100), nullable=False)
    day = db.Column(db.String(20), nullable=False)
    start_time = db.Column(db.String(10), nullable=False)
    end_time = db.Column(db.String(10), nullable=False)
    room = db.Column(db.String(10), nullable=False)

db.create_all()

@app.route('/timetable', methods=['POST'])
def add_timetable():
    data = request.json
    new_entry = Timetable(**data)
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Timetable entry added"}), 201

@app.route('/timetable', methods=['GET'])
def get_timetable():
    timetable = Timetable.query.all()
    return jsonify([{
        "course": t.course, "faculty": t.faculty, "day": t.day,
        "start_time": t.start_time, "end_time": t.end_time, "room": t.room
    } for t in timetable])

if __name__ == '__main__':
    app.run(debug=True)
