Feature: Add Employee to HRM
  Scenario: Successfully add a new employee after login
    Given I am on the HRM Login Page
    When I Enter User Credentials
    And I navigate to the Add Employee page
    And I fill in new employee details
    And I save the employee
    And I click on PIM
    And Search the EmpID
    And Delete the Employee