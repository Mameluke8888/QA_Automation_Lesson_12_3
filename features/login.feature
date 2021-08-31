Feature: User can access his account through login page
  Background:
    Given registered user who is not logged in has home page opened in a browser


    Scenario: Opening login page through header with correct credentials
      Given user clicks on Login option of My Account dropdown menu in the header
      When user enters correct both email address and password in the corresponding fields
      And user clicks Login button
      Then user account page is open

    Scenario: Opening login page through right menu with correct credentials
      Given user clicks on Register option of My Account dropdown menu in the header
      And user clicks on Login option in the right menu
      When user enters correct both email address and password in the corresponding fields
      And user clicks Login button
      Then user account page is open

    Scenario: Opening login page through header with incorrect email
      Given user clicks on Login option of My Account dropdown menu in the header
      When user enters incorrect email address and correct password in the corresponding fields
      And user clicks Login button
      Then message "Warning: No match for E-Mail Address and/or Password." appears

    Scenario: Opening login page through header with incorrect password
      Given user clicks on Login option of My Account dropdown menu in the header
      When user enters registered email address but incorrect password in the corresponding fields
      And user clicks Login button
      Then message "Warning: No match for E-Mail Address and/or Password." appears