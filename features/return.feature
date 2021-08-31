Feature: Users can return an item


  Scenario: Requesting an RMA number to process a return
    Given user opens return request form by clicking on Returns option in the footer
    When user fills all fields with order and product information
    And user indicates a reason for return by clicking a corresponding radiobutton in Reason for Return section
    And user indicates whether the product was opened by clicking a corresponding radiobutton
    And user clicks Submit button
    Then message "Thank you for submitting your return request..." appears