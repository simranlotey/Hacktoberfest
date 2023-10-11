import requests
import uuid


def generate_qr_code(data, size="150x150"):
    # URL for the qrserver.com QR code generation API
    api_url = f"https://api.qrserver.com/v1/create-qr-code/?size={size}&data={data}"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            return response.content
        else:
            print(f"Failed to generate QR code. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def generate_filename():
    unique_id = uuid.uuid4().hex
    return f"qr_code_{unique_id}.png"


if __name__ == "__main__":
    data = input("Enter data or URL: ")

    qr_code = generate_qr_code(data)

    if qr_code:
        filename = generate_filename()
        with open(filename, "wb") as qr_code_file:
            qr_code_file.write(qr_code)
        print(f"QR code saved as '{filename}'")
