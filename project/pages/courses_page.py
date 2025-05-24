from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CoursesPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def filter_by_level(self, level):
        level_filter = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, f"//div[contains(@class, 'filter-item') and contains(., '{level}')]"))
        )
        level_filter.click()

    def select_profession(self, profession_name):
        profession_link = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//a[contains(@class, 'course-card') and contains(., '{profession_name}')]"))
        )
        profession_link.click()