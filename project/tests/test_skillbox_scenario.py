# tests/test_skillbox_scenario.py
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSkillboxScenario:
    def test_automation_engineer_course_scenario(self, setup):
        driver = self.driver
        wait = WebDriverWait(driver, 30)

        try:

            driver.get("https://skillbox.ru")


            search_input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "input[type='search']"))
            )
            search_input.send_keys("Автотесты на Python")

            search_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            search_button.click()


            novice_filter = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[contains(text(), 'Для новичков')]"))
            )
            novice_filter.click()


            profession = wait.until(
                EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Инженер по автоматизации тестирования"))
            )
            profession.click()


            price = wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "div.price-block"))
            ).text
            assert price, "Цена не отображена"


            bookmark = driver.find_element(By.CSS_SELECTOR, "button.bookmark")
            bookmark.click()

        except Exception as e:
            driver.save_screenshot("error.png")
            pytest.fail(f"Тест упал с ошибкой: {str(e)}")