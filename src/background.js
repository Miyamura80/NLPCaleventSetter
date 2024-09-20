chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {
    if (request.action === "bookEvent") {
      bookCalendarEvent(request.description)
        .then(() => sendResponse({success: true}))
        .catch(error => sendResponse({success: false, error: error.message}));
      return true;  // Indicates we will send a response asynchronously
    }
  });
  
  async function bookCalendarEvent(description) {
    const token = await getAuthToken();
    const event = await parseEventDescription(description);
    
    const response = await fetch('https://www.googleapis.com/calendar/v3/calendars/primary/events', {
      method: 'POST',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        'summary': event.summary,
        'description': event.description,
        'start': {'dateTime': event.start},
        'end': {'dateTime': event.end},
        'attendees': [{'email': 'eito@gatlingx.com'}]
      })
    });
  
    if (!response.ok) {
      throw new Error('Failed to create event');
    }
  }
  
  async function getAuthToken() {
    return new Promise((resolve, reject) => {
      chrome.identity.getAuthToken({interactive: true}, function(token) {
        if (chrome.runtime.lastError) {
          reject(chrome.runtime.lastError);
        } else {
          resolve(token);
        }
      });
    });
  }
  
  async function parseEventDescription(description) {
    // This is a placeholder for natural language processing.
    // In a real implementation, you would use a more sophisticated NLP service.
    const now = new Date();
    const oneHourLater = new Date(now.getTime() + 60 * 60 * 1000);
    
    return {
      summary: "Automatically created event",
      description: description,
      start: now.toISOString(),
      end: oneHourLater.toISOString()
    };
  }