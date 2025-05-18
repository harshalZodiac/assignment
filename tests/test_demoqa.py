from page_objects.demo_qa_page import *
from conftest import *

class TestDemoQA:

    def test_demo_qa(self, browser_page):
        demo_qa_pages = DemoQAPage(browser_page)

        demo_qa_pages.navigate_to_book_store_application()
        demo_qa_pages.login()
