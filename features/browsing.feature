Feature: browsing products


  Scenario Outline: User can browse different products
    Given user has navigation bar available on home page
    When user moves to "<section>" in navigation bar
    And user clicks on "<option>" of a dropdown menu
    Then page with "<product>" is open


    Examples: Products
    |section      |option             |product      |
    |Desktops     |Macs               |Mac desktops |
    |Desktops     |PC                 |PC desktops  |
    |Phones & PDAs|Phones             |Phones       |
    |Components   |Show All Components|Components   |



