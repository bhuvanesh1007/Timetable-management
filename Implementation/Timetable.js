import React, { useEffect, useState } from "react";

const Timetable = () => {
  const [timetable, setTimetable] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:5000/timetable")
      .then(response => response.json())
      .then(data => setTimetable(data));
  }, []);

  return (
    <div>
      <h2>Class Timetable</h2>
      <table border="1">
        <thead>
          <tr>
            <th>Course</th>
            <th>Faculty</th>
            <th>Day</th>
            <th>Time</th>
            <th>Room</th>
          </tr>
        </thead>
        <tbody>
          {timetable.map((entry, index) => (
            <tr key={index}>
              <td>{entry.course}</td>
              <td>{entry.faculty}</td>
              <td>{entry.day}</td>
              <td>{entry.start_time} - {entry.end_time}</td>
              <td>{entry.room}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Timetable;
