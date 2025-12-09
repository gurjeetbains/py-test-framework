from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.expect = expect
        
    def goto(self, url: str):
        self.page.goto(url)
    
    def fill_field(self, selector: str, value: str):
        self.page.locator(selector).fill(value)
    
    def click_element(self, selector: str):
        self.page.locator(selector).click()
    
    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).text_content()