from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

def init():
    driver = webdriver.Chrome("..//Driver/chromedriver.exe")
    driver.get("https://atid.store/about/")
    driver.maximize_window()
    return driver

#function that chacking if the ui of the top page of  is comptiable  with the design document
def test_ui_for_top_of_the_page():
    driver = init()
    top = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert top == 'HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00\xa0₪ 0'
    title = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h1[1]").get_attribute("innerText")
    assert  title == "About Us"


def test_ui_for_middle_of_the_page():
    driver = init()
    left_side = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/section[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert left_side == "Who We Are\n\nATID Demo Store was created by ATID College dedicated employees. This is a complete demo site for practicing QA & Test Automation methodologies. Don't think for a second you can actually buy here something cause you can't ! This Demo Store contains software bugs which were put intentionally and your job is to locate them Good luck falks, Yoni Flenner - ATID College"
    title1 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[2]/div[1]/h4[1]").get_attribute("innerText")
    assert title1 == 'A Few Words About'
    title2 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[3]/div[1]").text
    assert title2 == "Our Team\nWe have the best team ever everybody who is somebody wants to work with us, so we can afford cherry-picking them, one by one..."
    title3 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[4]/div[2]/div[1]/div[1]/div[2]/div[1]/h2[1]").text
    assert title3 == "Follow Us"


def test_ui_for_bottom_of_the_page():
    driver = init()
    bottom1 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[5]").get_attribute("innerText")
    sleep(3)
    assert bottom1 == "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
    bottom2 = driver.find_element(By.XPATH,"//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert bottom2 == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets"
    bottom3 = driver.find_element(By.XPATH,"//body[1]/div[1]/footer[1]/div[2]").get_attribute("innerText")
    assert bottom3 == "Copyright © 2022 ATID Demo Store\n\nPowered by ATID College"
















