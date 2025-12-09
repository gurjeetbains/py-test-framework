import os
from dotenv import load_dotenv
from pages.registration_page import RegistrationPage
from playwright.sync_api import expect

load_dotenv()
def test_register_user_with_all_data(page):
    """Test user registration flow"""
    web_url = os.getenv('WEB_URL')
    
    # Initialize page object
    registration_page = RegistrationPage(page)
    
    # Navigate to page
    registration_page.goto(web_url)
    
    # Fill form using fluent interface (method chaining)
    registration_page \
        .fill_first_name("Gurjeet") \
        .fill_last_name("Bains") \
        .fill_phone("0224704325") \
        .select_country("Belize") \
        .fill_email("sdc@fv.c") \
        .fill_password("12345678") \
        .click_register()
    
    # Assert success
    registration_page.is_success_message_visible()
    registration_page.check_if_first_name_is_same_as_entered("Gurjeet")
    registration_page.check_if_country_is_same_as_entered("Belize")
    registration_page.check_if_email_is_same_as_entered("sdc@fv.c")
    registration_page.check_if_last_name_is_same_as_entered("Bains")
    registration_page.check_if_phone_is_same_as_entered("0224704325")
    
def test_register_user_with_just_mandatory_data(page):
    """Test user registration flow"""
    web_url = os.getenv('WEB_URL')
    
    # Initialize page object
    registration_page = RegistrationPage(page)
    
    # Navigate to page
    registration_page.goto(web_url)
    
    # Fill form using fluent interface (method chaining)
    registration_page \
        .fill_last_name("Bains") \
        .fill_phone("0224704325") \
        .select_country("Belize") \
        .fill_email("sdc@fv.c") \
        .fill_password("12345678") \
        .click_register()
    
    # Assert success
    registration_page.is_success_message_visible()
    registration_page.check_if_last_name_is_same_as_entered("Bains")
    registration_page.check_if_phone_is_same_as_entered("0224704325")
    registration_page.check_if_country_is_same_as_entered("Belize")
    registration_page.check_if_email_is_same_as_entered("sdc@fv.c")

def test_register_button_should_display_warning(page):
    """Test user registration flow"""
    web_url = os.getenv('WEB_URL')
    
    # Initialize page object
    registration_page = RegistrationPage(page)
    
    # Navigate to page
    registration_page.goto(web_url)
    
    registration_page.click_register()
    
    # Assert success
    registration_page.is_password_error_visible()
    registration_page.fill_password("123")
    registration_page.click_register()
    registration_page.is_password_error_visible()
    registration_page.fill_password("123456")
    registration_page.click_register()
    registration_page.is_phone_error_visible()
    registration_page.fill_phone("dsfsdfcer3242")
    registration_page.click_register()
    registration_page.is_phone_error_visible()

