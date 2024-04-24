
from selenium.common.exceptions import ElementNotInteractableException

from utils.center import browser as driver
from selenium.webdriver.common.by import By

friend_list = [] 
index = 0

async def click_next_friend():
    global friend_list
    global index

    if len(friend_list) == 0:
        friend_list = await get_friend_lists()
        if len(friend_list) == 0:
            return

    if index >= len(friend_list):
        index = 0

    try:
        friend_list[index].click()
    except ElementNotInteractableException:
        pass

    index += 1


async def get_friend_lists():
    friends = driver.find_elements(By.CSS_SELECTOR, ".item-header-name--2tELM")
    return friends
    

