
import requests
from bs4 import BeautifulSoup
from collections import Counter
from urllib.parse import urljoin
import csv

def fetch_hyperlinks(url):
    
    # Fetch the webpage content
    response = requests.get(url)
    response.raise_for_status()  # Raises an HTTPError for bad responses
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Select all <a> tags with an href attribute
    link_elements = soup.select("a[href]")
    
    # List to hold all hyperlinks
    hyperlinks = []
    
    # Extract href attribute from each <a> tag and resolve relative URLs
    for link in link_elements:
        href = link['href']
        absolute_url = urljoin(url, href)  # Convert relative URLs to absolute
        hyperlinks.append(absolute_url)
    
    return hyperlinks

    return []

def main():
    # URL to crawl
    base_url = "https://www.piet.poornima.org/"
    
    # Fetch hyperlinks from the base URL
    hyperlinks = fetch_hyperlinks(base_url)
    
    # Count the frequency of each hyperlink
    hyperlink_counts = Counter(hyperlinks)
    
    # Sort hyperlinks by frequency
    sorted_hyperlinks = sorted(hyperlink_counts.items(), key=lambda x: x[1], reverse=True)
    
    with open("hyperlinks.csv", "w", newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Hyperlink", "Frequency"])
        csv_writer.writerows(sorted_hyperlinks)


if __name__ == "__main__":
    main()