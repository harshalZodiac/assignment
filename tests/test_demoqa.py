from page_objects.demo_qa_page import *
from conftest import *

class TestDemoQA:

    def test_demo_qa_login_user_name_and_logout_button(self, browser_page):
        demo_qa_pages = DemoQAPage(browser_page)

        demo_qa_pages.navigate_to_book_store_application()
        logged_in_user_name= demo_qa_pages.login()
        assert logged_in_user_name == settings.USERNAME

        demo_qa_pages.log_out_button_availability()

    def test_book_search(self, browser_page):
        demo_qa_pages = DemoQAPage(browser_page)

        demo_qa_pages.navigate_to_book_store_application()
        logged_in_user_name= demo_qa_pages.login()
        assert logged_in_user_name == settings.USERNAME

        demo_qa_pages.log_out_button_availability()
        demo_qa_pages.search_specific_book()
        demo_qa_pages.user_log_out()
