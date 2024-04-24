from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import os

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_experimental_option('detach', True)
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser

def wait_login(browser):
    browser.get("https://creator.douyin.com/login")  # Adjust URL to the login page
    print("Please log in manually. Press Enter in the console once logged in.")
    ## TODO after login trigger the continue automatically, instead of users' input
    input()

def load_cookies(browser, path):
    if os.path.exists(path):
        browser.get("https://www.douyin.com")  # Navigate to the domain to set cookies for it
        with open(path, 'r') as cookiesfile:
            cookies = json.load(cookiesfile)
            for cookie in cookies:
                if 'expiry' in cookie:
                    del cookie['expiry']  # Selenium might not accept the expiry format
                browser.add_cookie(cookie)

def save_cookies(browser, path):
    # TODO save the login status
    cookies = browser.get_cookies() 
    with open(path, 'w') as file:
        json.dump(cookies, file)



browser = setup_browser()
wait_login(browser)


__all__ = ["browser"]


