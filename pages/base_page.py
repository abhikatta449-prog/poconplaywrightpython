from utils.highlighter import highlight

class BasePage:

    def __init__(self, page):
        self.page = page

    def click(self, locator):
        highlight(self.page, locator)
        self.page.locator(locator).click()

    def fill(self, locator, value):
        highlight(self.page, locator)
        self.page.locator(locator).fill(value)