from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
driver = webdriver.Chrome(options=options)
driver.get("https://popcat.click/")

image=driver.find_element_by_class_name("cat-img.p")

while True:
    image.click()
    time.sleep(0.038)