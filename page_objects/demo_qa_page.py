from playwright.sync_api import Page
from config.locators import *
import settings


class DemoQAPage:
    def __init__(self, page:Page):
        self.page = page
        self.login_button= LoginLocators.LOGIN_BUTTON
        self.username_field= LoginLocators.USERNAME_INPUT
        self.password_field = LoginLocators.PASSWORD_INPUT
        self.book_store_application_section = HomePageLocators.BOOK_STORE_APPLICATION_SECTION
        self.user_name= LoginLocators.USER_NAME
        self.log_out_button= LoginLocators.LOG_OUT_BUTTON
        self.book_store_section= BookStore.BOOK_STORE
        self.search_for_book = BookStore.SEARCH_BOOK
        self.book_title_anchor = BookStore.BOOK_TITLE_ANCHOR
        self.book_details_row = BookStore.ROW_FROM_BOOK_TITLE
        self.author_cell = BookStore.AUTHOR_CELL
        self.publisher_cell = BookStore.PUBLISHER_CELL

    def login(self):
        self.page.locator(self.login_button).click()
        self.page.locator(self.username_field).fill(settings.USERNAME)
        self.page.locator(self.password_field).fill(settings.PASSWORD)
        self.page.locator(self.login_button).click()
        self.page.locator(self.user_name).wait_for(state="visible")
        return self.page.locator(self.user_name).inner_text()

    def navigate_to_book_store_application(self):
        self.page.goto(settings.URL)
        self.page.locator(self.book_store_application_section).click()

    def log_out_button_availability(self):
        self.page.locator(self.log_out_button).wait_for(state="visible")
        assert self.page.locator(self.log_out_button).is_visible()

    def search_specific_book(self):
        self.page.locator(self.search_for_book).wait_for(state="visible")
        self.page.locator(self.search_for_book).fill(settings.BOOK_NAME)

        book_locator = self.page.locator(self.book_title_anchor.format(settings.BOOK_NAME))
        book_locator.wait_for(state="visible", timeout=5000)

        assert book_locator.is_visible(), f"Book '{settings.BOOK_NAME}' not found in search results"

        row_locator = self.page.locator(self.book_details_row.format(settings.BOOK_NAME)).first
        row_locator.wait_for(state="visible", timeout=5000)

        author = row_locator.locator(self.author_cell).text_content().strip()
        publisher = row_locator.locator(self.publisher_cell).text_content().strip()

        with open("book_info.txt", "w", encoding="utf-8") as file:
            file.write(f"Title: {settings.BOOK_NAME}\n")
            file.write(f"Author: {author}\n")
            file.write(f"Publisher: {publisher}\n")

    def user_log_out(self):
        self.page.locator(self.log_out_button).wait_for(state="visible")
        self.page.locator(self.log_out_button).click()
