@web
Feature: Avatar Edit Claim
    As a claim user , I should be able to edit claim

@p1 @claims @edit_claim
Scenario: Verify that user can edit claim
    Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on claim in top navigation bar
    And User searches for claim number '20200115'
    And User clicks on search button on claim home page
    And User clicks on claim '20200115' in the results table
    And User clicks on edit button on claim page
    And User changes the claim type to 'Fire Loss'
    And User changes the type of loss to 'Liability'
    And User changes the service rep to 'Adam Hunt'
    And User changes the event name to 'GORDON'
    And User changes the claim status open to 'Open'
    And User clicks on Update Claim button
    Then User should see green toast having message 'Claim details updated successfully'

    @claim_edit_alltabs
Scenario Outline: Verify that user can edit claim by changing values in all tabs
    Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on claim in top navigation bar
    And User searches for claim number '20200115'
    And User clicks on search button on claim home page
    And User clicks on claim '20200115' in the results table
    And User clicks on edit button on claim page
    And User changes the claim type to <claim_type>
    And User changes the type of loss to <loss_type>
    And User changes the service rep to <service_rep>
    And User changes the event name to <event_name>
    And User changes the claim status open to <claim_status>
    When User clicks Payment tab
    And User enters <date> in payment tab
    And User selects <TransactionType> in payment tab
    And User selects <Transaction_sub_type> in payment tab
    And User enters <Description> in payment tab
    And User clicks on Claim Deductible button in payment tab
    And User selects Attachment tab
    And User enter <Filename> in attachment tab
    And User selects <Authorisation> in attachment tab
    And User select <Attachment_type> in attachment tab
    And User selects <document_type> in attachment tab
    And User enters <description> in attachment tab
    And User click on Add Attachment button in attachment tab
    And User attaches file <file_path> in attachment tab
    And User clicks Asso party tab
    And User clicks Add row button
    And User clicks Add Info tab
    And User enters <total_estimate>
    And User enters <release_amount>
    And User clicks update button on Add info tab
    And User clicks Claim view button
    And User clicks on Update Claim button
    Then User should not see the red toast message
    And User should see green toast having message 'Claim details updated successfully'
    Examples:
    |claim_type|loss_type|service_rep|event_name|claim_status   |date|TransactionType|Transaction_sub_type|Description|Filename|Authorisation|Attachment_type|document_type|description|file_path|total_estimate|release_amount|
    |Fire Loss |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Claim Expense  |Description          |Testfile|Internal|Multiple Files|Denial|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Theft     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |OAE |Description          |Testfile|Internal|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Fire ( Including fire caused by lightning)|Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Legal Expense  |Description          |Testfile|External|Single File|DFS Complaint|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Lightning ( not resulting in fire )     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Mitigation   |Description          |Testfile|External|Single File|Engineer Report|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Collapse due to Sinkhole     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Other Legal   |Description          |Testfile|Internal|Single File|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Collapse due to all other cause of Collapse     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Subrogation  |Description          |Testfile|Internal|Single File|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Consequential Fungi , Wet , or Dry Rot or Bacteria Property losses     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Excess / Deductible   |Description          |Testfile|Internal|Single File|Assignment Of benefit|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |All other Losses (including Vandalism and Malicious Mischief)     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Excess / Deductible   |Description          |Testfile|Internal|Single File|Attorney Letter|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Loss Caused by other than Pollutant Hazard - Slip and Fall     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Excess / Deductible   |Description          |Testfile|Internal|Single File|Civil Remedy Notice|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Accidental Death     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Reserves                |Excess / Deductible   |Description          |Testfile|Internal|Single File|Claim Notification|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Condo Association Loss Assessment     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|Internal|Single File|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Roof Leak  - Large Tree Falling on The Roof     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Roof Leak  - Small branch falling on the Roof     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Refrigerator Like Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Water Heater Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Garbage Disposal Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Air conditioner Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Dishwasher Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Cloth Washer Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Pipe Under the Slab Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Pipe Behind the Wall Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Bathroom Leak     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Underground Water Seepage     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Window / Door Seepage     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Fence Damage     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Screen Enclosure Damage     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Tree Fell Not on Main Structure     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Food Spoilage     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Reset Reserves                |Excess / Deductible   |Description          |Testfile|External|Multiple Files|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|


#@web
#Feature: Avatar Edit Claim
#    As a claim user , I should be able to edit claim



Scenario Outline: Verify that user can edit claim wit Loss Payment type
    Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on claim in top navigation bar
    And User searches for claim number '20200115'
    And User clicks on search button on claim home page
    And User clicks on claim '20200115' in the results table
    And User clicks on edit button on claim page
    And User changes the claim type to <claim_type>
    And User changes the type of loss to <loss_type>
    And User changes the service rep to <service_rep>
    And User changes the event name to <event_name>
    And User changes the claim status open to <claim_status>

    When User clicks Payment tab
    And User enters <date> in payment tab
    And User selects <TransactionType> in payment tab
    And User selects <Transaction_sub_type> in payment tab
    And User enters <nameoncheck>
    And User enters <invoicedate>
    And User enters <invoiceduedate>
    And User enters <invoice>

    And User selects Attachment tab
    And User enter <Filename> in attachment tab
    And User selects <Authorisation> in attachment tab
    And User select <Attachment_type> in attachment tab
    And User selects <document_type> in attachment tab
    And User enters <description> in attachment tab
    And User click on Add Attachment button in attachment tab
    And User attaches file <file_path> in attachment tab

    And User clicks Asso party tab
    And User clicks Add row button

    And User clicks Add Info tab
    And User enters <total_estimate>
    And User enters <release_amount>
    And User clicks update button on Add info tab


    And User clicks Claim view button
    And User clicks on Update Claim button
    Then User should not see the red toast message
    And User should see green toast having message 'Claim details updated successfully'
    Examples:
    |claim_type|loss_type|service_rep|event_name|claim_status   |date|TransactionType|Transaction_sub_type|nameoncheck|invoicedate|invoiceduedate|invoice|Filename|Authorisation|Attachment_type|document_type|description|file_path|total_estimate|release_amount|
    |Fire Loss |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Payment               |OAE   |Description          |0724|0724|1 |Testfile|Internal|Single File|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
    |Theft     |Liability|Adam Hunt  |GORDON    |Open             |07242020|Loss Payment                |OAE   |Description          |0724|0724|1|Testfile|Internal|Single File|Acknowledge form|Description|C:\Users\samay\Pictures\a.jpg|1000|1000|
