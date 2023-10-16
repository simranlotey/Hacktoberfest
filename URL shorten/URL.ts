
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geolocation Service</title>
    <script>
        class GeolocationService {
            static getUserCoordinates() {
                return new Promise((resolve, reject) => {
                    if (!navigator.geolocation) {
                        reject(new Error('Geolocation is not supported by this browser.'));
                    } else {
                        navigator.geolocation.getCurrentPosition(
                            (position) => {
                                const { latitude, longitude } = position.coords;
                                resolve({ latitude, longitude });
                            },
                            (error) => {
                                switch (error.code) {
                                    case error.PERMISSION_DENIED:
                                        reject(new Error('User denied the request for Geolocation.'));
                                        break;
                                    case error.POSITION_UNAVAILABLE:
                                        reject(new Error('Location information is unavailable.'));
                                        break;
                                    case error.TIMEOUT:
                                        reject(new Error('The request to get user location timed out.'));
                                        break;
                                    default:
                                        reject(new Error('An unknown error occurred.'));
                                        break;
                                }
                            }
                        );
                    }
                });
            }
        }

        // Example usage
        GeolocationService.getUserCoordinates()
            .then((coordinates) => {
                console.log(`Latitude: ${coordinates.latitude}, Longitude: ${coordinates.longitude}`);
                // You can update the UI here with the latitude and longitude values
            })
            .catch((error) => {
                console.error(`Error: ${error.message}`);
                // Handle errors gracefully in the UI
            });
    </script>
</head>
<body>
<!-- Your HTML content here -->
</body>
</html>
