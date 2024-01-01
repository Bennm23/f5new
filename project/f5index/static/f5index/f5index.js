document.addEventListener('DOMContentLoaded', function() {
    // Add click event listener to the dismiss button
    const dismissButton = document.querySelector('.dismiss_button');
    dismissButton.addEventListener('click', function() {
        // Hide the parent element of the dismiss button, which is '.fact_of_the_day'
        this.parentElement.style.display = 'none';
    });
});