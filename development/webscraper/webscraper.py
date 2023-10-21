from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
import time

options = webdriver.ChromeOptions()
options.add_argument(' — headless')
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()


url = "https://www.linkedin.com/jobs/search?keywords=software%20engineering%20internship&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
driver.get(url)
driver.implicitly_wait(220)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight,)")
internships = []

job_button_selector = '#main-content > section.two-pane-serp-page__results-list > ul > li:nth-child({}) > div > a'

for i in range(1, 151):
    selector = job_button_selector.format(i)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(7)
    job_button = driver.find_element(By.CSS_SELECTOR, selector)

    company_name = ''
    company_logo = '' #url
    title = ''
    description = ''
    location = ''
    industry = ''

    job_button.click()
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR, "body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > div > section > button.show-more-less-html__button.show-more-less-button.show-more-less-html__button--more.\!ml-0\.5").click()
    industry = driver.find_element(By.CSS_SELECTOR, 'body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > ul > li:nth-child(4) > span').text
    title = driver.find_element(By.CSS_SELECTOR, 'body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > section > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div > a > h2').text
    company_name = driver.find_element(By.CSS_SELECTOR, 'body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > section > div > div.top-card-layout__entity-info-container.flex.flex-wrap.papabear\:flex-nowrap > div > h4 > div:nth-child(1) > span:nth-child(1) > a').text
    description = driver.find_element(By.CSS_SELECTOR, 'body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > div > section.core-section-container.my-3.description > div > div > section > div').text
    company_logo = driver.find_element(By.CSS_SELECTOR, 'body > div.base-serp-page > div > section > div.details-pane__content.details-pane__content--show > section > div > a > img').get_attribute('src')


    internship_listing = {
        'title': title,
        'company': company_name,
        'logo': company_logo,
        'industry': industry,
        'raw_description': description
    }
    internships.append(internship_listing)
    
internships_df = pd.DataFrame(internships)

internships_df.to_csv('swe_linkedin_internships_US.csv')








