#! DAY-22 WEB SCRAPING
# python "Python_all_concept\webscraping.py"

import requests
from bs4 import BeautifulSoup

# 1. Target URL
url = 'https://archive.ics.uci.edu/dataset/1/abalone'

# 2. Fetch webpage
response = requests.get(url)
print(f"Status Code: {response.status_code}")

# 3. Parse HTML
soup = BeautifulSoup(response.content, 'html.parser')

# 4. Extract and print the page title
print("Page Title:", soup.title.string)
