from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class ProfessionPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_course_price(self):
        return self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div.price-block__price"))
        ).text

    def add_to_bookmarks(self):
        bookmark_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.bookmark-button"))
        )
        bookmark_button.click()