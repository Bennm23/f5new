
// Toggle visibility of search forms on searchables.
function toggleSearchForm() {
  var search_form_container = document.getElementById("search_form_container");
  if (search_form_container.style.display === "none" || search_form_container.style.display === "") {
    search_form_container.style.display = "block";
  } else {
    search_form_container.style.display = "none";
  }
}

// Toggle visibility of site menu on all pages.
function toggleMenu() {
  const nav = document.querySelector("nav");
  const content = document.querySelector(".container");

  nav.classList.toggle("open");
  content.classList.toggle("blur");
}