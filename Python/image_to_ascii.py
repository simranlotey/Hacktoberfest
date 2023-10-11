from PIL import Image

# Define the ASCII characters to represent different shades of gray
ASCII_CHARS = "@%#*+=-:. "


# Resize the image according to the desired width while maintaining aspect ratio
def resize_image(image, new_width=100):
    width, height = image.size
    ratio = height / width / 1.65
    new_height = int(new_width * ratio)
    resized_image = image.resize((new_width, new_height))
    return resized_image


# Convert each pixel to a grayscale pixel using the luminance formula
def grayscale_image(image):
    grayscale_image = image.convert("L")
    return grayscale_image


# Map the grayscale pixels to ASCII characters
def pixels_to_ascii(image, ascii_chars=ASCII_CHARS):
    pixels = image.getdata()
    ascii_str = ""
    for pixel_value in pixels:
        ascii_str += ascii_chars[pixel_value // 25]
    return ascii_str


# Main function to convert an image to ASCII art
def image_to_ascii(image_path, output_width=100):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(e)
        return

    image = resize_image(image, output_width)
    image = grayscale_image(image)
    ascii_str = pixels_to_ascii(image)

    # Split the ASCII art into multiple lines to fit the desired width
    img_width = image.width
    ascii_str = "\n".join(ascii_str[i:(i + img_width)] for i in range(0, len(ascii_str), img_width))

    return ascii_str


if __name__ == "__main__":
    input_image_path = input("Enter image path: ")
    output_width = 100

    ascii_art = image_to_ascii(input_image_path, output_width)

    with open("output.txt", "w") as output_file:
        output_file.write(ascii_art)

    print("ASCII art saved to 'output.txt'")
