function toggleMenu() {
    var navWrapperHidden = document.querySelector('.nav_wrapper_hidden');
    var togglerButton = document.querySelector('.nav_toggler i');

    // Check the current state and toggle it
    if (navWrapperHidden.classList.contains('show')) {
        navWrapperHidden.classList.remove('show');
        setTimeout(function() {
            navWrapperHidden.style.display = "none";
        }, 500); // Match the timeout to your transition duration
        togglerButton.classList.replace('fa-times', 'fa-bars');
    } else {
        navWrapperHidden.style.display = "flex";
        setTimeout(function() {
            navWrapperHidden.classList.add('show');
        }, 10);
        togglerButton.classList.replace('fa-bars', 'fa-times');
    }
}

function setMenuInitialState() {
    var navWrapperHidden = document.querySelector('.nav_wrapper_hidden');
    var togglerButton = document.querySelector('.nav_toggler i');

    // Initially hide the menu
    navWrapperHidden.style.display = "none";
    navWrapperHidden.classList.remove('show');
    togglerButton.classList.add('fa-bars');
}

document.addEventListener('DOMContentLoaded', function() {
    setMenuInitialState();
});