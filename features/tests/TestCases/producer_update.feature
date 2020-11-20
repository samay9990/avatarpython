@web
Feature: Avatar Update Producer
    As a Avatar user, I should be able to update producer details

@p1 @producer @update_producer @producer_demo
    Scenario Outline: Verify producer update feature
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Search Agency button
        And User enters <agency_code>
        And User enters <fein_number>
        And User clicks on search button
        And User selects <search_value>
        And User lands on searched agency form with <verify_agency_code>
        And User inputs new <payee_name>
#    #Agency Visit Review tab
#        And User clicks Agency Visit Review
#        And User clicks Add Log
#        And User enters <visit_date>
#        And User enters <previsit>
#        And User enters <staffnotes>
#        And User enters <agentrequests>
#        And User enters <visitreview>
#        And User clicks Submit
    #Document tab
        And User clicks on Document
        And User enters <file_name>
        And User selects file_type
        And User inputs <file>
        And User inputs <upload_date>
        And User clicks submit document
        And User clicks close document
    #Agency user tab
        And User clicks Agency User
        And User enters <user_id>
        And User enters <sub_agent>
        And User enters <first_name>
        And User enters <middle_name>
        And User enters <last_name>
        And User enters <screen_name>
        And User enters <email>
        And User enters <phone>
        And User selects <status>
        And User selects <user_level>
        And User enters <effdatefrom>
        And User enters <effdateto>
        And User clicks on Add Row
        And User selects <product>
        And User selects <state>
        And User selects <uvassigned>
        And User selects <authorization>
        And User clicks Save Agency User
        And User clicks Close

        And User clicks update button

        Then User verifies successful toast message
    #Update log tab
        And User verifies in the updated log the <new_value>

    #User different <user_id> value in Agency Visit Review tab as the mentioned user must already have been added
        Examples:
            | agency_code            | fein_number| search_value |verify_agency_code|payee_name|file_name|file| upload_date |user_id|sub_agent|first_name|middle_name|last_name|screen_name|email|phone|status|user_level|effdatefrom|effdateto|product|state|uvassigned|authorization|new_value|
            |test_agency_2607      |111111111|test_agency_2607       |test_agency_2607      |PayeeTest123 |Test_File|a.jpg|07071991|19_test|agency_test_12|test1|test2|test3|test_screen|abc@gmail.com|111111111111111|Active|NewAdmin|10202020|10202022|MH HO3|FLORIDA| OPSI ROOFING SW|View Only|PayeeTest|

