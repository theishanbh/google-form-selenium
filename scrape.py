from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

# path to the chromedriver
driver_path = './chromedriver.exe'  
# form url
form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSdUCd3UWQ3VOgeg0ZzNeT-xzNawU8AJ7Xidml-w1vhfBcvBWQ/viewform'  

# setting up executable path
service = Service(executable_path=driver_path)

options = webdriver.ChromeOptions()
# this argument allows to open chrome in user profile itself
options.add_argument('user-data-dir=C:\\Users\\yojay\\AppData\\Local\\Google\\Chrome\\User Data\\')

# Initialize the WebDriver
driver = webdriver.Chrome(options=options)

# Open the Google Form
driver.get(form_url)

# Allow the page to load
time.sleep(2)

# field filling fucntion
def fill_field(data,xpath,driver=driver):
    field = driver.find_element(By.XPATH, xpath)
    field.send_keys(data)
    time.sleep(2)

# name fill
fill_field('Ishan Bhardwaj','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
# contact number fill
fill_field('9958963733','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
# email fill
fill_field('theishanbh@gmail.com','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
# address fill
fill_field('South Extension, New Delhi, India', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div[2]/textarea')
# pincode fill
fill_field('110003','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
# dob fill
fill_field('23112002','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
# gender fill
fill_field('Male','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div/div[1]/input')
# code fill
fill_field('GNFPYC','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[8]/div/div/div[2]/div/div[1]/div/div[1]/input')


time.sleep(3)

# Submit the form
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div').click()
# submit_button.click()

# Wait for a while to ensure the form is submitted
time.sleep(5)

# successful
print("Google form submitted successfully")


# Close the WebDriver
driver.quit()
