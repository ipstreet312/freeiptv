import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

url = "https://www.fox.com.tr/canli-yayin"

# Set up a headless browser with Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

# Load the page with Selenium
driver.get(url)

# Extract the content after dynamic modifications
html_content = driver.page_source

# Close the browser
driver.quit()

# Parse HTML using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Find the script tag containing the desired URL
script_tag = soup.find('script', {'type': 'text/javascript'})
print("Script Content:", script_tag.text)

# Adjust the regular expression to handle variations
url_match = re.search(r"daiUrl\s*:\s*['\"]([^'\"]+)['\"]", script_tag.text, re.DOTALL)
if url_match:
    dai_url = url_match.group(1)
    print("Retrieved URL:", dai_url)
else:
    print("URL not found in the script.")
