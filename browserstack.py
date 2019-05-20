from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

desired_cap = {
 'browserName': 'iPhone',
 'device': 'iPhone 8 Plus',
 'realMobile': 'true',
 'os_version': '11'
}

driver = webdriver.Remote(
    command_executor='http://robblackburn2:J9jypeH3Zyn9sqVLy9oG@hub.browserstack.com:80/wd/hub',
    desired_capabilities=desired_cap)

driver.get("http://www.qa.orcid.org")
if not "ORCID" in driver.title:
    raise Exception("Unable to load orcid page!")
driver.implicitly_wait(100)
elem = driver.find_element_by_id("home-blog-list")
print driver.title
driver.quit()

# <a href="/news/2012/03/23/version-104-orcid-mock-api-released"><i>News</i> | Version 1.0.4 of the ORCID Mock API Released</a>
# elem = driver.find_element_by_id("userId")
# elem.send_keys("robqa@mailinator.com")
# elem = driver.find_element_by_id("password")
# elem.send_keys("Iai8zB067EJC")
# elem.submit()
# print driver.title
# driver.quit()



# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# desired_cap = {
#  'browser': 'IE',
#  'browser_version': '11.0',
#  'os': 'Windows',
#  'os_version': '10',
#  'resolution': '1024x768'
# }

# driver = webdriver.Remote(
#     command_executor='http://robblackburn2:J9jypeH3Zyn9sqVLy9oG@hub.browserstack.com:80/wd/hub',
#     desired_capabilities=desired_cap)

# driver.get("http://www.qa.orcid.org/signin")
# #if not "Orcid" in driver.title:
# #    raise Exception("Unable to load orcid page!")
# elem = driver.find_element_by_id("userId")
# elem.send_keys("robqa@mailinator.com")
# elem = driver.find_element_by_id("password")
# elem.send_keys("Iai8zB067EJC")
# elem.submit()
# print driver.title
# driver.quit()

# check that blog feed loads as well as page contents) the side bar on the home page check nav, check public record ( the one we use for testing pblic record testing check the header nav sign in and register)

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