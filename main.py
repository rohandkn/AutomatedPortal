import os
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import csv
import os
cwd = os.getcwd()
print(cwd)

emails = []
urls = []
passwords = []


location = str(cwd)+'/chromedriver'
location = location.replace("\n'","")
print(location)
chromedriver = location
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
counter = 1
with open('links.csv', 'rt') as csvfile:
    spamreader = csv.DictReader(csvfile)
    for column in spamreader:
         emails.append(column['user'])
         passwords.append(column['pass'])
         urls.append(column['url'])


for item in urls:
    try:
        driver.execute_script("window.open('');")
        driver.switch_to.window(driver.window_handles[counter])
        driver.get(item)
        try:
            username1 = driver.find_elements_by_css_selector("input")
            username = username1[0]
            password = username1[1]

            username.send_keys(emails[counter-1])
            password.send_keys(passwords[counter-1])

            driver.find_element_by_css_selector("button").click()
            try:
                driver.switch_to.alert().accept()
            except:
                print("No Alert")
            print("Fully logged in for " + item)
        except:
            print("Unable to fully login for "+item+". Still, the website will still be loaded")
    except:
        print("Something weird went wrong")
    counter += 1










