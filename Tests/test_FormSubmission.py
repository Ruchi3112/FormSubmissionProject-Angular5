import pytest
from selenium import webdriver
from PageObject.FormPage1 import FormSubmissionPage
from Testdata.FormPageData import FormData
from utilities.BaseClass import BaseClass
from selenium.webdriver.support.select import Select


class TestFormSubmission(BaseClass):

    def test_formSubmission(self, getData):
        log = self.getLogger()

        formpage = FormSubmissionPage(self.driver)
        formpage.GetName().send_keys(getData["firstName"])
        log.info("Getting first Name :"+getData["firstName"])

        formpage.GetEmail().send_keys(getData["Email"])
        log.info("Getting Email address :"+getData["Email"])

        formpage.GetPassword().send_keys(getData["password"])
        log.info("Getting Password :"+getData["password"])

        formpage.GetCheckBox().click()
        log.info("clicking the checkbox")

        sel=Select(formpage.GetGender())
        sel.select_by_visible_text(getData["Gender"])
        log.info("Getting Gender Info :"+getData["Gender"])

        formpage.GetEmploymentStatus().send_keys(getData["EmploymentStatus"])
        log.info("Getting Employment Info :"+getData["EmploymentStatus"])

        formpage.GetDOB().send_keys(getData["BirthDay"])
        log.info("Getting Birthday info :"+getData["BirthDay"])

        formpage.SubmitForm().click()

        alertText = formpage.GetSuccessMessage().text
        log.info("Text received after form submission is :"+alertText)
        assert ("Success" in alertText)
        self.driver.refresh()


    @pytest.fixture(params=FormData.test_Form_data)
    def getData(self,request):
        return request.param