## Day 45 – Top 100 Movies Web Scraper 🎬🌐

### Overview
This project is a Python-based web scraper that extracts the list of the **Top 100 Movies of All Time** from a webpage and saves the results into a text file.

It demonstrates how to retrieve, parse, and process real-world web data using Python.

---

### Tech Stack
- Python
- requests
- BeautifulSoup (bs4)

---

### Features
- Fetches webpage content using HTTP requests  
- Parses HTML using BeautifulSoup  
- Extracts movie titles from structured HTML elements  
- Reorders the list to match correct ranking order  
- Stores the output in a text file  

---

### How It Works
1. Sends a request to the target URL  
2. Parses the HTML content  
3. Extracts all movie titles using:
   ```python
   soup.find_all(name="h3", class_="title")
4. Converts the extracted elements into a list of text
5. Reverses the list to maintain ranking from 1 to 100
6. Writes the final list into movies.txt

---
### Output

A file named movies.txt is generated, containing the list of movies in correct ranked order.

---
### Key Learnings
- Basics of web scraping using Python
- Parsing and navigating HTML structures
- Extracting and processing data efficiently
- Writing data to files

---

### Future Improvements
- Add error handling for failed requests
- Extract additional details (year, ratings, etc.)
- Export data in CSV or JSON format
- Build a simple UI to display results