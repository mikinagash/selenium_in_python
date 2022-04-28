from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep




def init():
    driver = webdriver.Chrome("..//Driver/chromedriver.exe")
    driver.get("https://atid.store/about/")
    driver.maximize_window()
    return driver



# function_that_trensfer_to_pages_by_click_the_links_on_top_logo_bar
def test_trensfer_to_page():
    driver = init()
    home = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[1]/a[1]")
    home.click()
    sleep(2)
    driver.back()
    store = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
    store.click()
    sleep(2)
    driver.back()
    man = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
    man.click()
    driver.back()
    sleep(2)
    women = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]")
    women.click()
    sleep(2)
    driver.back()
    accessories = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[5]/a[1]")
    accessories.click()
    sleep(2)
    driver.back()
    about = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[6]/a[1]")
    about.click()
    sleep(2)
    contuct_us = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[7]/a[1]")
    contuct_us.click()
    sleep(2)
    driver.back()





# def test_trensfer_to_page():
#     driver = init()
#     nav_bar = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]")
#     for i in nav_bar:
#         i.click()
#         driver.back()
#         sleep(3)






















