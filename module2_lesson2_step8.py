from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

try:
    browser=webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    first=browser.find_element(By.NAME,"firstname")
    first.send_keys("Ирина")
    last=browser.find_element(By.NAME,"lastname")
    last.send_keys("Иванова")
    email=browser.find_element(By.NAME,"email")
    email.send_keys("ira@mail.ru")
    load=browser.find_element(By.ID,"file")
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file_for_module2_lesson2_step8.txt')           # добавляем к этому пути имя файла 
    load.send_keys(file_path)
    button=browser.find_element(By.CSS_SELECTOR,"button.btn")
    button.click()
  
finally:
    time.sleep(10)
    browser.quit()

    
    