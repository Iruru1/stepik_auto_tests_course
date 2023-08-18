from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link="https://suninjuly.github.io/math.html"

try:
    browser=webdriver.Chrome()
    browser.get(link)
    textx=browser.find_element(By.ID,"input_value")
    x=textx.text
    answer=calc(x)
    textanswer=browser.find_element(By.ID,"answer")
    textanswer.send_keys(answer)
    textcheckbox=browser.find_element(By.ID,"robotCheckbox")
    textcheckbox.click()
    textradio=browser.find_element(By.ID,"robotsRule")
    textradio.click()
    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()    
    
    