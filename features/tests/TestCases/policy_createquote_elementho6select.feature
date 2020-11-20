@web
Feature: Avatar Policy Create Quote
    As a claim user , I should be able to create quote under policy

  @p1 @policy @ho6_elements
  Scenario Outline: Verify the HO6 Element fields under policy
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO6 Elements card
    And User enters <first_name>

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

   And User selects <personal_liability>

    And User selects <cvg_limit>
    And User selects <cvg_liability>
    And User clicks on deductible tab
    And User selects <non_hurricane>
    And User selects <hurricane>
    And User clicks Rate button
    Then User should be able to see error msg window
    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|ppc|bceg|year_built|construction_type|personal_liability|cvg_limit|cvg_liability|non_hurricane|hurricane|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |1  |1  |2014       |Frame            |100,000           |$25,000  |$100,000     |$1000 Deductible| 2% Ded|
