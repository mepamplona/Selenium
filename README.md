REQUIREMENTS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Python 2.7
- Module Selenium v3.14
	pip install -U selenium
- Geckodriver v0.23 
	Geckodriver executable needs to be in PATH

USAGE:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
python test_login.py https://app.sysdigcloud.com

COMPLETED TASKS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
A class has been implemented with the foresight to develop different use cases linked to the login page.
Two cases of use have been made:
	1) Testing invalid credentials on login page
	2) Testing correct access to signUp link

The python script has been commented inside explaining the process. 

SETUP METHOD: In this method, general tasks have been implemented.
	- Define user  and password constant with test values. 
	- Create a global browser 
	- Instantiate a Firefox browser 
	- Get a local session when exploring to a page given by the URL variable in the web browser.
	
WebDriver will hold up until the page has completely been loaded before returning control to your test or script.

NOTE: It's important to know in this case it's a javascript web page so that it's necessary to wait some seconds to javascript code is processed.

CASE OF USE 1: test_invalid_credentials Method
	
    Code line 31-34: In these lines, we are finding the element of the textbox where the "username" and "password" has to be written.
    Code line 32-36: Clear these elements of previous values
	Code line 33-37: Now we are sending the values to the username and password sections
    Code line 39: elem.send_keys(Keys.RETURN) is used to press enter after the values are inserted
	Code line 42: "Asserts" keyword is used to verify the conditions. In this line, we are confirming whether the text 'Credential are not valid' appears in the page source.

CASE OF USE 2: test_access_sign_up Method

	Code line 47: We are finding the element of the href
	Code line 48:  elem.click() is used to press the link and access to the new page
	Code line 49: "Asserts" keyword is used to verify the conditions. In this line, we are confirming whether the title is correct or not. For that, we will compare the title with the string which is given.
 
TEARDOWN METHOD: In this method is closed the session and browser


TODO or NEXT STEPS
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
If I had more time I'd develop more cases of use to test the rest of functionalities, for instance:
	- Access other links such as OAuth with Google, SAML and OpenId
	- Forget your password

Furthermore it will be necessary to improve the code to be reuse to other login pages passing username/password name fields as arguments in command line
