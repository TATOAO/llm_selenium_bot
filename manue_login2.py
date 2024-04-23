import time
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    browser = webdriver.Chrome(options=options)
    browser.maximize_window()
    return browser

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
    cookies = browser.get_cookies()
    with open(path, 'w') as file:
        json.dump(cookies, file)

def perform_task(browser):
    browser.get("https://creator.douyin.com/creator-micro/data/following/chat")
    print("Task performed at:", time.ctime())

    # Find all the tab elements
    tabs = browser.find_elements(By.CSS_SELECTOR, ".semi-tabs-tab")
    import ipdb;ipdb.set_trace()

    # Click each tab in order every 30 seconds
    for tab in tabs:
        tab.click()
        time.sleep(30)

def main():
    browser = setup_browser()
    cookies_path = './cookies.json'
    load_cookies(browser, cookies_path)

    if not browser.get_cookies():  # Check if cookies are loaded or not
        browser.get("https://creator.douyin.com/login")  # Adjust URL to the login page
        print("Please log in manually. Press Enter in the console once logged in.")
        input()

    try:
        while True:
            perform_task(browser)
    except KeyboardInterrupt:
        print("Exiting script and saving cookies...")
        save_cookies(browser, cookies_path)
        browser.quit()

if __name__ == '__main__':
    main()

