# from webdriver_manager.firefox import GeckoDriverManager
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# import time


# browser = webdriver.ChromiumEdge()
# browser.get('https://wuzzuf.net/jobs/egypt')
# print(browser.title)
# clickable = browser.find_element(By.NAME, "q")
# ActionChains(browser)\
#     .click(clickable)\
#     .perform()
# ActionChains(browser)\
#         .send_keys("Engineer")\
#         .perform()
# ActionChains(browser)\
#         .send_keys(Keys.ENTER)\
#         .perform()

# time.sleep(50)
# # browser.back()
# # browser.close()

from webdriver_manager.firefox import GeckoDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


browser = webdriver.Firefox()
browser.get('https://wuzzuf.net/jobs/egypt')
print(browser.title)
clickable = browser.find_element(By.NAME, "q")
ActionChains(browser)\
    .click(clickable)\
    .perform()
ActionChains(browser)\
        .send_keys("Engineer")\
        .perform()
ActionChains(browser)\
        .send_keys(Keys.ENTER)\
        .perform()
element_list=[]
time.sleep(5)
for i in range(16):
    page_3_xpath = f"//li[@class='css-1q4vxyr'][button[text()='{i}']]"

    try:
        page_3_button = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, page_3_xpath))
        )
        
        browser.execute_script("arguments[0].scrollIntoView(true);", page_3_button)

        WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.XPATH, page_3_xpath))
        )
        
        browser.execute_script("arguments[0].click();", page_3_button)
        print(f"Clicked on page {i}")
    
    except Exception as e:
        print(f"Failed to click on page {i}: {e}")

title = browser.find_elements(By.CLASS_NAME, "css-o171kl")
recruiter = browser.find_elements(By.CLASS_NAME, "css-17s97q8")
# years_of_exp = browser.find_elements(By.CLASS_NAME, "xh-highlight")

for i in range(len(title)):
    try:
        title_text = title[i].text
        recruiter_text = recruiter[i].text
        element_list.append([title_text, recruiter_text])
    except IndexError:
        element_list.append([title[i].text, ""])

print(element_list)
element_list
time.sleep(30)

with open('job_listings.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Recruiter"])  
    writer.writerows(element_list)  

browser.close()