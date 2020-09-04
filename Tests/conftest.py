import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(executable_path="E:/Chromedriver.exe")
    driver.get("https://www.rahulshettyacademy.com/angularpractice/")
    driver.maximize_window()
    request.cls.driver = driver
    #yield
        #driver.close()



