import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get('file:///Users/watanabeyuki/Desktop/type%20trainer/index.html')
driver.implicitly_wait(10)
pyautogui.moveTo(700,300)
pyautogui.click()
pyautogui.write('500')
pyautogui.moveTo(300,300)
pyautogui.click()


numJapanese = 0
while numJapanese < 10000:
  elementJapanese = driver.find_element(By.CLASS_NAME, 'sentence')
  textJapanese = elementJapanese.text
  pyautogui.write(textJapanese)
  numJapanese = numJapanese + 1
  