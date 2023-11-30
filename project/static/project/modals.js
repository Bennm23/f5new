const CONFIRM_DELETE_DIV="confirm_delete_div";

function showConfirmDelete() {
    var confirmDeleteDiv = document.getElementById(CONFIRM_DELETE_DIV);
    confirmDeleteDiv.style.display = "block";
}

function hideConfirmDelete() {
    var confirmDeleteDiv = document.getElementById(CONFIRM_DELETE_DIV);
    confirmDeleteDiv.style.display = "none";
}

window.onclick = function(event) {
    var modal = document.getElementById(CONFIRM_DELETE_DIV);
    if (event.target === modal) {
        modal.style.display = "none";
    }
}