from bs4 import BeautifulSoup
import requests

# Request target website and store as variable
page_to_scrape = requests.get("https://www.gutenberg.org/cache/epub/84/pg84-images.html")

# Parse the website HTML and store as a variable
soup = BeautifulSoup(page_to_scrape.text, "html.parser")

# Find all chapters on the page
chapters = soup.find_all("div", class_="chapter")

# Open a text file in write mode
with open("output.txt", "w", encoding="utf-8") as file:
    # Iterate through each chapter and write its text content to the file
    for chapter in chapters:
        file.write(chapter.get_text(separator='\n'))
        file.write("\n\n")
