# Project Gutenberg Scraper

This repository contains a Python script for scraping and extracting chapter texts from books available on Project Gutenberg. Utilizing the BeautifulSoup library for HTML parsing and the requests library for HTTP requests, this script is designed to streamline the process of accessing and saving the literary content from one of the largest collections of free eBooks.

## Purpose

The script is intended for educational purposes, facilitating research, analysis, and accessibility of classic literary works. It is specifically crafted to extract text by chapters, making it suitable for analysis or digital formatting projects.

## Compliance with Project Gutenberg

The use of this script is in compliance with Project Gutenberg's `robots.txt`, which permits automated access to its resources. Users of this script are encouraged to conduct their scraping responsibly to avoid putting undue stress on Project Gutenberg's servers. It's recommended to make requests sparingly and considerately, adhering to best practices in web scraping etiquette.

## Customization and Usage

While the script is designed to work out of the box for most books on Project Gutenberg, adjustments might be necessary depending on the specific structure of the book's HTML page. Users may need to modify the script to target different HTML elements or classes that contain the book's text. The script includes comments and clear code structure to assist with these adjustments.

### Getting Started

To use this scraper:
1. Ensure Python 3.x is installed on your system.
2. Install required libraries using `pip install -r requirements.txt`.
3. Change the `page_to_scrape` URL in the script to match the URL of the book you wish to scrape. By default, it is set to scrape "Frankenstein" by Mary Shelley.
4. Run the script.
5. The extracted text will be saved in an output text file, organized by chapters.
