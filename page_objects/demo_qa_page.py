from playwright.sync_api import Page
from config.locators import LoginLocators, HomePageLocators
import settings


class DemoQAPage:
    def __init__(self, page:Page):
        self.page = page
        self.login_button= LoginLocators.LOGIN_BUTTON
        self.username_field= LoginLocators.USERNAME_INPUT
        self.password_field = LoginLocators.PASSWORD_INPUT
        self.book_store_application_section = HomePageLocators.BOOK_STORE_APPLICATION_SECTION

    def login(self):
        # self.page.goto(settings.URL)
        self.page.locator(self.username_field).fill(settings.USERNAME)
        self.page.locator(self.password_field).fill(settings.PASSWORD)
        self.page.locator(self.login_button).click()

    def navigate_to_book_store_application(self):
        self.page.goto(settings.URL)
        self.page.locator(self.book_store_application_section).click()

