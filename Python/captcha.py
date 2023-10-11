from PIL import Image, ImageDraw, ImageFont
import random


def generate_captcha_string(length=6):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    captcha_string = ''.join(random.choice(characters) for _ in range(length))
    return captcha_string


def create_captcha_image(captcha_string, image_width=200, image_height=80):
    image = Image.new('RGB', (image_width, image_height), color='white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", size=36)

    for x in range(0, image_width, 50):
        for y in range(image_height):
            if random.random() > 0.8:
                draw.point((x, y), fill='black')

    for i, char in enumerate(captcha_string):
        draw.text((20 + i * 30, 20), char, font=font, fill='black')

    return image


# Verify user input against the generated CAPTCHA
def verify_captcha(captcha_string, user_input):
    return captcha_string == user_input


if __name__ == "__main__":
    captcha_string = generate_captcha_string()
    captcha_image = create_captcha_image(captcha_string)

    captcha_image.show()  # Display the CAPTCHA image

    user_input = input("Enter the characters you see in the CAPTCHA image: ")

    if verify_captcha(captcha_string, user_input):
        print("CAPTCHA verification successful!")
    else:
        print("CAPTCHA verification failed. Please try again.")
