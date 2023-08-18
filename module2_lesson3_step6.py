from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/redirect_accept.html")
    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    new_window=browser.window_handles[1]
    browser.switch_to.window(new_window)
    textx=browser.find_element(By.ID,"input_value")
    x=textx.text
    answer=calc(x)
    textanswer=browser.find_element(By.ID,"answer")
    textanswer.send_keys(answer)
    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
    
  
finally:
    time.sleep(10)
    browser.quit()

    
    