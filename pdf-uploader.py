# You have to have the same version-as-your-browser Chrome WebDriver or Firefox GeckoDriver to use this.

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.expected_conditions import element_to_be_clickable

# (Not so important) Prompt user which browser webdriver to load

# Initialize webdriver
driver = webdriver.Firefox()

# Prompt the user which website to login to
# target_site = input("What is the name of the website? ")

target_site = "https://asc-prod.llnl.gov"

# Login to site manually
driver.get(target_site + '/login')

proceed = input(
    "Are you logged-in and ready to proceed? 'y' = yes, any key to abort: ")

FILESDIR = "./files_for_upload"

if proceed == 'y':
    for filename in os.listdir(FILESDIR):
        if filename.endswith('.pdf'):
            wait = WebDriverWait(driver, 60)
            driver.get(target_site + "/media/add/document")
            driver.find_element_by_id(
                "edit-field-document-0-upload").send_keys(os.path.join(FILESDIR, filename))
            wait.until(presence_of_element_located(
                (By.NAME, 'field_document_0_remove_button')))
            driver.find_element(
                By.ID, "edit-name-0-value").send_keys(filename)
            wait.until(element_to_be_clickable(
                (By.XPATH, 'html/body/div[2]/div[1]/main/div[4]/div[1]/form/div[8]/input[@id="edit-submit"]'))).click()
            continue
else:
    driver.quit()