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
driver.get("https://owasp.org/www-project-top-ten/")

top_ten_link = driver.find_element(By.XPATH, "//a[contains(text(), 'OWASP Top Ten 2025')]")

top_ten_url = top_ten_link.get_attribute("href")
driver.get(top_ten_url)

print(driver.current_url)
print(driver.title)

# 3. Find 10 vilnarabilities
vulnarabilities = driver.find_elements(By.XPATH, "//a[contains(@href, 'A01_2025') or contains(@href, 'A02_2025') or contains(@href, 'A03_2025') or contains(@href, 'A04_2025') or contains(@href, 'A05_2025') or contains(@href, 'A06_2025') or contains(@href, 'A07_2025') or contains(@href, 'A08_2025') or contains(@href, 'A09_2025') or contains(@href, 'A10_2025')]")

# Create list
results = []

# Main loop
for vulnarability in vulnarabilities:
    name = vulnarability.text.strip()
    url = vulnarability.get_attribute("href")

    if name and url:
        result = {"name":name, "url":url}
        results.append(result)

print(results)

# Create DataFrame
results_df = pd.DataFrame(results)

# Write results to CSV
results_df.to_csv("owasp_top_10.csv", index=False)

driver.quit()

