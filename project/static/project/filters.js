function toggleFilters(open) {
    var filterContainer = document.querySelector('.filter_container');
    var filterButton = document.querySelector('.filter_toggler');

    var shouldOpen = open !== undefined ? open : filterContainer.style.display === "none" || filterContainer.style.display === "";

    if (shouldOpen) {
        filterContainer.style.display = "flex";
        setTimeout(function() {
            filterContainer.classList.add('show');
        }, 10);
        filterButton.innerHTML = '<i class="fa-solid fa-times"></i> Filters';
    } else {
        filterContainer.classList.remove('show');
        setTimeout(function() {
            filterContainer.style.display = "none";
        }, 500);
        filterButton.innerHTML = '<i id="filter_button" class="fa-solid fa-filter"></i> Filters';
    }
}

function setInitialFilterState() {
    var params = new URLSearchParams(window.location.search);
    var category = params.get('category');

    // Open the filters if 'category' parameter is present and not empty
    toggleFilters(category !== null && category !== '');
}

document.addEventListener('DOMContentLoaded', function() {
    setInitialFilterState();
});