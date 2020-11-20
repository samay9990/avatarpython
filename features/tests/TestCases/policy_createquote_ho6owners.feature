@web
Feature: Avatar Policy Create Quote
    As a claim user , I should be able to create quote under policy

  @p1 @policy @ho6_owners
  Scenario Outline: Verify the HO6 Owners fields under policy
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO6 Homeowners card
    And User enters <first_name>
    And User clicks Rate button
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User enters <house_number>
    And User enters <street_name>
    And User enters <zip_code>
    And User clicks Property Details
    And User selects <ppc>
    And User selects <bceg>
    And User enters <year_built>
    And User selects <construction_type>
    And User clicks coverage tab
    And User enters <personal_property>
    Then User should be able to see error msg window
    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|ppc|bceg|year_built|construction_type|personal_property|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |1  |1  |2014       |Frame            |20000   |
|
