const POPUP_CONTENT_DIV="popup_content";

function showPopupContent() {
    var popupContent = document.getElementById(POPUP_CONTENT_DIV);
    popupContent.style.display = "block";
}

function hidePopupContent() {
    var popupContent = document.getElementById(POPUP_CONTENT_DIV);
    popupContent.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById(POPUP_CONTENT_DIV);
    if (event.target === modal) {
        modal.style.display = "none";
    }
}