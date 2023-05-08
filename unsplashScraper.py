import requests
from bs4 import BeautifulSoup

# URL to scrape
url = "your unsplash url here"

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all <img> tags on the page
img_tags = soup.find_all("img")

# Extract the src attribute from each <img> tag
img_urls = [img['src'] for img in img_tags]

# Print the image URLs
print(img_urls)