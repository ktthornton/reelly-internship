Feature: Add a Project page in mobile emulation


  Scenario: Verify clicking Add a Project brings the user to the correct page
    Given User signs in to Reelly site
    When Click Settings/Menu
    And Click Add a Project
    Then Verify user is brought to the correct page

  Scenario: Verify Send an application button is clickable
    Given User signs in to Reelly site
    When Click Settings/Menu
    And Click Add a Project
    Then Verify Send an application button is clickable

  Scenario: Verify Add a Project page fields
    Given User signs in to Reelly site
    When Click Settings/Menu
    And Click Add a Project
    And Text is input into fields
    Then Verify text displays correctly