@web
Feature: Avatar Policy Create Quote
    As a claim user , I should be able to create quote under policy

  @p1 @policy @ho3_owners
  Scenario Outline: Verify the HO3 Diamond fields under policy
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User enters <house_number>
    And User enters <street_name>
    And User enters <zip_code>
    And User clicks Property Details
    And User selects <structure_type>
    And User enters <nor>
    And User enters <areasqft>
    And User selects <roof_type>
    And User selects <sub_roof_type>
    And User selects <ppc>
    And User selects <bceg>
    And User enters <year_built>
    And User selects <construction_type>
    And User selects <occupancy_type>
    And User enters <fire_stn>
    And User enters <hydrant>
    And User clicks coverage tab
    And User enters <dwelling>
    And User clicks Rate button
    Then User should verify the premium value
    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|structure_type|nor|areasqft|roof_type|sub_roof_type|ppc|bceg|year_built|construction_type|occupancy_type|fire_stn|hydrant|dwelling|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Apart         |1  |111     |Composition|3-Tab      |1  |1  |2014       |Frame            |Owner        |1        |1      |150000   |
      | test_policy1 |test_last1|07071991|test |122         |florida    |33319   |Co-Op         |1  |122     |Composition|Architectural     |2  |2  |2014       |Frame            |Tenant        |1        |1      |190000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Dwelling         |1  |111     |Composition|Architectural      |1  |1  |2014       |Masonry            |Unoccupancy        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Condo         |1  |333  |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Row House        |1  |111     |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Town House        |1  |111     |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Villa       |1  |555     |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |MFG Home         |1  |111     |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Mobile Home         |1  |111     |Composition|3-Tab      |1  |1  |2014       |MFG Home            |Vacant        |1        |1      |150000   |

 @p1 @policy @ho3_owners1
  Scenario Outline: Verify the HO3 Diamond fields under policy without coverage tab
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
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
    And User clicks Rate button
    Then User should be able to see error msg window
    And User should see the 'Dwelling cost' error popup
    And User should see the 'coverage' error popup
    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|ppc|bceg|year_built|construction_type|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |1  |1  |2014       |Frame            |
      | test_policya |test_last|07071991|test |122         |florida    |33319   |1  |1  |2015       |Masonry            |
      | test_policyb |test_last|07071991|test |122         |florida    |33319   |1  |1  |2016       |Vinyl Siding            |
      | test_policyc |test_last|07071991|test |122         |florida    |33319   |1  |1  |2017       |Stucco on Block            |
      | test_policyc |test_last|07071991|test |122         |florida    |33319   |1  |1  |2017       |Stucco on Frame            |
      | test_policyc |test_last|07071991|test |122         |florida    |33319   |1  |1  |2017       |Masonry Veener            |

 @p1 @policy @ho3_owners2
  Scenario Outline: Verify the HO3 Diamond fields under policy without property and coverage tab
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User enters <house_number>
    And User enters <street_name>
    And User enters <zip_code>
    And User clicks Rate button
   Then User should be able to see error msg window
   And User should see the 'Protection Class' error popup
   And User should see the 'BCEG' error popup
   And User should see the 'Year Built' error popup
   And User should see the 'Construction Type' error popup
   And User should see the 'Dwelling cost' error popup
   And User should see the 'coverage' error popup

    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |

 @p1 @policy @ho3_owners3
  Scenario Outline: Verify the HO3 Diamond fields under policy without street name
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User clicks Rate button
    Then User should be able to see error msg window
    And User should see the 'House No' error popup
    And User should see the 'Protection Class' error popup
    And User should see the 'BCEG' error popup
    And User should see the 'Year Built' error popup
    And User should see the 'Construction Type' error popup
    And User should see the 'Dwelling cost' error popup
    And User should see the 'coverage' error popup
    Examples:
        | first_name  |last_name|dob|occupation|
        | test_policy |test_last|07071991|test |
 @p1 @policy @ho3_owners4
  Scenario Outline: Verify the HO3 Diamond fields under policy only name and dob
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User clicks Rate button
    Then User should be able to see error msg window
    And User should see the 'House No' error popup
    And User should see the 'Protection Class' error popup
    And User should see the 'BCEG' error popup
    And User should see the 'Year Built' error popup
    And User should see the 'Construction Type' error popup
    And User should see the 'Dwelling cost' error popup
    And User should see the 'coverage' error popup
    Examples:
      | first_name  |last_name|dob|
      | test_policy |test_last|07071991|
 @p1 @policy @ho3_owners5
  Scenario Outline: Verify the HO3 Diamond fields under policy only name
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User clicks Rate button
    Then User should be able to see error msg window
    And User should see the 'House No' error popup
    And User should see the 'House No' error popup
    And User should see the 'Protection Class' error popup
    And User should see the 'BCEG' error popup
    And User should see the 'Year Built' error popup
    And User should see the 'Construction Type' error popup
    And User should see the 'Dwelling cost' error popup
    And User should see the 'coverage' error popup


    Examples:
      | first_name  |last_name|
      | test_policy |test_last|


   @p1 @policy @ho3_owners
  Scenario Outline: Verify the HO3 Diamond fields under policy fire and hydrant error
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User enters <house_number>
    And User enters <street_name>
    And User enters <zip_code>
    And User clicks Property Details
    And User selects <structure_type>
    And User enters <nor>
    And User enters <areasqft>
    And User selects <roof_type>
    And User selects <sub_roof_type>
    And User selects <ppc>
    And User selects <bceg>
    And User enters <year_built>
    And User selects <construction_type>
    And User selects <occupancy_type>
    And User clicks coverage tab
    And User enters <dwelling>
    And User clicks Rate button
    Then User should see the 'Hydrant and Firestation' error popup

    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|structure_type|nor|areasqft|roof_type|sub_roof_type|ppc|bceg|year_built|construction_type|occupancy_type|dwelling|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Apart         |1  |111     |Composition|3-Tab      |1  |1  |2014       |Frame |Owner                    |150000  |


  Scenario Outline: Verify the HO3 Diamond fields under policy without sub roof
    Given User is on Avatars login page
    When User logs in with user 'claim_user'
    And User clicks on policy on top navigation bar
    And User clicks on create quote from left hand navigation bar
    And User clicks HO3 Diamond card
    And User enters <first_name>
    And User enters <last_name>
    And User enters <dob>
    And User enters <occupation>
    And User enters <house_number>
    And User enters <street_name>
    And User enters <zip_code>
    And User clicks Property Details
    And User selects <structure_type>
    And User enters <nor>
    And User enters <areasqft>
    And User selects <roof_type>
    And User selects <ppc>
    And User selects <bceg>
    And User enters <year_built>
    And User selects <construction_type>
    And User selects <occupancy_type>
    And User enters <fire_stn>
    And User enters <hydrant>
    And User clicks coverage tab
    And User enters <dwelling>
    And User clicks Rate button
    Then User should verify the premium value
    Examples:
      | first_name  |last_name|dob|occupation|house_number|street_name|zip_code|structure_type|nor|areasqft|roof_type|ppc|bceg|year_built|construction_type|occupancy_type|fire_stn|hydrant|dwelling|
      | test_policy |test_last|07071991|test |122         |florida    |33319   |Apart         |1  |111     |Other|     1  |1  |2014       |Frame            |Owner        |1        |1      |150000   |
      | test_policy |test_last|07071992|test1 |122         |florida    |33319   |Apart        |3  |222     |Metal Roof|     1  |1  |2014       |Masonry            |Tenant        |1        |1      |800000   |
      | test_policy |test_last|07071993|test2 |122         |florida    |33319   |Apart        |4  |333     |Tile|     1  |1  |2014       |MFG Home            |Owner        |1        |1      |450000   |
      | test_policy |test_last|07071994|test3 |122         |florida    |33319   |Apart        |5  |444     |Wood Shake|     1  |1  |2014       |Vinyl Siding            |Owner        |1        |1      |500000   |