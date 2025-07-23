document.addEventListener('DOMContentLoaded', function() {
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      return response.json();
    })
    .then(data => {
      let Hello = document.getElementById('hello');
      let data_hello = data.hello;
      Hello.textContent = data_hello;
    })

    .catch(error => {
      console.error('Error getting the hello:', error);
    });
});
