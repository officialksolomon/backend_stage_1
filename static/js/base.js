const allButtons = document.querySelectorAll('button')
// closes alerts on all pages after a giving timeout
const closeAlerts = () => {
    const alerts = document.querySelectorAll(".alert");
    setTimeout(() => {
        alerts.forEach((alert) => {
            alert.classList.add('d-none');
        });
    }, 8000);
};
// close alert after DOM is loaded.
document.addEventListener('DOMContentLoaded', closeAlerts);
// close alert when any button is clicked.
allButtons.forEach((button) => {
    button.addEventListener('click', closeAlerts)
})

// closes the laoding indicator on all pages...
const closeLoader = () => {
    const loaderWrapper = document.querySelector('.loader-wrapper');
    window.addEventListener('load', () => {
        loaderWrapper.classList.add('d-none');

    });
};
closeLoader();

