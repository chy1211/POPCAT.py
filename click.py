from selenium import webdriver
import tkinter as tk
from tkinter import Button
import time

def start():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://popcat.click/")
    image=driver.find_element_by_class_name("cat-img.p")
    while True:
        image.click()
        time.sleep(0.038)

win = tk.Tk()

win.title("POPCAT!!!!")

btn_start = Button(text="開始", command=start)
btn_start.grid(column=0, row=0)

win.mainloop()