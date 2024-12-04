@landing_zone_to_core
Feature: Landing Zone to Core

Scenario: Order ETL, Orders Arrive, No Duplicates
  Given a type 1 source file
  And a type 2 source file
  When ETL is executed from sources to landing zone
  And ETL is executed from landing zone to core
  Then orders from the landing zone arrive in the core db
  And there are no duplicate orders

Scenario: Album ETL, Albums Arrive, No Duplicates
  Given a type 1 source file
  And a type 2 source file
  When ETL is executed from sources to landing zone
  And ETL is executed from landing zone to core
  Then albums from the landing zone arrive in the core db
  And there are no duplicate albums

@skip
Scenario: Album ETL, Conversion to Fahrenheit
  Given a type 1 source file
  When ETL is executed from sources to landing zone
  And ETL is executed from landing zone to core
  Then temperature is displayed as fahrenheit 

Scenario: Customer ETL, No Duplicates
  Given a type 2 source file
  When ETL is executed from sources to landing zone
  And ETL is executed from landing zone to core
  Then customers from the landing zone arrive in the core db
  And there are no duplicate customers

Scenario: Customer ETL, Conversion to First Name and Last Name
  Given a type 2 source file
  When ETL is executed from sources to landing zone
  And ETL is executed from landing zone to core
  Then the Full Name field has been converted to First Name and Last Name
