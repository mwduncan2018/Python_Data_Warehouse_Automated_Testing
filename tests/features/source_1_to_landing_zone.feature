@source_1_to_landing_zone
@source_to_landing_zone
@todo
Feature: Source 1 to Landing Zone

Scenario: Order ETL
  Given a type 1 source file
  When ETL is executed from sources to landing zone
  Then all orders from type 1 source arrive in the landing zone 

Scenario: Order ETL, Blank Order Location Defaults to Online
  Given a type 1 source file
  When ETL is executed from sources to landing zone
  Then a blank order_location defaults to Online

Scenario: Album ETL
  Given a type 1 source file
  When ETL is executed from sources to landing zone
  Then all albums from type 1 source arrive in the landing zone 

Scenario: Customer ETL
  Given a type 1 source file
  When ETL is executed from sources to landing zone
  Then all customers from type 1 source arrive in the landing zone 