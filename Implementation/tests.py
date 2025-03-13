import unittest
import sqlite3

# Import the app correctly
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'Implementation')))

from app import app  # Now, this should work

class TimetableTestCase(unittest.TestCase):

    def setUp(self):
        """Set up test client and database"""
        self.app = app.test_client()
        self.app.testing = True
        self.db = sqlite3.connect('timetable.db')
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close database after test"""
        self.db.close()

    def test_get_timetable(self):
        """Test fetching timetable"""
        response = self.app.get('/timetable')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json, list)

if __name__ == '__main__':
    unittest.main()
