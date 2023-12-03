function showTab(tabId) {
    var tabs = document.querySelectorAll('.tab-content');
    tabs.forEach(function(tab) {
        tab.classList.remove('active');
    });

    var selectedTab = document.getElementById(tabId);
    selectedTab.classList.add('active');

    // Remove active class from all tabs
    var tabHeaders = document.querySelectorAll('.tab');
    tabHeaders.forEach(function(tabHeader) {
        tabHeader.classList.remove('active');
    });

    // Add active class to the clicked tab
    var clickedTab = document.querySelector('.tab[data-tab-id="' + tabId + '"]');
    if (clickedTab) {
        clickedTab.classList.add('active');
    }
}

