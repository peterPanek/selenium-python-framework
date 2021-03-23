from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
from ddt import ddt, data, unpack
from utilities.read_data import getCSVData
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetup","setUp")
@ddt
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=2)
    # @data(("tomket87@gmail.com","`1`1`11"))
    @data(*getCSVData("C:\\Python\\Selenium_udemy\\selenium_framework\\testdata.csv"))
    @unpack
    def test_validLogin(self, username, password):     
        # self.lp.login("tomket87@gmail.com","`1`1`11")
        self.lp.login(username,password)
        self.ts.mark(self.lp.verifyTitle("All Courses"),"Title Verification")
        self.ts.markFinal("test_validLogin",self.lp.verifyLoginSuccessful(),"Login verification")
        

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):      
        self.lp.login("tomket87@gmail.com","0101011")
        self.assertTrue(self.lp.verifyLoginFailed)
