from selenium import webdriver #импорт библиотеки webdriver для работы с браузером
from selenium.webdriver.common.by import By #импорт библиотеки By для запросов поиска
from selenium.webdriver.support.ui import Select #импорт библиотеки  Select  для упрощения выблоа эелемнтов списка
import time #импорт библиотеки времени

link="https://suninjuly.github.io/selects1.html"

try:
    browser=webdriver.Chrome()  #открытие хрома
    browser.get(link) #открытие нужной страницы
    stnum1=browser.find_element(By.ID,"num1") #поиск строки с первым числом
    num1=int(stnum1.text) #определяем первое число
    stnum2=browser.find_element(By.ID,"num2")#поиск строки со вторым числом
    num2=int(stnum2.text)#определяем второе число
    summa=num1+num2 #определяем сумму чисел
    drop=browser.find_element(By.ID,"dropdown") #поиск строки с выпадающим списком
    select = Select(browser.find_element(By.TAG_NAME, "select")) #инициализация объекта списка
    select.select_by_visible_text(str(summa)) #поиск элемента спсика с нужной  суммой
    button=browser.find_element(By.CSS_SELECTOR,"button.btn") #поиск строки кнопки
    button.click() #нажатие кнопки
    
finally:
    time.sleep(10) #задержка 
    browser.quit() #закрытие хрома   
    
    