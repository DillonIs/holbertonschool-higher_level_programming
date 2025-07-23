let listElement = document.getElementById('add_item');

listElement.addEventListener('click', function() {
  let ulElement = document.querySelector('.my_list');
  let liElement = document.createElement('li');
  liElement.textContent = 'Item';

  ulElement.appendChild(liElement);
});
