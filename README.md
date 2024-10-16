# wuzzuf.scraping-by-selenium


A Python project using Selenium to scrape job listings from the Wuzzuf website. The script searches for specific jobs, navigates through the pages, and extracts job titles and recruiters, saving the results to a CSV file.

## Table of Contents
- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions) 
- [How to Use](#how-to-use)
- [Project Structure](#project-structure)
- [Disclaimer](#disclaimer)

## Project Overview
This project uses Selenium WebDriver to scrape job postings from [Wuzzuf](https://wuzzuf.net/jobs/egypt). It searches for jobs by a given keyword, iterates through multiple pages, and extracts the job titles and recruiter names. The results are then stored in a CSV file for easy analysis.

## Technologies Used
- **Python**
- **Selenium WebDriver**
- **WebDriver Manager**
- **CSV for data storage**

## Setup Instructions

### Prerequisites
- **Python 3.x** installed on your system.
- **Web browser** (e.g., Mozilla Firefox) that matches the WebDriver.
- Required Python libraries installed.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yousefosamaali/Customer-Churn_Predict.git
   cd Customer-Churn_Predict
2.Install required Python packages:
pip install selenium webdriver-manager


3.Install the WebDriver Manager for Firefox: 
pip install webdriver-manager

# How to Use
1-Launch the Script:

Open a terminal or command prompt.
Run the script using:
python wuzzuf_scraper.py

 # 2-How it Works:

The script opens the Wuzzuf website.
Searches for the specified job title (e.g., "Engineer").
Iterates through the first 16 pages of job listings.
Extracts job titles and recruiters.
Saves the information to job_listings.csv.

# Project Structure

Wuzzuf-Job-Listings-Scraper/
├── wuzzuf_scraper.py
├── job_listings.csv
├── README.md


# Disclaimer
The data collected from Wuzzuf is used for educational purposes only.
Please ensure that scraping complies with Wuzzuf's terms of service.


### Additional Notes
- Ensure that `wuzzuf_scraper.py` matches the name of your script file.

This structure and content provide a comprehensive overview of your web scraping project and help guide users in setting up and using your script.
