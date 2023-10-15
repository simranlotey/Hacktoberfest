const form = document.getElementById('myForm');

form.addEventListener('submit', function (event) {
    event.preventDefault();

    const email = form.elements.email.value;
    if (!email.includes('@')) {
        alert('Invalid email address');
        return;
    }

    // Submit the form
    form.submit();
});