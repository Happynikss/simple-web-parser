# Simple Web Parser: Парсер новин Inshorts

Цей проєкт демонструє, як проходить збір новин з сайту [Inshorts](https://inshorts.com/en/read) за допомогою **Selenium** та **headless Chrome**, а також зберігання їх у CSV-файл.

---

## Функціонал

- Парсинг **заголовків новин** та посилань на джерела (якщо доступно)  
- Збереження результатів у CSV (`inshorts_news_selenium.csv`)  
- Робота з **динамічним контентом**, який рендериться JavaScript  
- Headless режим браузера (без GUI)  

---

## Використані технології

- Python 3.9  
- Selenium  
- webdriver-manager (автоматичне встановлення ChromeDriver)  
- pandas (для збереження у CSV)  

---
