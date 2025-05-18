class LoginLocators:
    LOGIN_BUTTON = '[id="login"]'
    USERNAME_INPUT = '[placeholder="UserName"]'
    PASSWORD_INPUT = '[placeholder="Password"]'
    USER_NAME = '[id="userName-value"]'
    LOG_OUT_BUTTON = '//button[@type="button" and text()="Log out"]'

class HomePageLocators:
    BOOK_STORE_APPLICATION_SECTION = '//h5[text()="Book Store Application"]'

class BookStore:
    BOOK_STORE = '//span[@class="text" and text()="Book Store"]'
    SEARCH_BOOK = '[placeholder="Type to search"]'
    BOOK_TITLE_ANCHOR = "a:has-text('{}')"
    ROW_FROM_BOOK_TITLE = "//a[text()='{}']/ancestor::div[contains(@class, 'rt-tr')]"
    AUTHOR_CELL = "div.rt-td:nth-child(3)"
    PUBLISHER_CELL = "div.rt-td:nth-child(4)"