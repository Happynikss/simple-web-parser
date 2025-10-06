from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

URL = "https://inshorts.com/en/read"

def get_news():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(URL)

    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "span[itemprop='headline']"))
        )
    except TimeoutException:
        print("Не вдалося знайти заголовки на сторінці")
        driver.quit()
        return []

    news_list = []
    articles = driver.find_elements(By.CSS_SELECTOR, "span[itemprop='headline']")
    for article in articles:
        title = article.text
        # Шукаємо посилання на джерело, якщо є
        link_tags = article.find_elements(By.XPATH, "../../a[@class='source']")
        link = link_tags[0].get_attribute("href") if link_tags else "Немає джерела"
        if not any(news["title"] == title for news in news_list):
            news_list.append({"title": title, "link": link})

    driver.quit()
    return news_list

if __name__ == "__main__":
    news_items = get_news()
    if news_items:
        df = pd.DataFrame(news_items)
        df.to_csv("inshorts_news_selenium.csv", index=False)
        print("Новини збережено у inshorts_news_selenium.csv")
        print(f"Знайдено {len(news_items)} новин")
    else:
        print("Новини не знайдено")

