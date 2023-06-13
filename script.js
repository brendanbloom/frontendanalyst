const apiUrl = 'https://github.com/brendanbloom/backendanalyst.git';  // Replace with the URL of your backend API

fetch(apiUrl)
  .then(response => response.json())
  .then(data => {
    const dataContainer = document.getElementById('data-container');
    dataContainer.textContent = data.message;
  })
  .catch(error => {
    console.error('Error:', error);
  });
