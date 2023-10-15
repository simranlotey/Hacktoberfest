import pyshorteners

def shorten_url(url_to_shorten):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url_to_shorten)
    return shortened_url

if __name__ == "__main__":
    url_to_shorten = input("Enter the URL to shorten: ")
    shortened_url = shorten_url(url_to_shorten)
    print("Shortened URL:", shortened_url)
