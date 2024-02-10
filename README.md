# Project Documentation: Web Scraping of ThinkByte.ai Website

## Introduction
This project aims to scrape data from all pages of the ThinkByte.ai website using Python and Beautiful Soup. The objective is to extract relevant details and information available on each page, ensuring that the scraping process is efficient and comprehensive, covering all sections and categories of the website.

## Tools and Technologies Used
- Python programming language
- Beautiful Soup library for parsing HTML
- Requests library for making HTTP requests
- Regular expressions for URL filtering

## Implementation Details
### 1. URL Filtering and Avoiding Duplicate Visits
The script maintains a set of visited URLs to avoid revisiting the same page. It filters URLs based on certain criteria such as ensuring they belong to the ThinkByte.ai domain and excluding URLs from Facebook and LinkedIn.

### 2. Scraping Process
- The script makes an HTTP request to fetch the HTML content of each page.
- If the request is successful (status code 200), it parses the HTML using Beautiful Soup.
- Relevant data such as page title, paragraphs, classes, and list items are extracted from the HTML.
- Links on the page are also extracted for further scraping of linked pages.

### 3. Data Storage
Scraped data is stored in a list of dictionaries, with each dictionary representing the data extracted from a single page. The data includes URL, title, paragraphs, classes, and list items.

### 4. Saving Data to Text File
The scraped data is saved to a text file in the "data" folder. Each entry in the text file corresponds to the data extracted from a single page, organized by URL, title, paragraphs, classes, and list items.

## Example Usage
```python
seed_url = 'https://thinkbyte.ai/'
scrape_website(seed_url)

# Save the scraped data to a text file
save_to_text('scraped_complete_data.txt')
```

## Conclusion
The web scraping script successfully retrieves data from all pages of the ThinkByte.ai website, ensuring comprehensive coverage of relevant information. The extracted data can be further analyzed and utilized for bulding chatbot using framework LlamaIndex.
