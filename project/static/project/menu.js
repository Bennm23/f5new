function toggleMenu() {
    var navWrapperHidden = document.querySelector('.nav_wrapper_hidden');
    var togglerButton = document.querySelector('.nav_toggler i');

    // Check the current state and toggle it
    if (navWrapperHidden.classList.contains('show')) {
        navWrapperHidden.classList.remove('show');
        togglerButton.classList.replace('fa-times', 'fa-bars');
    } else {
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
    navWrapperHidden.classList.remove('show');
    togglerButton.classList.add('fa-bars');
}

document.addEventListener('DOMContentLoaded', function() {
    setMenuInitialState();
});