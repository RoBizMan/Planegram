/**
 * @jest-environment jsdom
 */

const {
    fetchGrams,
    dismissAlerts
} = require('../script.js');

beforeAll(() => {
    // Set up the DOM structure required for the tests
    document.body.innerHTML = `
        <div id="gram-container">Initial content</div>
        <button id="load-more" data-page="2">Load More</button>
        <div class="alert show">Test Alert</div>
    `;
});

describe('fetchGrams', () => {
    beforeEach(() => {
        global.fetch = jest.fn(() =>
            Promise.resolve({
                ok: true,
                text: () => Promise.resolve('<div id="gram-container">New content</div>'),
            })
        );
    });

    test('should fetch and append new grams to the container', async () => {
        const gramContainer = document.getElementById('gram-container');
        const loadMoreButton = document.getElementById('load-more');
        const currentPage = 2;

        const result = await fetchGrams(currentPage, loadMoreButton, gramContainer);

        expect(result).toBe(true);
        expect(gramContainer.innerHTML).toContain('New content');
    });

    test('should hide the load more button when no more pages are available', async () => {
        global.fetch = jest.fn(() =>
            Promise.resolve({
                ok: true,
                text: () => Promise.resolve('<div id="gram-container">New content</div>'),
            })
        );

        const gramContainer = document.getElementById('gram-container');
        const loadMoreButton = document.getElementById('load-more');
        loadMoreButton.style.display = 'block';

        const result = await fetchGrams(2, loadMoreButton, gramContainer);

        expect(result).toBe(true);
        expect(loadMoreButton.style.display).toBe('none');
    });
});

describe('dismissAlerts', () => {
    jest.useFakeTimers();

    test('should auto-dismiss alerts after 5 seconds', () => {
        const alert = document.querySelector('.alert');

        dismissAlerts();

        expect(alert.classList.contains('show')).toBe(true);

        // Fast-forward time by 5 seconds
        jest.advanceTimersByTime(5000);

        expect(alert.classList.contains('show')).toBe(false);
        expect(alert.classList.contains('fade')).toBe(true);
    });
});