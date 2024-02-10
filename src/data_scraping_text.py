import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

# Set to store visited URLs to avoid revisiting the same page
visited_urls = set()

# List to store scraped data
scraped_data = []

def scrape_website(url):
    # Check if the URL has already been visited
    if url in visited_urls:
        return
    else:
        visited_urls.add(url)

    # Check if the URL belongs to the desired domain and is not a Facebook URL
    if 'thinkbyte.ai' not in url or 'facebook.com' in url:
        print(f"Skipping URL: {url}")
        return

    # Check if the URL is a LinkedIn URL
    if re.match(r'^https?://(www\.)?linkedin\.com', url):
        print(f"Skipping LinkedIn URL: {url}")
        return

    # Make an HTTP request to fetch the HTML content of the page
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Parse the HTML content using Beautiful Soup
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract relevant data from the page
            # Example: Extract titles, paragraphs, links, classes, li elements, etc.
            title = soup.title.text
            paragraphs = [p.text for p in soup.find_all('p') if 'LinkedIn' not in p.text]
            # classes = [element.text for element in soup.find_all(class_=['article-style',' hero-lead'])]
            classes = [element.text.strip() for element in soup.find_all(class_= ['article-style', 'hero-lead']) if element.text.strip()]
            # classes = [[c for c in cls if '[ ]' not in c] for cls in classes_raw]
            list_items = [li.text for li in soup.find_all('li')]
            # Add the extracted data to the list
            scraped_data.append({'URL': url, 'Title': title, 'Paragraphs': '\n'.join(paragraphs), 'Classes': classes, 'List Items': list_items})
            print(f"Scraped page: {url}")

            # Extract links from the page and recursively scrape linked pages
            links = [link.get('href') for link in soup.find_all('a', href=True)]
            for link in links:
                # Resolve relative URLs to absolute URLs
                absolute_url = urljoin(url, link)
                # Recursively scrape linked pages
                scrape_website(absolute_url)
        else:
            print(f"Failed to fetch page: {url}")
    except Exception as e:
        print(f"Error scraping page {url}: {e}")

def save_to_text(filename):
    # Specify the path where the text file should be saved (in the "data" folder)
    data_folder = 'data'
    os.makedirs(data_folder, exist_ok=True)  # Create the "data" folder if it doesn't exist
    filepath = os.path.join(data_folder, filename)

    # Write the scraped data to a text file
    with open(filepath, 'w', encoding='utf-8') as textfile:
        for data in scraped_data:
            textfile.write(f"URL: {data['URL']}\n")
            textfile.write(f"Title: {data['Title']}\n")
            textfile.write(f"Paragraphs:\n{data['Paragraphs']}\n")
            textfile.write(f"Classes: {data['Classes']}\n")
            textfile.write(f"List Items:\n{data['List Items']}\n")
            textfile.write('\n')

# Example usage:
seed_url = 'https://thinkbyte.ai/'
scrape_website(seed_url)

# Save the scraped data to a text file in the "data" folder
save_to_text('scraped_complete_data.txt')
