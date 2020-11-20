@web
Feature: Avatar Search Producer
    As a user, I should be able to search producer

  @p1 @producer @search_producer @producer_demo
    Scenario Outline: Verify producer search feature
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Search Agency button
        And User enters <agency_code>
        And User clicks on search button
        And User selects <search_value>
        Then User lands on searched agency form with <verify_agency_code>

  Examples:
    | agency_code | search_value |verify_agency_code|
    |M1111        |M1111         |M1111      |