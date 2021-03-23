from base.selenium_driver import SeleniumDriver

class TestStatus(SeleniumDriver):
    def __init__(self, driver):
        super().__init__(driver)
        self.resultsList = []

    def setResult(self, result, resultMessage):
        try:
            if result:
                self.resultsList.append("PASS")
                self.log.info("### VERIFICATION SUCCESFUL - {0}".format(resultMessage))
            else:
                self.resultsList.append("FAIL")
                self.log.error("### VERIFICATION IS FAILED - {0}".format(resultMessage))
                self.screenShot(resultMessage)
        except:
            self.resultsList.append("FAIL")
            self.log.error("### EXCEPTION OCCURED ###")
            self.screenShot(resultMessage)

    def mark(self, result, resultMessage):
        self.setResult(result, resultMessage)
        
    def markFinal(self, testName, result, resultMessage):
        self.setResult(result, resultMessage)

        if "FAIL" in self.resultsList:
            self.log.error("{0} ### TEST FAILED".format(testName))
            self.resultsList.clear()
            assert True == False
        else:
            self.log.info("{0} ### TEST SUCCESSFUL".format(testName))
            assert True == True