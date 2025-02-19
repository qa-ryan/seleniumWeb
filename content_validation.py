from packages import*
def content_validation(self):
    try:
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "p")))
    except TimeoutException:
        print("Need more time to load")

        # This line is to check Title Validation
    title = self.driver.find_element(By.TAG_NAME, "p").text
    title_1 = title
    title_2 = "Success!"
    self.assertEqual(title_1, title_2, "Title doesn't match")
    print(title)

    # This line is to check List of Stuff text
    stuff = self.driver.find_element(By.XPATH, "//h1[text()='List of stuff']").text
    stuff_1 = stuff
    stuff_2 = "List of stuff"
    self.assertEqual(stuff_1, stuff_2, "Title doesn't match")
    print(stuff)

    # This line is to print list item text
    items = self.driver.find_elements(By.TAG_NAME, "li")
    values = [item.text for item in items]
    print(values)

    # This line is to check almost empty text
    almost_empty = self.driver.find_element(By.XPATH, "//h1[text()='Almost empty']").text
    print(almost_empty)

    # This line is to check result text
    result = self.driver.find_element(By.CSS_SELECTOR, "body > p:nth-child(5)").text
    print(result)