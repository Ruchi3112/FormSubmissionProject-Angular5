
from selenium import webdriver
from selenium.webdriver.common.by import By


class FormSubmissionPage:

    def __init__(self, driver):
        self.driver = driver

    def GetName(self):
        return self.driver.find_element_by_name('name')

    def GetEmail(self):
        return self.driver.find_element_by_css_selector("input[name='email']")

    def GetPassword(self):
        return self.driver.find_element_by_css_selector("input[placeholder='Password']")

    def GetCheckBox(self):
        return self.driver.find_element_by_id("exampleCheck1")

    def GetGender(self):
        return self.driver.find_element_by_id("exampleFormControlSelect1")


    def GetEmploymentStatus(self):
        return self.driver.find_element_by_xpath("//input[@id='inlineRadio2']")


    def GetDOB(self):
        return self.driver.find_element_by_xpath("//input[@name='bday']")


    def SubmitForm(self):
        return self.driver.find_element_by_xpath("//input[@value='Submit']")


    def GetSuccessMessage(self):
        return self.driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']")


