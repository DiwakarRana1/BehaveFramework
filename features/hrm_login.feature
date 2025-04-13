Feature: Login to HRM Page
  Scenario: Open the URL and and Enter Credentials
    Given I am on the HRM Login Page
    When I Enter User Credentials
    Then I should see the Admin Page