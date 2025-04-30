#Author: Anna V
# Jira ID 123
# this is test scenarios for manual testcase path: C://...

Feature: Profitolizer Login Test Scenarios for functional testing
  Background:
    Given Open "https://profitolizer.com/"
    Then Verify page by title "Home - Profitolizer"
    Then Click element "//a[contains(text(),'Login')]"
    Then Wait for the element with xpath "//h5" to be present
    And Verify that xpath "//h5" should contain text "Login to Your Account"
    Then Verify that xpath "//p[@class='text-center small']" should contain text "Enter your username & password to login"
  @smoke
  Scenario: Login with valid username and valid password

    #fill out email and password text fields for login form
    When Type "annaverpcs+22@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    When Click element "//button[@type='submit']"
    #redirection to main page
    #Then Wait 1 seconds
    Then Verify page by title "Profotolizer - Projects"
    And Wait for the element with xpath "//span[contains(text(),'annaverpcs22')]" to be present
    Then Verify that xpath "//span[contains(text(),'annaverpcs22')]" should contain text "annaverpcs22"
    Then Wait 1 seconds


  Scenario: Login with valid username and valid password for user with 1 project
    #fill out email and password text fields for login form
    When Type "annaverpcs+21@gmail.com" into "//input[@type='text']"
    When Type "12345678" into "//input[@type='password']"
    When Click element "//button[@type='submit']"
    #redirection to main page
    Then Verify page by title "Profotolizer - P&L charts"
    And Wait for the element with xpath "//span[contains(text(),'annaverpcs21')]" to be present
    Then Verify that xpath "//span[contains(text(),'annaverpcs21')]" should contain text "annaverpcs21"
    And Verify that xpath "//h1" should contain text "P&L Graphs"
    And Verify presents of element "//a[contains(text(),'test')]"
    Then Wait 1 seconds

  Scenario: Login with valid username and empty password
    #Given Open "https://profitolizer.com/"
    #Then Verify page by title "Home - Profitolizer"
    #Then Click element "//a[contains(text(),'Login')]"
    #Then Wait for the element with xpath "//h5" to be present
    #And Verify that xpath "//h5" should contain text "Login to Your Account"
    #Then Verify that xpath "//p[@class='text-center small']" should contain text "Enter your username & password to login"
    #fill out email and password text fields for login form
    When Type "annaverpcs+22@gmail.com" into "//input[@type='text']"
    When Click element "//button[@type='submit']"
    #verify that user cannot login with empty password and verify error message
    Then Verify presents of element "//div[@class='invalid-feedback' and contains(text(),'Password is required')]"
