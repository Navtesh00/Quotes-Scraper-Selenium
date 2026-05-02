from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import csv 


options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://quotes.toscrape.com/js/")

wait = WebDriverWait(driver, 10)


with open("qoutes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["text", "author", "tags"])

    while True:
        qoutes = wait.until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "quote"))
        )
        print(len(qoutes))
        for qoute in qoutes:
            text = qoute.find_element(By.CLASS_NAME, "text").text
            author = qoute.find_element(By.CLASS_NAME, "author").text
            tags = qoute.find_elements(By.CLASS_NAME, "tag")
            tags = [tag.text for tag in tags]
            writer.writerow([text, author, tags])


        try:
            next_button = driver.find_element(By.PARTIAL_LINK_TEXT, "Next →")
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth'});", next_button)
            next_button.click()
        except Exception:
            break

driver.quit()
