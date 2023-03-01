Feature: autocomplete with multiple complete scenario
  As a user
  I want to enter an address
  So that multiple suggestion to be available

  Scenario Outline: test autocomplet with 10 inputs
    Given I am on autocomplete page
    When I type "<city>" in address field
    Then  "<expected_results>"should be display
    Examples:
      | city | expected_results |
      | Cj   | Cluj             |
      | cl   | calarasi          |
      | bv   | brasov           |
      | mm   | maramures        |
      | ph   | prahova          |
      | b    | bucuresti        |
      | g    | galati           |
      | tm    | timisoara        |
      | bc   | bacau            |
      | s    | sibiu            |
