import random
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from cowpy import cow
import random
import string
import undetected_chromedriver.v2 as uc


try:
    driver = uc.Chrome()

    #открываем страницу для регистрации новой почты GMAIL
    driver.get(
        "https://accounts.google.com/signup"
        )
    time.sleep(5)

    #генерируем имя
    name = ''.join([random.choice(string.ascii_lowercase) for n in range(8)])

    #записываем имя
    my_name = driver.find_element(By.ID, 'firstName')
    my_name.clear()
    my_name.send_keys(name)
    time.sleep(3)
    
    #генерируем фамилию
    surname = ''.join([random.choice(string.ascii_lowercase) for n in range(8)])

    #записываем фамилию
    my_surname = driver.find_element(By.ID, 'lastName')
    my_surname.clear()
    my_surname.send_keys(surname)
    time.sleep(3)

    #генерируем логин
    username = ''.join([random.choice(string.ascii_letters + string.digits  ) for n in range(12)])

    #записываем логин
    my_username = driver.find_element(By.ID, 'username')
    my_username.clear()
    my_username.send_keys(username)
    time.sleep(5)

    #генерируем пароль
    password = ''.join([random.choice(string.ascii_letters + string.digits  ) for n in range(8)])

    #записываем пароль
    passw = driver.find_element(By.NAME, 'Passwd')
    passw.clear()
    passw.send_keys(password)
    time.sleep(3)

    #повторяем в конфирм
    confirm_passw = driver.find_element(By.NAME, 'ConfirmPasswd')
    confirm_passw.clear()
    confirm_passw.send_keys(password)
    time.sleep(3)

    #жмем на кнопку 'далее'
    next_button = driver.find_element(By.ID, "accountDetailsNext").click()
    time.sleep(15)


    next_button2 = driver.find_element(By.ID, "passp:sign-in").click()
    time.sleep(5)

    mail = driver.find_element(By.CLASS_NAME, "mail-ComposeButton-Text").click()
    time.sleep(10)

    recipient = driver.find_element(By.CLASS_NAME, "composeYabbles")
    recipient.clear()
    recipient.send_keys("cto@groscloud.com")
    time.sleep(2)

    title = driver.find_element(By.CLASS_NAME, "composeTextField ComposeSubject-TextField")
    title.clear()
    title.send_keys("Это те самые дроиды, которых вы ищите!")
    time.sleep(3)

    letter = driver.find_element(By.ID, "cke_wysiwyg_div cke_reset cke_enable_context_menu cke_editable cke_editable_themed cke_contents_ltr cke_htmlplaceholder")
    letter.clear()
    letter.send_keys("Это те самые дроиды, которых вы ищите! Хамерзаев Мансур Мусаевич, +79389926611, телеграм(@mahamerz)")
    time.sleep(3)

    binder = driver.find_element(By.XPATH, "//input[@type='file']")
    binder.send_keys('/home/mahamerz/Рабочий стол/проекты/tz_kitchen')
    time.sleep(5)

except Exception as ex:
    cheese = cow.Moose()
    msg = cheese.milk("Упс.. Произошла ошибка! Свяжитесь с автором данного скрипта для решения проблемы!")
    print(msg)

finally:
    driver.close()
    driver.quit()