# property_data_scraping

A Python-based web scraping toolkit for collecting property listing data from real estate platforms. Built with Selenium for dynamic page interaction and designed to be modular and extensible across multiple data sources.

---

## Table of Contents

- [Overview](#overview)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Data Sources](#data-sources)
- [Usage](#usage)
- [Output](#output)
- [Notes & Disclaimers](#notes--disclaimers)

---

## Overview

This project scrapes publicly available property listing data (prices, locations, acreage, etc.) from real estate websites for analysis and research purposes. The scraper handles JavaScript-rendered pages, pagination, and dynamic content loading.

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Selenium | Browser automation & dynamic content scraping |
| ChromeDriver | WebDriver for Chrome |
| pandas | Data cleaning and export |
| dotenv | Environment variable management |

---

## Project Structure

```
property-scraper/
│
├── scrapers/
│   ├── __init__.py
│   └── landsearch.py       # LandSearch.com scraper
│
├── data/
│   └── output/             # Scraped data saved here (CSV/JSON)
│
├── utils/
│   ├── __init__.py
│   └── driver.py           # Selenium WebDriver setup & helpers
│
├── .env.example            # Environment variable template
├── requirements.txt
├── main.py                 # Entry point
└── README.md
```

---

## Getting Started

### Prerequisites

- Python 3.7+
- Google Chrome installed
- ChromeDriver matching your Chrome version — download from [chromedriver.chromium.org](https://chromedriver.chromium.org/)

### Installation

```bash
# Clone the repository
git clone https://github.com/your-username/property-scraper.git
cd property-scraper

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

# Install dependencies
pip install -r requirements.txt
```

### Environment Variables

Copy `.env.example` to `.env` and fill in any required values:

```bash
cp .env.example .env
```

---

## Data Sources

### 1. LandSearch — Price History
- **URL:** https://www.landsearch.com/price
- **Status:** In Development
- **Data collected:** _(to be defined — e.g., listing price, acreage, location, date)_
- **Scraper:** `scrapers/landsearch.py`

> Additional sources will be added here as the project grows.

---

## Usage

```bash
# Run the main scraper
python main.py

# Run a specific source scraper (example)
python -m scrapers.landsearch
```

---

## Output

Scraped data is saved to the `data/output/` directory. Files are named by source and timestamp, e.g.:

```
data/output/landsearch_2025-05-07.csv
```

---

## Notes & Disclaimers

- This project is intended for **personal research and educational use only**.
- Always review a website's `robots.txt` and Terms of Service before scraping.
- Use reasonable request delays to avoid overloading servers.
- Do not redistribute scraped data without verifying applicable terms.
