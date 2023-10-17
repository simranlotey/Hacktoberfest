const getLocationButton = document.getElementById('getLocationButton') as HTMLButtonElement;
const locationInfo = document.getElementById('locationInfo') as HTMLParagraphElement;

// Check if geolocation is available in the browser
if ('geolocation' in navigator) {
    getLocationButton.addEventListener('click', getLocation);
} else {
    getLocationButton.disabled = true;
    locationInfo.innerText = 'Geolocation is not available in your browser.';
}

// Get the user's geolocation
function getLocation() {
    getLocationButton.disabled = true;
    locationInfo.innerText = 'Fetching location...';

    navigator.geolocation.getCurrentPosition(
        (position) => {
            const latitude = position.coords.latitude;
            const longitude = position.coords.longitude;
            locationInfo.innerText = `Latitude: ${latitude}, Longitude: ${longitude}`;
        },
        (error) => {
            getLocationButton.disabled = false;
            locationInfo.innerText = `Error: ${getErrorString(error)}`;
        }
    );
}

// Error Handling
function getErrorString(error: GeolocationPositionError): string {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            return 'User denied the request for geolocation.';
        case error.POSITION_UNAVAILABLE:
            return 'Location information is unavailable.';
        case error.TIMEOUT:
            return 'The request to get user location timed out.';
        case error.UNKNOWN_ERROR:
            return 'An unknown error occurred.';
        default:
            return 'An unspecified error occurred.';
    }
}
