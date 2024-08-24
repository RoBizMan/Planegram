/* jshint esversion: 11 */

document.addEventListener('DOMContentLoaded', function () {
    // Load more functionality for infinite scrolling
    let currentPage = 2; // Start from the second page
    const loadMoreButton = document.getElementById('load-more');
    const gramContainer = document.getElementById('gram-container');

    if (loadMoreButton) {
        loadMoreButton.addEventListener('click', function () {
            fetch(`?page=${currentPage}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Network response was not ok');
                    }
                    return response.text();
                })
                .then(data => {
                    const parser = new DOMParser();
                    const doc = parser.parseFromString(data, 'text/html');
                    const newGrams = doc.getElementById('gram-container').innerHTML;

                    // Append new grams to the existing container
                    gramContainer.innerHTML += newGrams;

                    // Check if there's a next page
                    if (!doc.querySelector('#load-more')) {
                        loadMoreButton.style.display = 'none'; // Hide the button if no more pages
                    } else {
                        currentPage++;
                        loadMoreButton.dataset.page = currentPage; // Update the data-page attribute
                    }
                })
                .catch(error => {
                    console.error('There was a problem with the fetch operation:', error);
                });
        });
    }

    // Auto-dismiss alerts after a few seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        // Set a timeout to dismiss the alert after 5 seconds
        setTimeout(() => {
            alert.classList.remove('show');
            alert.classList.add('fade');
        }, 5000); // 5000 milliseconds = 5 seconds
    });
});