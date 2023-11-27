
// Toggle visibility of search forms on searchables.
function toggleSearchForm() {
  var searchFormContainer = document.getElementById("searchFormContainer");
  if (searchFormContainer.style.display === "none" || searchFormContainer.style.display === "") {
    searchFormContainer.style.display = "block";
  } else {
    searchFormContainer.style.display = "none";
  }
}