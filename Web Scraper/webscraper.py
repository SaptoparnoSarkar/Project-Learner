import requests 
from bs4 import BeautifulSoup

#URL of the page I want to scrape
url = 'https://www.amazon.in/-/en/ref=nav_logo'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

#Send a GET request to the URL
# response = requests.get(url)
response = requests.get(url, headers=headers)

if response.status_code == 200:
    page_content = response.content
    print(page_content)
    
    soup = BeautifulSoup(page_content, 'html.parser')
    print(soup.prettify())
    
    links = soup.find_all('a')
    for i in links:
        href = i.get('href')
        print(href)
else:
    print(f'Failed to Recieve Page Content. Status code: {response.status_code}')
