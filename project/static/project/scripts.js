
// Toggle visibility of search forms on searchables.
function toggleSearchForm() {
  var searchFormContainer = document.getElementById("searchFormContainer");
  if (searchFormContainer.style.display === "none" || searchFormContainer.style.display === "") {
    searchFormContainer.style.display = "block";
  } else {
    searchFormContainer.style.display = "none";
  }
}

// Toggle visibility of site menu on all pages.
function toggleMenu() {
  const nav = document.querySelector("nav");
  const content = document.querySelector(".container");

  nav.classList.toggle("open");
  content.classList.toggle("blur");
}