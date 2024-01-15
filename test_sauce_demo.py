import pytest
from sauce_demo import WebPageAutomation
from selenium.webdriver.common.by import By
import os

# Initialize the variables that are common to all functions
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "standard_user"

# Create an instance of WebPageAutomation for testing
saucedemo_website = WebPageAutomation(url, username, password)

# Test cases to test the Title of the webpage
# 1. Positive test case
def test_title_positive():
    assert saucedemo_website.fetch_title() == "Swag Labs"
# 2. Negative test case
def test_title_negative():
    # Create an instance with an invalid URL
    invalid_url = "https://invalid-url"
    saucedemo_website_invalid = WebPageAutomation(invalid_url, username, password)
    assert saucedemo_website_invalid.fetch_title() == "Swag Labs"

# Test cases to test the URL of the webpage
# 1. Positive test case
def test_fetch_url_positive():
    test_url = "https://www.saucedemo.com/"
    assert saucedemo_website.fetch_url() == test_url
# 2. Negative test case
def test_fetch_url_negative():
    # Create an instance with an invalid URL
    invalid_url = "https://%^invalid-url$%"
    saucedemo_website_invalid = WebPageAutomation(invalid_url, username, password)
    assert saucedemo_website_invalid.fetch_url() == invalid_url

# Test cases to test the page source
# 1. Positive test case
def test_fetch_webpage_positive():
    # Check if a specific chunk is present in the page source
    assert "02e67e.chunk.j" in saucedemo_website.fetch_webpage()
# 2. Negative test case
def test_fetch_webpage_negative():
    # Create an instance with an invalid URL
    invalid_url = "https://invalid-url"
    saucedemo_website_invalid = WebPageAutomation(invalid_url, username, password)
    # Fetch the page source and check if an invalid string is present
    page_source = saucedemo_website_invalid.fetch_webpage()
    assert "7e.£%^$£" in page_source

# Test case to check the existence of a file
def test_webpage_source():
    # Verify if the file exists
    assert os.path.exists("webpage_task_11.txt")
    # Remove the file after verification
    os.remove("webpage_task_11.txt")


# Test case to check if the shutdown function returns True
def test_shutdown():
    assert saucedemo_website.shutdown() == True







