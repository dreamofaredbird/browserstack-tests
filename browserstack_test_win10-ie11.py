
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browser': 'IE',
 'browser_version': '11.0',
 'os': 'Windows',
 'os_version': '10',
 'resolution': '1024x768'
}


driver = webdriver.Remote(
    command_executor='http://robblackburn2:J9jypeH3Zyn9sqVLy9oG@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("https://orcid.org/about/news/news")
# if not "Orcid" in driver.title:
#    raise Exception("Unable to load orcid page!")
elem = driver.find_element_by_id("userId")
elem.send_keys("robqa@mailinator.com")
elem = driver.find_element_by_id("password")
elem.send_keys("Iai8zB067EJC")
elem.submit()
print driver.title
driver.quit()


# Using IE 11 visit the follow pages and make sure everything loads
# 	* https://qa.orcid.org (check that blog feed loads as well as page contents)
# 	* https://qa.orcid.org/0000-0002-0630-7594
# 	* https://qa.orcid.org/register
# 	* https://qa.orcid.org/sign-in
# 	* sign into 0000-0002-0630-7594 account and check that it also looks as expected



# 74. Using browserstack check the following pages on one Android and one Apple device to check load times
# 	* https://qa.orcid.org (check that blog feed loads as well as page contents)
# 	* https://qa.orcid.org/0000-0003-1637-5088
# 	* https://qa.orcid.org/register
# 	* https://qa.orcid.org/sign-in