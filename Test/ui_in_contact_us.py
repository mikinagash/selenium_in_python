from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep



def init():
    driver = webdriver.Chrome("..//Driver/chromedriver.exe")
    driver.get("https://atid.store/contact-us/")
    driver.maximize_window()
    return driver

def test_ui_for_top_of_the_page():
    driver = init()
    top = driver.find_element(By.XPATH,"//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert top == 'HOME\nSTORE\nMEN\nWOMEN\nACCESSORIES\nABOUT\nCONTACT US\nSearch\n0.00\xa0₪ 0'
    sleep(3)
    title = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[1]/div[2]/div[1]/div[1]/div[1]/div[1]/h1[1]").get_attribute("innerText")
    assert title == "Contact Us"


def test_ui_for_middle_of_the_page():
    driver = init()
    email = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[1]/span[2]").get_attribute("innerText")
    assert email == "hello@atid.store"
    phone = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[2]/span[2]").get_attribute("innerText")
    assert phone == "972-52-1234567"
    weekday = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[3]/span[2]").get_attribute("innerText")
    assert weekday == "Sunday to Thursday - 9:00 am to 7:00 pm"
    friday = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[4]/span[2]").get_attribute("innerText")
    assert friday == "Friday - 8:00 am to 3:00 pm"
    need_help = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[3]/div[1]/h4[1]").get_attribute("innerText")
    assert need_help == "Need Help? Call Us."
    help_number = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[1]/div[1]/div[4]/div[1]/h3[1]").get_attribute("innerText")
    assert help_number == "972-52-1234567"
    field_title = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]").get_attribute("innerText")
    assert field_title == ("Have any Queries? We're here to help.\n"'Name *\n''Single Line Text\n''Email *\n''Comment or Message *\n''SEND MESSAGE')

def test_ui_for_bottom_of_the_page():
    driver = init()
    bottom1 = driver.find_element(By.XPATH,"//body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div[1]/div[1]/div[1]/section[3]").get_attribute("innerText")
    assert bottom1 == "Worldwide Shipping\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Quality\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nBest Offers\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo.\n\nSecure Payments\n\nIt elit tellus, luctus nec ullamcorper mattis, pulvinar dapibus leo."
    bottom2 = driver.find_element(By.XPATH,"//body[1]/div[1]/footer[1]/div[1]/div[1]/div[1]").get_attribute("innerText")
    assert bottom2 == "Quick Links\nHome\nAbout\nCart\nContact Us\nFor Her\nWomen Jeans\nTops and Shirts\nWomen Jackets\nHeels and Flats\nWomen Accessories\nFor Him\nMen Jeans\nMen Shirts\nMen Shoes\nMen Accessories\nMen Jackets"
    bottom3 = driver.find_element(By.XPATH,"//body[1]/div[1]/footer[1]/div[2]").get_attribute("innerText")
    assert bottom3 == "Copyright © 2022 ATID Demo Store\n\nPowered by ATID College"



























