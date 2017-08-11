
#reload dataframe with cols: location, url, zip_code, ad_type
import pandas as pd
import pickle
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
df=pd.read_pickle('clist_df')

#obtain login info and ad content
emails=pickle.load(open('email_info','rb'))
passwords = pickle.load(open('pword_info','rb'))
post_title = pickle.load(open('post_title','rb'))
ad=pickle.load(open('ad_info','rb'))

col_towns = df[df['ad_type']=='col']
col=list(col_towns.index)
# col

hs_towns = df[df['ad_type']=='hs']
hs= list(hs_towns.index)
hs

phone_number='631-923-5030'
contact_name='Andrew'

#function to post to particular location
def post(loc, email, password):
    link=df['url'][loc]
    zipcode=df['zip_code'][loc]
    driver = webdriver.Chrome()
    driver.get(link)
    driver.find_element_by_id('post').click()
    driver.find_element_by_xpath('/html/body/article/section/form/ul/li[10]/label/span[2]').click()
    driver.find_element_by_xpath('/html/body/article/section/form/ul/li[13]/label/span[2]').click()
    driver.find_element_by_id('inputEmailHandle').send_keys(email)
    driver.find_element_by_id('inputPassword').send_keys(password)
    driver.find_element_by_xpath('/html/body/article/section/div/div[1]/form/div[3]/button').click()
    try:
        driver.find_element_by_id('PostingTitle').send_keys(post_title)
    except:
        #for those locations with an extra landing page, just choose the first sublocation
        #consider discovering ones w extra page and looping thru sublocations
        driver.find_element_by_xpath('/html/body/article/section/form/ul/li[1]/label').click()
        driver.find_element_by_id('PostingTitle').send_keys(post_title)
    driver.find_element_by_id('postal_code').send_keys(zipcode)
    driver.find_element_by_id('PostingBody').send_keys(ad)
    # driver.find_element_by_id('PostingBody').send_keys(Keys.CONTROL, 'v')
    driver.find_element_by_xpath('//*[@id="contact_phone_ok"]').click()
    driver.find_element_by_xpath('//*[@id="contact_text_ok"]').click()
    driver.find_element_by_xpath('//*[@id="contact_phone"]').send_keys(phone_number)
    driver.find_element_by_xpath('//*[@id="contact_name"]').send_keys(contact_name)
    driver.find_element_by_xpath('//*[@id="postingForm"]/div/button').click()
    driver.find_element_by_xpath('//*[@id="leafletForm"]/button[1]').click()
    driver.find_element_by_xpath('/html/body/article/section/form/button').click()
#     driver.find_element_by_xpath('//*[@id="publish_top"]/button').click()

i=2
location='potsdam-massena'
post(location, emails[i], passwords[i])


