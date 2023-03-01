Feature: autocomplete section
  As a user
  I want to enter an address
  So that multiple suggestion to be available

  @smoke
  Scenario: test address field
    Given I am on autocomplete page
    When I type cj in address field
    Then Cluj should be display

  Scenario: enter only street name
    Given I am on autocomplete page
    When I type Dorobantilor on street field
    And I click on search button
    Then Dorobantilor should be display


    #todo sa verificati toate combinatile de taguri