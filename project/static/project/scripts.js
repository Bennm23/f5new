
// Toggle visibility of search forms on searchables.
function toggleSearchForm() {
  var search_form_container = document.getElementById("search_form_container");
  if (search_form_container.style.display === "none" || search_form_container.style.display === "") {
    search_form_container.style.display = "block";
  } else {
    search_form_container.style.display = "none";
  }
}

function toggleMenu() {
  var hidden_object = document.querySelector('.nav_wrapper_hidden');
  var togglerButton = document.getElementById('toggler_button');

  if (hidden_object.style.display === 'flex') {
    hidden_object.style.display = 'none';
    togglerButton.classList.remove('fa-xmark');
    togglerButton.classList.add('fa-bars');
  } else {
    hidden_object.style.display = 'flex';
    togglerButton.classList.remove('fa-bars');
    togglerButton.classList.add('fa-xmark');
  }
}