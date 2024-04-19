// Function to fetch available dates and time slots from the server
function fetchAvailability() {
    // Make an AJAX request to the server to fetch availability data
    // Update the calendar based on the response
    fetch('/bookings/fetch_availability/')
        .then(response => response.json())
        .then(data => updateCalendar(data))
        .catch(error => console.error('Error fetching availability:', error));
}

// Function to update the calendar with available dates and time slots
function updateCalendar(availabilityData) {
    // Update the calendar HTML dynamically based on availabilityData
    // Example: Populate the calendar with available dates and time slots
    const calendarElement = document.getElementById('calendar');
    calendarElement.innerHTML = '';  // Clear existing calendar content
    availabilityData.forEach(date => {
        const dateElement = document.createElement('div');
        dateElement.textContent = `Date: ${date.date}, Available Time Slots: ${date.time_slots}`;
        calendarElement.appendChild(dateElement);
    });
}
// Function to initialize the calendar functionality
function initCalendar() {
    // Call fetchAvailability to fetch initial data when the page loads
    fetchAvailability();
}

// Call initCalendar when the page loads
document.addEventListener('DOMContentLoaded', initCalendar);