from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os

USER = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

chrome_driver_path = "C:\development\chromedriver-win64\chromedriver.exe"
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3673789741&distance=25&geoId=102257491&keywords"
           "=Marketing&refresh=true")
login = driver.find_element(By.XPATH, '/html/body/div[3]/a[1]')
time.sleep(5)
login.click()
user = driver.find_element(By.ID, "username")
user.send_keys(USER)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)

submit_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
submit_button.click()

job = driver.find_element(By.LINK_TEXT, 'Junior Strategist')
job.click()

time.sleep(5)
ez_apply = driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div['
                                         '1]/div[4]/div/div/div')
ez_apply.click()

phone_number = driver.find_element(By.XPATH, '//*[@id="single-line-text-form-component-formElement-urn-li-jobs'
                                             '-applyformcommon-easyApplyFormElement-3660045846-7174650087946148572'
                                             '-phoneNumber-nationalNumber"]')
phone_number.send_keys("3208821925")

submit_application = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
submit_application.click()

submit_application_2 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]/span')
submit_application_2.click()

submit_application_3 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
submit_application_3.click()

submit_application_4 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
submit_application_4.click()

submit_application_5 = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
submit_application_5.click()

review_application = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
review_application.click()

send_application = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div[2]/div/footer/div[3]/button[2]')
send_application.click()
