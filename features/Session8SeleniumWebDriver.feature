# Created by averkhovskaya at 4/29/25
@regression
Feature: Session 8 Selenium WebDriver test scenarios
  @smoke @regression @sanity
  Scenario: Login to app with custom methods
    Given AnnaV would like to open "Profitolizer" page
    #Given AnnaV would like to open "Google" page
   # Then AnnaV would like to open "Walmart" page
    Then AnnaV verify page title is "Home - Profitolizer"
    And AnnaV click on "Login" button
    Then Wait for the element with xpath "//h5" to be present
    Then AnnaV type "annaverpcs+22@gmail.com" to "//input[@type='text']"
    Then AnnaV type "12345678" to "//input[@type='password']"
    And AnnaV click on "Submit" button
    And Wait 5 seconds
    Then AnnaV verify page title is "Profotolizer - Projects"