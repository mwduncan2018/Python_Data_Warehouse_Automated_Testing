import json

from pytest_bdd import scenario, scenarios, given, when, then, parsers


scenarios('../features/source_1_to_landing_zone.feature')

@then("all orders from type 1 source arrive in the landing zone")
def _(scenario_context: dict):
    # This step is not implemented for the demo.
    pass 

@then("a blank order_location defaults to Online")
def _(scenario_context: dict):
    # This step is not implemented for the demo.
    pass

@then("all albums from type 1 source arrive in the landing zone")
def _(scenario_context: dict):
    # This step is not implemented for the demo.
    pass

@then("all customers from type 1 source arrive in the landing zone")
def _(scenario_context: dict):
    # This step is not implemented for the demo.
    pass