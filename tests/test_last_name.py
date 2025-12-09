import os
from dotenv import load_dotenv
from playwright.sync_api import Page, expect
from pages.registration_page import RegistrationPage

load_dotenv()
web_url = os.getenv('WEB_URL')

def test_last_name_field(page: Page):
    registration_page = RegistrationPage(page)
    registration_page.goto(web_url)
    registration_page.fill_last_name("Bains")  
    
    # Verify value
    actual_value = registration_page.get_last_name_value()
    assert actual_value == "Bains"