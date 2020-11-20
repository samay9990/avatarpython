@web
Feature: Avatar add Producer
    As a Avatar User, I should be able to add producer

@p1 @producer @add_producer
Scenario: Verify producer add feature
      Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on producer in top navigation bar
    And User clicks on Add Agency
    And User clicks Save Agency
    Then User verifies Please Enter Unique No! toast message

    @p1 @producer @add_producer
Scenario Outline: Verify producer add feature agency code error
    Given User is on Avatar Insurance Login Page
    When User logs in with user 'claim_user'
    And User clicks on producer in top navigation bar
    And User clicks on Add Agency
    And User enters <agency_code>
    And User clicks Save Agency
    Then User verifies Please Enter Agency Name toast message
    Examples:
        | agency_code |
        | 2222        |

    @p1 @producer @add_producer
    Scenario Outline: Verify producer add feature agency name error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User enters <agency_code>
        And User clicks Save Agency
        Then User verifies Please Enter Agency Name toast message
        Examples:
            | agency_code |
            | 2222        |

    @p1 @producer @add_producer
    Scenario Outline: Verify producer add feature dba name error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User clicks Save Agency
        Then User verifies Please Enter Agency DBA Name toast message
        Examples:
            | agency_code |agency_name|
            | 2222        |bb         |

    @p1 @producer @add_producer
    Scenario Outline: Verify producer add feature fein name error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User enters <dba_name>
        And User clicks Save Agency
        Then User verifies Please FEIN Number toast message
        Examples:
            | agency_code | agency_name |dba_name|
            | 2222        | bb          |    aa  |

    @p1 @producer @add_producer
    Scenario Outline: Verify producer add feature agency address error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User enters <dba_name>
        And User enters <fein_number>
        And User clicks Save Agency
        Then User verifies Please Agency Address toast message
        Examples:
            | agency_code | agency_name | dba_name | fein_number |
            | 2222        | bb          | aa       | 111111111   |

    @p1 @producer @add_producer @producer_demo
    Scenario Outline: Verify producer add feature zipcode error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User enters <dba_name>
        And User enters <fein_number>
        And User enters <agency_address>
        And User clicks Save Agency
        Then User verifies Please Enter Agency Zipcode toast message
        Examples:
            | agency_code | agency_name | dba_name | fein_number | agency_address |
            | 2222        | bb          | aa       | 111111111   | Test           |

        @p1 @producer @add_producer
    Scenario Outline: Verify producer add feature agency phone error
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User enters <dba_name>
        And User enters <fein_number>
        And User enters <agency_address>
        And User enters <zip>
        And User clicks checkbox
        And User clicks Save Agency
        Then User verifies Please Enter Agency Phone toast message
        Examples:
            | agency_code | agency_name | dba_name | fein_number | agency_address |zip|
            | 2222        | bb          | aa       | 111111111   | Test           |10001|

    @p1 @producer @add_producer @producer_demo
    Scenario Outline: Verify producer add feature all parameters
        Given User is on Avatar Insurance Login Page
        When User logs in with user 'claim_user'
        And User clicks on producer in top navigation bar
        And User clicks on Add Agency
        And User enters <agency_code>
        And User enters <agency_name>
        And User selects <select_group>
        And User selects <uv>
        And User enters <payee_name>
        And User selects <agency_status>
        And User selects <service_rep>
        And User enters <dba_name>
        And User enters <fein_number>
        And User enters <agency_address>
        And User enters <zip>
        And User clicks checkbox
        And User enters <web>
        And User enters <phone>
        And User enters <fax>
        And User selects <direct_deposit>
        And User enters <manager>
        And User enters <manager_phone>
        And User enters <manager_email>
        And User enters <principal>
        And User enters <principal_phone>
        And User enters <principal_email>
        And User enters <bank_acc>
        And User enters <bank_name>
        And User enters <routingno>
        And User clicks add row in License Information
        And User selects <license_type>
        And User enters <license_no>
        And User selects <state>
        And User selects <appointed>
        And User inputs <issue_date>
        And User inputs <exp_date>
        And User inputs <app_date>
        And User clicks on Products button
        And User clicks add row in product
        And User selects <policy_product>
        And User clicks close
        And User clicks Save Agency
        #Then User verifies successful toast message


        #change agency_code whenever you run the test case , as this user must be already added"

        Examples:
            | agency_code | agency_name |select_group|uv|payee_name|agency_status|service_rep| dba_name | fein_number | agency_address |zip|web|phone|fax|direct_deposit|manager|manager_phone|manager_email|principal|principal_phone|principal_email|bank_acc|bank_name|routingno|license_type|license_no|state|appointed|issue_date|exp_date|app_date|policy_product|
            | test_agency_2616| test11          |Florida Insurance| OPSI ROOFING SW|test11|Active| OPSI ROOFING SW| test1       | 111111111   | Test           |10001|a.com|1111111111|1111111111|Direct Deposit|test|1111111111|a@a.com|test|1111111111|a@a.com|1234|hdfc|123|Active|1234|ALABAMA|AVATAR APPOINTED|06302020|06202030|10162020|MH HO3|
