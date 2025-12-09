from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class RegistrationPage(BasePage):
    # Locators
    FIRST_NAME= "First Name"
    LAST_NAME = "Last Name* Phone nunber*"
    PHONE = "Enter phone number"
    COUNTRY_DROPDOWN = "#countries_dropdown_menu"
    EMAIL = 'Enter email'
    PASSWORD = 'Password'
    REGISTER_BTN = 'Register'
    RESULTS_SECTION = '#results-section'
    RESULTS_BANNER = '#message'
    RESULT_FIRSTNAME= '#resultFn'
    RESULT_LASTNAME= '#resultLn'
    RESULT_PHONE= '#resultPhone'
    RESULT_COUNTRY= '#country'
    RESULT_EMAIL= '#resultEmail'
    
    # Texts that need to be verified
    SUCCESS_TEXT = "Successfully registered the following information"
    PASSWORD_ERROR_TEXT = "The password should contain between [6,20] characters!"
    PHONE_ERROR_TEXT = "The phone number should contain at least 10 characters!"
    
    
    def fill_first_name(self, name: str):
        self.page.get_by_role("textbox", name=self.FIRST_NAME).fill(name)
        return self
    
    def fill_last_name(self, name: str):
        self.page.get_by_role("textbox", name=self.LAST_NAME).fill(name)
        return self
    
    def fill_phone(self, phone: str):
        self.page.get_by_role("textbox", name=self.PHONE).fill(phone)
        return self
    
    def select_country(self, country: str):
        self.page.locator(self.COUNTRY_DROPDOWN).select_option(country)
        return self
    
    def fill_email(self, email: str):
        self.page.get_by_role("textbox", name=self.EMAIL).fill(email)
        return self
    
    def fill_password(self, password: str):
        self.page.get_by_role("textbox", name=self.PASSWORD).fill(password)
        return self
    
    def click_register(self):
        self.page.get_by_role("button", name=self.REGISTER_BTN).click()
        return self
    
    def get_first_name_value(self) -> str:
        return self.page.get_by_role("textbox", name=self.FIRST_NAME).input_value()    
    
    def get_last_name_value(self) -> str:
        return self.page.get_by_role("textbox", name=self.LAST_NAME).input_value()
    
    def get_phone_value(self) -> str:
        return self.page.get_by_role("textbox", name=self.PHONE).input_value()

    def get_email_value(self) -> str:
        return self.page.get_by_role("textbox", name=self.EMAIL).input_value()
    
    def is_success_message_visible(self):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_be_visible()
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_contain_text(self.SUCCESS_TEXT)
    
    def check_if_first_name_is_same_as_entered(self, name: str):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULT_FIRSTNAME)).to_contain_text(name)
        
    def check_if_last_name_is_same_as_entered(self, name: str):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULT_LASTNAME)).to_contain_text(name)
    
    def check_if_phone_is_same_as_entered(self, phone: str):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULT_PHONE)).to_contain_text(phone)
    
    def check_if_country_is_same_as_entered(self, country: str):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULT_COUNTRY)).to_contain_text(country)
        
    def check_if_email_is_same_as_entered(self, email: str):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULT_EMAIL)).to_contain_text(email)
    
    def is_password_error_visible(self):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_be_visible()
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_contain_text(self.PASSWORD_ERROR_TEXT)
    
    def is_phone_error_visible(self):
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_be_visible()
        self.expect(self.page.locator(self.RESULTS_SECTION).locator(self.RESULTS_BANNER)).to_contain_text(self.PHONE_ERROR_TEXT)