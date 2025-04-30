# Created by averkhovskaya at 4/2/25
Feature: First exercise with functional testing
  @regression
  Scenario: Yahoo Web Search with valid text
    Given Open "https://search.yahoo.com/"
    Then Type "Python" into "//input[@id='yschsp']"
    Then Click element "//button[@id='sbq-submit']"
    #moved to search result page after submitting search request
    Then Verify presents of element "//input[@id='yschsp' and @value='Python']"
    Then Wait 2 seconds
    Then Verify that xpath "//div[@id='left']" should contain text "Python"

