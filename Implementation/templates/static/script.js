document.addEventListener('DOMContentLoaded', function() {
    fetchTimetable();

    document.getElementById('addForm').addEventListener('submit', function(event) {
        event.preventDefault();
        const course = document.getElementById('course').value;
        const faculty = document.getElementById('faculty').value;
        const time = document.getElementById('time').value;

        fetch('/timetable', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ course, faculty, time })
        }).then(response => response.json())
          .then(() => {
              fetchTimetable();
              document.getElementById('addForm').reset();
          });
    });
});

function fetchTimetable() {
    fetch('/timetable')
        .then(response => response.json())
        .then(data => {
            const list = document.getElementById('timetable-list');
            list.innerHTML = '';
            data.forEach(entry => {
                const li = document.createElement('li');
                li.textContent = `${entry.course} - ${entry.faculty} at ${entry.time}`;
                list.appendChild(li);
            });
        });
}
