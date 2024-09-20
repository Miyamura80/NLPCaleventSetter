document.addEventListener('DOMContentLoaded', function() {
    const bookEventButton = document.getElementById('bookEvent');
    const eventDescriptionTextarea = document.getElementById('eventDescription');
    const statusDiv = document.getElementById('status');
  
    bookEventButton.addEventListener('click', function() {
      const description = eventDescriptionTextarea.value;
      if (description) {
        chrome.runtime.sendMessage({action: "bookEvent", description: description}, function(response) {
          if (response.success) {
            statusDiv.textContent = "Event booked successfully!";
          } else {
            statusDiv.textContent = "Error booking event: " + response.error;
          }
        });
      } else {
        statusDiv.textContent = "Please enter an event description.";
      }
    });
  });