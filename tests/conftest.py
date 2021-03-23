import pytest
from selenium import webdriver

@pytest.fixture()
def setUp(request, getUrl):
    request.cls.driver.get(getUrl)   
    yield

@pytest.fixture(scope="class")
def oneTimeSetup(browser, request):   
    if browser == "chrome":           
            driver_location = "././utilities/drivers/chromedriver.exe"
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--no-proxy-server")
            driver = webdriver.Chrome(driver_location,options=chrome_options)            
            print("Running tests on Chrome") 
    else:
        driver = webdriver.Firefox()
        print("Running tests on firefox")
    
    driver.maximize_window()
    driver.implicitly_wait(3)

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def getUrl():
    return 'https://letskodeit.com/'

def pytest_addoption(parser):
    parser.addoption("--browser")
