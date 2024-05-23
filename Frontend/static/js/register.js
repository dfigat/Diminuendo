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
                    console.log('Registration succesfully comppleted!');
                } else {
                    const response = JSON.parse(xhr.responseText);
                    console.error('Error:', xhr.status, xhr.responseText);
                }
            }
        };

        console.log(formData);
        xhr.send(formData);
    });
});