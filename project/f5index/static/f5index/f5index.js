document.addEventListener('DOMContentLoaded', function () {
    new Glide('.glide', {
        type: 'carousel', // Use 'carousel' for a basic slider
        startAt: 0,
        perView: 1, // Number of slides to show at once
        focusAt: 'center',
        gap: 20, // Space between slides
        breakpoints: {

        }
    }).mount();
});