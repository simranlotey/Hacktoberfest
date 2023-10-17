
interface Coordinates {
    latitude: number;
    longitude: number;
  }
  
  class GeolocationService {
    static getUserCoordinates(): Promise<Coordinates> {
      return new Promise((resolve, reject) => {
        if (!navigator.geolocation) {
            reject(new Error('Browser does not support geolocation.'));
        } else {
          navigator.geolocation.getCurrentPosition(
            (position) => {
              const { latitude, longitude } = position.coords;
              resolve({ latitude, longitude });
            },
            (error) => {
              switch (error.code) {
                case error.PERMISSION_DENIED:
                    reject(new Error('User denied.'));
                  break;
                case error.POSITION_UNAVAILABLE:
                    reject(new Error('Unavailable.'));
                  break;
                case error.TIMEOUT:
                    reject(new Error('Timed out.'));
                  break;
                default:
                    reject(new Error('Something broke and caused an error.'));
                  break;
              }
            }
          );
        }
      });
    }
  }
  
