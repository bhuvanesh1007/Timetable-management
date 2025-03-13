 Test Cases for Timetable Management System
1️⃣ Homepage Loading
Scenario: Verify if the homepage loads correctly.
Steps:
Open a browser.
Enter the application URL (/).
Press Enter.
Expected Result: The homepage should display a welcome message.

2️⃣ Fetch All Timetable Entries
Scenario: Check if all timetable entries are retrieved.
Steps:
Send a GET request to /timetable.
Expected Result: A JSON response containing a list of timetable entries.

3️⃣ Add a New Timetable Entry
Scenario: Verify if a new entry can be added successfully.
Steps:
Send a POST request to /timetable with the following data:
json

Copy

Edit
{
  "day": "Monday",
  "time": "10:00 AM",
  "subject": "Math",
  "faculty": "Dr. Smith"
}
Expected Result: The response status should be 201, and a success message should be returned.

4️⃣ Add Timetable Entry with Missing Field
Scenario: Check if the system handles missing fields properly.
Steps:
Send a POST request to /timetable without the "subject" field.
Expected Result: The response should return a 400 Bad Requestand

5️⃣ Update an Existing Timetable Entry
Scenario: Verify if an existing timetable entry can be updated.
Steps:
Send a PUT request to /timetable/1 with the following data:
json

Copy

Edit
{
  "subject": "Physics"
}
Expected Result: The response should return a 200 status with a confirmation message.

6️⃣ Update Timetable Entry with Invalid ID
Scenario: Check the behavior when updating a non-existent entry.
Steps:
Send a PUT request to /timetable/999 (assuming ID 999 does not exist).
Expected Result: The response should return a 404 Not Found error.

7️⃣ Delete an Existing Timetable Entry
Scenario: Verify if a timetable entry can be deleted.
Steps:
Send a DELETE request to /timetable/1.
Expected Result: The response should return a 200 status with a deletion confirmation message.

8️⃣ Delete Timetable Entry with Invalid ID
Scenario: Check if an error is returned when deleting a non-existent entry.
Steps:
Send a DELETE request to /timetable/999 (assuming ID 999 does not exist).
Expected Result: The response should return a 404 Not Found error.

9️⃣ API Handles Large Data
Scenario: Test if the system can handle a large number of timetable records.
Steps:
Insert 1000+ timetable records.
Send a GET request to /timetable.
Expected Result: The response should return all records in a valid JSON format without performance issues.

🔟 Validate Incorrect HTTP Methods
Scenario: Ensure API does not allow unsupported HTTP methods.
Steps:
Send a PATCH request to /timetable/1 (if PATCH is not implemented).
Expected Result: The response should return a 405 Method Not Allowederror.