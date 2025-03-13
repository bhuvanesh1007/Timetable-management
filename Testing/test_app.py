import unittest
from app import app, db, Timetable

class TestTimetable(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()
        db.create_all()

    def test_add_timetable(self):
        response = self.client.post('/timetable', json={
            "course": "Math", "faculty": "Dr. Smith",
            "day": "Monday", "start_time": "10:00", "end_time": "11:00", "room": "A1"
        })
        self.assertEqual(response.status_code, 201)

    def test_get_timetable(self):
        response = self.client.get('/timetable')
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == "__main__":
    unittest.main()
