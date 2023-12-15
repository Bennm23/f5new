function toggleFilters() {
    var filterContainer = document.querySelector('.filter_container');
    var filterButton = document.querySelector('.filter_toggler');

    // Check if the filter container is currently displayed
    if (filterContainer.style.display === "none" || filterContainer.style.display === "") {
        filterContainer.style.display = "flex";
        setTimeout(function() {
            filterContainer.classList.add('show');
        }, 10); // Timeout to allow the display change to take effect
        filterButton.innerHTML = '<i class="fa-solid fa-times"></i> Filters';
    } else {
        filterContainer.classList.remove('show');
        setTimeout(function() {
            filterContainer.style.display = "none";
        }, 500); // Timeout matches the duration of the fade effect
        filterButton.innerHTML = '<i id="filter_button" class="fa-solid fa-filter"></i> Filters';
    }
}

function setInitialState() {
    var filterContainer = document.querySelector('.filter_container');
    var filterButton = document.querySelector('.filter_toggler');
    var selectedCategory = filterContainer.getAttribute('data-selected-category');

    // Check if the selected category is set and not 'all'
    var shouldShowFilters = selectedCategory;

    if (shouldShowFilters) {
        // Show the filter container
        filterContainer.style.display = "flex";
        filterContainer.classList.add('show');
        filterButton.innerHTML = '<i class="fa-solid fa-times"></i> Filters';
    } else {
        // Hide the filter container
        filterContainer.style.display = "none";
        filterButton.innerHTML = '<i class="fa-solid fa-filter"></i> Filters';
    }
}

document.addEventListener('DOMContentLoaded', function() {
    setInitialState();
});
