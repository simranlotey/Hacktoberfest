const toggleSwitch = document.getElementById('toggle');

toggleSwitch.addEventListener('change', () => {
    document.body.classList.toggle('dark-mode', toggleSwitch.checked);
    document.body.classList.toggle('light-mode', !toggleSwitch.checked);
});

// Optional: Set default mode based on system preference
if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    toggleSwitch.checked = true;
    document.body.classList.add('dark-mode');
}
