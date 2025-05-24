from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def search_courses(self, query):
        search_input = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.search__input"))
        )
        search_input.send_keys(query)
        search_button = self.driver.find_element(By.CSS_SELECTOR, "button.search__button")
        search_button.click()