const apiUrl = 'https://github.com/brendanbloom/frontendanalyst/blob/main/main.py';  // Replace with the URL of your backend API

// Make a GET request to the backend API
fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    // Process the response data
    console.log(data);
  })
  .catch(error => {
    // Handle any errors
    console.error('Error:', error);
  });
