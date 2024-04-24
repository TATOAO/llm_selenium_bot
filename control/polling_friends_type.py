from utils.center import browser as driver
from selenium.webdriver.common.by import By

friend_type_list = [] 
index = 0

async def click_next_friend_type():
    global friend_type_list
    global index

    if len(friend_type_list) == 0:
        friend_type_list = await get_friend_type_tags()
        if len(friend_type_list) == 0:
            return

    if index >= len(friend_type_list):
        index = 0

    friend_type_list[index].click()
    index += 1



async def get_friend_type_tags():
    tabs = driver.find_elements(By.CSS_SELECTOR, ".semi-tabs-tab")
    return tabs
    

