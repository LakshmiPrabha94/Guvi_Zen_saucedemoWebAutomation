#Name: Lakshmi Prabha
#Program : 
"""
Visit the url, https://www.saucedemo.com/ and login with the following credentials
username = "standard_user"
password = "standard_user"
Try to fetch the following using Python Selenium
1. Title of the webpage
2. Current URL of the webpage 
3. Extract the entire contents of the webpage and save it in a Text file whose name will be "Webpage_task_11.txt"
"""
#Date : 14 Jan 2024
#Version: 1
#Python Version: 3.12.0


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class WebPageAutomation:
    def __init__(self, url, username, password):
        # Initialize the WebPageAutomation instance with URL, username, and password
        self.url = url
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

    def booting_function(self):
        try:
            # Maximize window and navigate to the specified URL
            self.driver.maximize_window()
            self.driver.get(self.url)
            return True
        except Exception as e:
            # Handle exception if unable to start the browser
            print(f"ERROR: Unable to start the browser: {e}")
            return False

    def shutdown(self):
        # Quit the browser and return True indicating successful shutdown
        self.driver.quit()
        return True

    def login(self):
        try:
            print("Navigated to Saucedemo webpage!!!")

            # Wait for the visibility of the username element and fill in the username
            username_locator = "user-name"
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, username_locator)))
            self.driver.find_element(by=By.ID, value=username_locator).send_keys(self.username)
            print("Username filled")

            # Fill in the password
            password_locator = "password"
            self.driver.find_element(by=By.ID, value=password_locator).send_keys(self.password)
            print("Password filled")

            # Click on the login button
            login_locator = "login-button"
            self.driver.find_element(by=By.ID, value=login_locator).click()
            print("Login Button clicked")

            self.driver.find_element(by=By.ID, value=username_locator).send_keys(self.username)

        except Exception as e:
            # Handle exception if something goes wrong with locators
            print("ERROR: Something went wrong with Locators! Details:", str(e))

    def fetch_title(self):
        # Call booting_function before fetching the title
        self.booting_function()
        return self.driver.title

    def fetch_url(self):
        # Fetch the current URL without calling booting_function
        self.booting_function()
        self.login()
        return self.driver.current_url

    def fetch_webpage(self):
        # Fetch the page source without calling booting_function
        return self.driver.page_source
         

# Initializing values
url = "https://www.saucedemo.com/"
username = "standard_user"
password = "standard_user"

# Creating an instance of WebPageAutomation
sauce_demo = WebPageAutomation(url, username, password)

if sauce_demo.booting_function():
    # Logging in
    sauce_demo.login()

    # Task 1: Fetch and print the title
    print("Title of the webpage:", sauce_demo.fetch_title())
    print()

    # Task 2: Fetch and print the URL
    print("URL of the webpage:", sauce_demo.fetch_url())
    print()

    # Task 3: Fetch and print the content of the webpage
    print("The content of the Web page is:", sauce_demo.fetch_webpage())
    print()

    # Task 4: Save content to a file
    with open("webpage_task_11.txt", "w", encoding="utf-8") as file:
        file.write(sauce_demo.fetch_webpage())
    
    # Close the browser
    sauce_demo.shutdown()
    print("See you soon!!!")
