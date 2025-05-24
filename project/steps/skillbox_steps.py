from pages.main_page import MainPage
from pages.courses_page import CoursesPage
from pages.profession_page import ProfessionPage


class SkillboxSteps:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.courses_page = CoursesPage(driver)
        self.profession_page = ProfessionPage(driver)

    def open_main_page(self):
        self.main_page.driver.get("https://skillbox.ru")

    def search_courses(self, query):
        self.main_page.search_courses(query)

    def filter_courses_by_level(self, level):
        self.courses_page.filter_by_level(level)

    def select_profession(self, profession_name):
        self.courses_page.select_profession(profession_name)

    def get_profession_price(self):
        return self.profession_page.get_course_price()

    def save_course_to_bookmarks(self):
        self.profession_page.add_to_bookmarks()