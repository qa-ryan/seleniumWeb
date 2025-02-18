import unittest

from requests import options

from packages import*

class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        #self.driver.minimize_window()

    #This function is to check ClickTest_testClicksASurroundingStrongTag.html
    """def test_click_test(self):
        self.driver.get("https://www.selenium.dev/selenium/web/")
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="ClickTest_testClicksASurroundingStrongTag.html"]')))
        except TimeoutException:
            print('NEed more time to load')

        click_test_link1 = self.driver.find_element(By.CSS_SELECTOR, 'a[href="ClickTest_testClicksASurroundingStrongTag.html"]')
        if requests.head(click_test_link1.get_attribute('href')).status_code == 200:
            print('Link 1 is Valid: ', click_test_link1.get_attribute('href'))
        else:
            print('Link 1 is broken: ', click_test_link1.get_attribute('href'))

        click_test_link1.click()

        # Chceking link from Click
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='xhtmlTest.html']")))
        except TimeoutException:
            print("Need more time to load")

        click_test_link2 = self.driver.find_element(By.CSS_SELECTOR, "a[href='xhtmlTest.html']")
        if requests.head(click_test_link2.get_attribute("href")).status_code == 200:
            print("Link 2 is valid", click_test_link2.get_attribute("href"))
        else:
            print("Link 2 is broken", click_test_link2.get_attribute("href"))

        click_test_link2.click()

        self.driver.quit()"""

    #This function to check https://www.selenium.dev/selenium/web/xhtmlTest.html
    def test_open_new_window(self):
        self.driver.get("https://www.selenium.dev/selenium/web/xhtmlTest.html")
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='resultPage.html']")))
        except TimeoutException:
            print("Need more time to load")
        new_window = self.driver.find_element(By.CSS_SELECTOR, "a[href='resultPage.html']")
        new_window.click()

        #This line is to change webdriver to new open tab >> webdriver changed to resultPage.html
        self.driver.switch_to.window(self.driver.window_handles[1])

        #This line start to check the page, Content Validation
        content_validation(self)

        self.driver.close()
        #This line is to bring webdriver back to previous tab
        self.driver.switch_to.window(self.driver.window_handles[0])
        self.driver.quit()
    #This function is to check https://www.selenium.dev/selenium/web/iframes.html
    def test_new_anon_window(self):
        self.driver.get("https://www.selenium.dev/selenium/web/xhtmlTest.html")
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.NAME, "windowTwo")))
        except TimeoutException:
            print("Need more time to load")

        self.driver.find_element(By.NAME, "windowTwo").click()
        self.driver.switch_to.window(self.driver.window_handles[1])

        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "iframe_page_heading")))
        except TimeoutException:
            print("Need more time to load")

        heading = self.driver.find_element(By.ID, "iframe_page_heading").text
        print(heading)

        #This line is to change webdriver to iframe
        iframe_element = self.driver.find_element(By.TAG_NAME, "iframe")
        self.driver.switch_to.frame(iframe_element)

        email = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
        email.send_keys("testing@gmail.com")
        self.driver.find_element(By.ID, "age").send_keys("45")
        self.driver.find_element(By.ID, "submitButton").click()

        # This line start to check the page, Content Validation
        content_validation(self)

























if __name__ == '__main__':
    unittest.main()