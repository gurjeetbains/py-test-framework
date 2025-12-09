import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage

load_dotenv()
web_url = os.getenv('WEB_URL')

def test_firstName_field(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.goto(web_url)
    registration_page.fill_first_name("Gurjeet321423423")  
    
    # Verify value
    actual_value = registration_page.get_first_name_value()
    assert actual_value == "Gurjeet321423423"
    assert actual_value.isalpha(), f"First name should contain only alphabets, but got: {actual_value}"