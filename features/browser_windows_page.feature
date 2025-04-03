Feature: Browser Tab Handling

  Background:
    Given I am on the DEMOQA Home Page
    When I click on the Elements Section
    Then I should see the Elements Page

    Scenario: Opening the new tab and Switching Back to Original
    When I click on the Alerts, Frames & Windows
    And I click on Browser Windows
    And I click on the new tab button
    Then the switching of tabs will done
