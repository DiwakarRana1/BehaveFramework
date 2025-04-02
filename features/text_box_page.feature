Feature: Text Box Page Functionality

  Background:
    Given I am on the DEMOQA Home Page
    When I click on the Elements Section
    Then I should see the Elements Page

  Scenario: Fill and submit the text box form
    When I click on the "Text Box" menu
    And I enter text in all fields
    And I click on the submit button
    Then the input values should be correctly displayed
