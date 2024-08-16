document.addEventListener('DOMContentLoaded', function () {
    const addPlaneForm = document.getElementById('addPlaneForm');

    if (addPlaneForm) {
        addPlaneForm.addEventListener('submit', function (event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(addPlaneForm);
            console.log('Form Data:', formData); // Debugging statement

            fetch('/add-plane/', { // Ensure this URL matches your URL configuration
                    method: 'POST',
                    body: formData,
                    headers: {
                        'X-Requested-With': 'XMLHttpRequest',
                        'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                    }
                })
                .then(response => {
                    console.log('Response Status:', response.status); // Debugging statement
                    return response.json();
                })
                .then(data => {
                    console.log('Response Data:', data); // Debugging statement
                    if (data.success) {
                        alert('Plane added successfully!');
                        const modal = bootstrap.Modal.getInstance(document.getElementById('addPlaneModal'));
                        modal.hide();
                        updatePlaneDropdown(data.newPlane);
                    } else {
                        alert('Error adding plane: ' + data.error);
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    }

    function updatePlaneDropdown(newPlane) {
        const dropdown = document.querySelector('#id_plane');
        const newOption = document.createElement('option');
        newOption.value = newPlane.id;
        newOption.textContent = `${newPlane.make} ${newPlane.model}`;
        dropdown.appendChild(newOption);
    }
});