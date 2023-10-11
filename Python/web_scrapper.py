import requests
from bs4 import BeautifulSoup

def scrape_and_extract_titles(url):
    try:
        
        response = requests.get(url)

        
        if response.status_code == 200:
            
            soup = BeautifulSoup(response.text, 'html.parser')

            
            titles = soup.find_all('h2')

            
            for title in titles:
                print(title.text)

        else:
            print(f"Failed to retrieve the web page. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    user_url = input("Enter the URL of the web page you want to scrape: ")
    scrape_and_extract_titles(user_url)
