#! /usr/bin/env python
# Script: test_login.py
# Author: Maria Eugenia Pamplona
# Analysis Login Web SisDig - Monitor

import time, unittest, sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login(unittest.TestCase):
	
	URL = "http://www.google.es"	
	def setUp(self):
		# Base variables to testing
		self.user = "test@sysdig.com"
		self.password = "p4ssw0rd"
	
		# We instantiate a Firefox browser, get a local session and open a specific url in the web browser
		global browser
		browser = webdriver.Firefox()
		browser.get(self.URL)
		# Web wait some seconds to javascript code is processed
                time.sleep(5)

	''' Test1: Invalid credentials in login page '''	
	def test_invalid_credentials(self):
		# DEBUG - This code allows us to obtain the page source to analys name of fields.
		#html = browser.page_source
		#print(html)

		elem = browser.find_element_by_name('username')
		elem.clear()
		elem.send_keys(self.user)

		elem = browser.find_element_by_name('password')
		elem.clear()
		elem.send_keys(self.password)

		# We trigger a press RETURN key on the submit button which will then login to the website for us
		elem.send_keys(Keys.RETURN)
		
		time.sleep(5)
		assert 'Credentials are not valid' in browser.page_source
	
	''' Test2: Access when you click SignUp link '''
	def test_access_sign_up(self):
		elem = browser.find_element_by_link_text('Not a customer? Try for free')
		elem.click()
		assert 'Sign up' in browser.page_source
		
	def tearDown(self):
		browser.quit()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		Login.URL=sys.argv.pop()
		unittest.main()
	else:
		print("USAGE: python test_login.py <URL>")
		print("")
		print("Example: python test_login.py https://app.sysdigcloud.com")
		
