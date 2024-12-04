@source_2_to_landing_zone
@source_to_landing_zone
Feature: Source 2 to Landing Zone

Scenario: Order ETL
  Given a type 2 source file
  When ETL is executed from sources to landing zone
  Then all orders from type 2 source arrive in the landing zone 

Scenario: Album ETL
  Given a type 2 source file
  When ETL is executed from sources to landing zone
  Then all albums from type 2 source arrive in the landing zone 

Scenario: Customer ETL
  Given a type 2 source file
  When ETL is executed from sources to landing zone
  Then all customers from type 2 source arrive in the landing zone 