from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def ruparse_timer():
    URL = "https://worldnomadgames.kz/ru"

    # Настроим Selenium WebDriver в headless режиме
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запуск браузера в фоновом режиме
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    try:
        driver.get(URL)
        # Явное ожидание, пока элемент с классом 'timer__content' станет доступен
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "timer__content"))
        )

        # Сделаем паузу для обеспечения полной загрузки контента


        # Получение страницы после полной загрузки
        soup = BeautifulSoup(driver.page_source, "html.parser")
        post = soup.find("div", class_="timer__content")

        if post:
            title = post.find("h3", class_="timer__title").text.strip()
            timer = post.find("span", class_="timer__info-number").text.strip()
            text = post.find("span", class_="timer__info-text").text.strip()
            return f"{title} {timer} {text}"
        else:
            return "Обратный отсчет не найден"
    finally:
        driver.quit()