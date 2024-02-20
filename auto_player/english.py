import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('file:///Users/watanabeyuki/Desktop/Type%20trainer/index.html')
pyautogui.moveTo(600,300)
pyautogui.click()

numEnglish = 0
while numEnglish < 10000:
  elementEnglish = driver.find_element(By.CLASS_NAME, 'sentenceEnglish')
  textEnglish = elementEnglish.text
  pyautogui.write(textEnglish)
  numEnglish = numEnglish + 1
  
