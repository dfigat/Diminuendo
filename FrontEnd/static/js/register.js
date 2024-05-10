document.addEventListener('DOMContentLoaded', () => {

    const form = document.querySelector('#registration-form');
    form.addEventListener('submit', (event) => {
        event.preventDefault();

        const formData = new FormData(form);

        const xhr = new XMLHttpRequest();
        xhr.open('POST', '/api/user/', true);
        xhr.onreadystatechange = () => {
            if (xhr.readyState == 4) {
                if (xhr.status == 201) {
                    // success
                } else {
                    console.log('Error:', xhr.status, xhr.responseText);
                }
            }
        };
        xhr.send(formData);
    });
});