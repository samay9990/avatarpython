@web
Feature: Avatar Add Claim
    As a claim user , I should be able to Add claim



Scenario Outline: Verify that user can add new claim
    Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on claim in top navigation bar
    And User clicks Add Claim button
    And User enters policy number 'HOFL200163690'
    And User clicks Search button
    And User clicks on the Policy number 'HOFL200163690' from the table
    And User selects <select_location> from the dropdown
    And User selects the claim type to <claim_type>
    And User selects the type of loss to <loss_type>
    And User selects the service rep to <service_rep>
    And User selects <date_of_loss>
    And User selects the event name to <event_name>
    And User enters the <email_id>
    And User selects <claim_reported_by>
    And User selects <claim_sub_status>
    And User clicks on Save Claim button

    And User clicks Payment tab
    And User enters <date> in payment tab
    And User selects <Transaction_sub_type> in payment tab
    And User selects <TransactionType> in payment tab
    And User enters <Description> in payment tab
    And User clicks on Claim Deductible button in payment tab

    And User selects Attachment tab
    And User enter <Filename> in attachment tab
    And User selects <Authorisation> in attachment tab
    And User select <Attachment_type> in attachment tab
    And User selects <document_type> in attachment tab
    And User enters <description> in attachment tab
    And User click on Add Attachment button in attachment tab
    And User clicks Claim View Tab from attachment tab

    Then User should not see the red toast message
    And User should see green toast having message 'Claim details stored successfully'
    Examples:
    |select_location                                        |claim_type|loss_type|service_rep|date_of_loss|event_name|email_id   |claim_reported_by  |claim_sub_status|date|Transaction_sub_type|TransactionType|Description|Filename|Authorisation|Attachment_type|document_type|description|
    |6730 NW 27 TERR, FT LAUDERDALE, BROWARD, FLORIDA, 33309|Fire Loss |Liability|Adam Hunt  |0724        |GORDON    |test@gmail.com|Insured            |Assigned to STI |07242020|Claim Expense                |Loss Reserves   |Description          |Testfile|Internal|Single File|Acknowledge form|Description|
