Feature: Unregistered users can create a new account


  Scenario: Registering a new user
    Given an unregistered user is on home page
    When user clicks on Register option of dropdown menu from My Account option in the header
    And user fills all fields with personal information
    And user checks Yes/No radiobutton for subscription to the newsletter
    And user checks I have read and agree to the Privacy Policy checkbox
    And user clicks Continue button
    Then message "Your Account Has Been Created!" or "E-Mail Address is already registered" appears