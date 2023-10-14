import hashlib

url_dict = {}

def shorten_url(url):
    
    hash_object = hashlib.md5(url.encode())
    short_code = hash_object.hexdigest()[:8]  
    url_dict[short_code] = url

    return short_code

def expand_url(short_code):
    
    original_url = url_dict.get(short_code)
    if original_url:
        return original_url
    else:
        return "URL not found."

if __name__ == "__main__":
    while True:
        print("URL Shortener Menu:")
        print("1. Shorten URL")
        print("2. Expand URL")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            original_url = input("Enter the URL to shorten: ")
            short_code = shorten_url(original_url)
            print("Shortened URL:", short_code)

        elif choice == "2":
            short_code = input("Enter the short code to expand: ")
            original_url = expand_url(short_code)
            print("Expanded URL:", original_url)

        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
