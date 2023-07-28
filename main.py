import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
#Enter Your Login Email For Your Facebook Account
myemail="example@gmail.com"
#Enter Your Login Password For Your Facebook Account
mypass="1234"
#Enter The Path To Your Driver
service = Service(r"C:\Users\User\Selenium Driver\chromedriver.exe")
driver= webdriver.Chrome(service=service)
driver.get(r"https://tinder.com/app/recs")
time.sleep(2)
login_el = driver.find_element(By.XPATH,'//*[@id="q-1470728188"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_el.click()
time.sleep(3)
try:
    facebook_el= driver.find_element(By.CSS_SELECTOR,'button[aria-label="Log in with Facebook"]')
    facebook_el.click()
    
except:
    more_el= driver.find_element(By.XPATH,'//*[@id="q1095858032"]/main/div/div[1]/div/div/div[3]/span/button')
    more_el.click()
    facebook_el= driver.find_element(By.CSS_SELECTOR,'button[aria-label="Log in with Facebook"]')
    facebook_el.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
email_el= driver.find_element(By.CSS_SELECTOR,'input[name=email]')
email_el.send_keys(myemail)
time.sleep(1)
pass_el = driver.find_element(By.CSS_SELECTOR,'input[type=password')
pass_el.send_keys(mypass)
pass_el.submit()
time.sleep(5)
driver.switch_to.window(base_window)
time.sleep(2)
allow_el = driver.find_element(By.XPATH,'//*[@id="q1095858032"]/main/div/div/div/div[3]/button[1]')
allow_el.click()
time.sleep(2)
enable_el= driver.find_element(By.XPATH,'//*[@id="q1095858032"]/main/div/div/div/div[3]/button[2]')
enable_el.click()
time.sleep(2)
accept_el=driver.find_element(By.XPATH,'//*[@id="q-1470728188"]/div/div[2]/div/div/div[1]/div[1]/button')
accept_el.click()
time.sleep(6)
for i in range(20):
    keyboard = Controller()
    keyboard.press(Key.right)
    keyboard.release(Key.right)
    time.sleep(2)
