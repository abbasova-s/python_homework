# Task 1: Review robots.txt to Ensure Policy Compliance
# I have reviewed the policy compliance for the Durham County Library site and it appears as for general public (/User-agent: *) the only dissalowed section is /staff/

# Task 2: Understanding HTML and the DOM for the Durham Library Site
# Books - li.cp-search-result-item
# Title - span.title-content
# Authors - a.author-link
# Format and Year - div.cp-format-info span.display-info-primary

# Task 3: Write a Program to Extract this Data
# Initialization
import pandas as pd
import json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Driver configurations
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--window-size=1920x1080')

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), 
    options=options
)

# Fetching a web page
driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")


# 3. Find all the li elements in that page for the search list results
books = driver.find_elements(By.CSS_SELECTOR,'li.cp-search-result-item')

print("Number of books found:", len(books))

# 4. Create an empty list called results
results = []

# 5. Main loop
for book in books:
    # Find title
    title = book.find_element(By.CSS_SELECTOR, 'span.title-content').text

    # Find author/s
    authors = "; ".join(author.text for author in book.find_elements(By.CSS_SELECTOR, 'a.author-link'))

    # Find format and year
    format_year = book.find_element(By.CSS_SELECTOR, 'div.cp-format-info span.display-info-primary').text

    # Create a dictionary
    result = {
        "Title": title,
        "Author/s": authors,
        "Format-Year": format_year
    }

    # Add dictionary to results
    results.append(result)

#print(results)

# 6. Create a DataFrame from the results list
results_df = pd.DataFrame(results)

# Print the DataFrame
print(results_df)


# Task 4: Write out the Data
# 1. Write the DataFrame to a CSV file
results_df.to_csv("get_books.csv", index=False)

# 2. Write the results list to a JSON file
with open('get_books.json', 'w') as json_file:
    json.dump(results, json_file, indent=4)

driver.quit()