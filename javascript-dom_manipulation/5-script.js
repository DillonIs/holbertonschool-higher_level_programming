let UpdateHeader = document.getElementById('update_header');

UpdateHeader.addEventListener('click', function() {
  let headerElement = document.querySelector('header');
  headerElement.innerText = 'New Header!!!';
});
