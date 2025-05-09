Feature: Login to User Management Page
  Scenario: Open the URL and and Do Successful Login
    Given I am on the User Management Home Page
    When I Click on Login Button
    When I Enter Credentials
    Then I should see the Dashboard