# Python script : sauce_demo 
# WebPageAutomation using Selenium
# Overview
This Python script utilizes the Selenium library to automate interactions with the **SauceDemo website  - https://www.saucedemo.com/**. It performs the following tasks:

**_1. Login to SauceDemo:_**
  Opens the URL https://www.saucedemo.com/.
  Logs in with the username "standard_user" and password "standard_user".

**2. Fetch Webpage Details:**__
  Retrieves information from the webpage, including the title, current URL, and entire webpage content.

**3. Save Webpage Content to File:**__
  Saves the fetched webpage content to a text file named "webpage_task_11.txt".

# Usage
_**1. Requirements:**_
a. Python 3.12.0 or higher.
b. Firefox browser.

_**2. Installation:**_
 Install the required Python packages using pip:
 pip install webdriver-manager
 
_**3. Execution:**_
  Run the Python script sauce_demo.py.

_**4. Output:**_
  The script will print the title, URL, and content of the SauceDemo webpage.
  The webpage content will be saved to a text file ("webpage_task_11.txt") in the script's directory.


# Note:
1. The script uses Firefox as the browser and requires an internet connection.
2. Ensure that geckodriver (Firefox WebDriver) is compatible with your Firefox version.


# Test Cases
# Python Automation Test script : test_sauce_demo.py 

**Title Tests:**
1. test_title_positive: Positive test case to ensure the fetched title matches "Swag Labs".
2. test_title_negative: Negative test case with an instance of an invalid URL to check the title fetching mechanism.

**URL Tests:**
1. test_fetch_url_positive: Positive test case to check if the fetched URL matches the expected SauceDemo URL.
2. test_fetch_url_negative: Negative test case with an instance of an invalid URL to verify the URL fetching mechanism.

**Page Source Tests:**
1. test_fetch_webpage_positive: Positive test case to check if a specific chunk is present in the page source.
2. test_fetch_webpage_negative: Negative test case with an instance of an invalid URL to check for the presence of an invalid string in the page source.

**Existence of File Test:**
1. test_webpage_source: Verifies the existence of the "webpage_task_11.txt" file and removes it after verification.

**Shutdown Test:**
test_shutdown: Checks if the shutdown function of the WebPageAutomation class returns True.

# Usage
1. Ensure you have pytest installed:
      pip install pytest
2. Run the pytest script:
      pytest test_sauce_demo.py
   
# Notes
The tests assume the existence of a valid SauceDemo website.
Ensure the geckodriver (Firefox WebDriver) is compatible with your Firefox version.
