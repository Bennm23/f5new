const POPUP_CONTENT_DIV="popup_content";

function showPopupContent() {
    popupById(POPUP_CONTENT_DIV)
}

function hidePopupContent() {
    hideById(POPUP_CONTENT_DIV)
}

function popupById(elementId) {
    var popupContent = document.getElementById(elementId);
    popupContent.style.display = "block";
}

function hideById(elementId) {
    var popupContent = document.getElementById(elementId);
    popupContent.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById(POPUP_CONTENT_DIV);
    if (event.target === modal) {
        modal.style.display = "none";
    }
}