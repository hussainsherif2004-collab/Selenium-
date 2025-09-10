from selenium import webdriver

#Set the path to the WebDriver
driver = webdriver.Chrome(executable_path='/path/to/chromedriver')

#Open a website
driver.get('https://www.example.com')

#Find an element (e.g., a button) and click it
button = driver.find_element_by_id('exampleButtonId')
button.click()

#Close the browser
driver.quit()
