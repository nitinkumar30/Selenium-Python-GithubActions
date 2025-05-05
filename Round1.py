# The task is to open the Mathup website, click the "Start" button and record the difficulty level of the game in the
# terminal. This process should be repeated for ten times from opening of the “Mathup” website, hitting the "Start"
# button and noting the difficulty level for each time.


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://mathup.com/games/crossbit?mode=championship"
startXpath = "//div[text()='Start']"
difficultyXpath = "//div[text()='Difficulty']/ancestor::div[@class='GamePostStart_info__Rwi7G']//div[@class='GamePostStart_value__zH0b9']"

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--headless')  # optional with xvfb
chrome_options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=chrome_options)

try:
    for i in range(10):
        driver.get(URL)

        # Wait for the Start button
        WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.XPATH, startXpath))
        ).click()

        # Wait for difficulty level to be visible
        difficulty_element = WebDriverWait(driver, 15).until(
            EC.visibility_of_element_located((By.XPATH, difficultyXpath))
        )
        difficulty_level = difficulty_element.text

        print(f"Difficulty level for round {i + 1}: {difficulty_level}")

finally:
    driver.quit()

