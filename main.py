from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# --------------------------------
# Step0: Initial Webdriver Chrome (keep browser opening after code running completely)
ser = Service(r"C:\Users\Ba Truong Huu\Downloads\chromedriver_win32\chromedriver.exe")      #webdriver path
chrome_option = Options()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=ser,options=chrome_option)

# --------------------------------
# Step1: Login to Linkedin

url = 'https://www.linkedin.com/login'
driver.get(url)                                                                             #open URL
email_field = driver.find_element(By.ID, value='username')                                  #get email field by ID
email_field.send_keys('truongtam.vietdevils@gmail.com')                                     #fill email

password_field = driver.find_element(By.ID, 'password')                                     #get password field by ID
password_field.send_keys('123456aA@')                                                       #fill password

login_click_field = driver.find_element(By.XPATH,'//*[@id="organic-div"]/form/div[3]/button') #get login_click field by Xpath
login_click_field.click()                                                                   #click login

# --------------------------------
# Stepn: Quit driver
input('Bạn có muốn thoát không? Bấm enter')
driver.quit()



