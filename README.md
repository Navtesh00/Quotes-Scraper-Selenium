# 💬 Quotes Scraper — Selenium

A Python web scraper that extracts all quotes, authors, and tags from [quotes.toscrape.com/js](https://quotes.toscrape.com/js/) — a JavaScript-rendered site that cannot be scraped with `requests` alone.

---

## Why Selenium?

This site loads content dynamically with JavaScript. Standard `requests` + BeautifulSoup returns empty results. Selenium launches a real browser, executes the JavaScript, and then extracts the fully rendered content.

---

## What it does

- Launches Chrome in headless mode (no browser window)
- Waits for JS content to fully load before scraping
- Scrapes all quotes across all 10 pages by clicking the Next button
- Extracts quote text, author, and tags for each quote
- Saves output to both `quotes.csv` and `quotes.json`

---

## Output

`quotes.csv`:

| Text | Author | Tags |
|---|---|---|
| "The world as we have created it..." | Albert Einstein | change, deep-thoughts |
| "It is our choices, Harry..." | J.K. Rowling | choices |

---

## Tech Stack

- Python 3
- `selenium` — browser automation
- `webdriver-manager` — auto ChromeDriver setup
- `csv` + `json` — built-in, data export

---

## Setup

```bash
# Clone the repo
git clone https://github.com/Navtesh00/quotes-scraper-selenium.git
cd quotes-scraper-selenium

# Install dependencies
pip install selenium webdriver-manager

# Run
python scraper.py
```

Output files `quotes.csv` and `quotes.json` will be created in the same directory.

---

## Project Structure

```
quotes-scraper-selenium/
├── scraper.py      # main script
├── quotes.csv      # output (generated after running)
├── quotes.json     # output (generated after running)
└── README.md
```

---

## Key Concepts Used

- Headless Chrome with `ChromeOptions`
- `WebDriverWait` + `expected_conditions` for reliable element detection
- Next button click with staleness check before scraping next page
- `find_elements` with list comprehension for tag extraction
- Graceful loop exit when no Next button found

---

## Difference from Static Scraping

| | requests + BeautifulSoup | Selenium |
|---|---|---|
| Static HTML sites | ✅ Fast | ✅ Works but overkill |
| JS-rendered sites | ❌ Returns empty | ✅ Required |
| Speed | Fast | Slower (real browser) |
| Use case | Most sites | Dynamic / interactive sites |

---

## Notes

- `quotes.toscrape.com` is a sandbox site built for scraping practice
- Always check `robots.txt` before scraping real sites
- Headless mode makes the scraper run faster with no visible browser window

---

*Part of my web scraping portfolio — built to practice Selenium on JavaScript-rendered content.*
