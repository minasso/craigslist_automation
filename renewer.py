import pandas as pd
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#obtain login info
emails=pickle.load(open('email_info','rb'))
passwords = pickle.load(open('pword_info','rb'))

def renew(email, password):
    link='https://accounts.craigslist.org/login/home'
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element_by_id('inputEmailHandle').send_keys(email)
    driver.find_element_by_id('inputPassword').send_keys(password)
    driver.find_element_by_xpath('/html/body/section/section/div/div[1]/form/div[3]/button').click()
    i=0
    while i<30:
        i+=1
        try:
            driver.find_element_by_xpath('//*[@id="paginator"]/table/tbody/tr[{}]/td[2]/div/form[3]/input[3]'.format(i)).click()
            driver.execute_script("window.history.go(-1)")
        except:
            pass
    driver.close()
    return

for i in range(3):
    renew(emails[i],passwords[i])

