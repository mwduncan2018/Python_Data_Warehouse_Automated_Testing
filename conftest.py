import os
import json
import psycopg2
import pytest

from pytest_bdd import given, when, then, parsers 
from configprovider.config_provider import ConfigProvider


# Scenario Context

@pytest.fixture 
def scenario_context():
    # Connect to the landing zone database
    landing_zone_conn = psycopg2.connect(
        host=ConfigProvider.get_landing_zone_host(), 
        port=ConfigProvider.get_landing_zone_port(), 
        database=ConfigProvider.get_landing_zone_database(), 
        user=ConfigProvider.get_landing_zone_user(), 
        password=ConfigProvider.get_landing_zone_password()
        )
    landing_zone_cur = landing_zone_conn.cursor()

    # Connect to the core database
    core_conn = psycopg2.connect(
        host=ConfigProvider.get_core_host(), 
        port=ConfigProvider.get_core_port(), 
        database=ConfigProvider.get_core_database(), 
        user=ConfigProvider.get_core_user(), 
        password=ConfigProvider.get_core_password()
        )
    core_cur = core_conn.cursor()

    # Put connections in the scenario context dict
    sc = { }
    sc["landing_zone_cur"] = landing_zone_cur
    sc["core_cur"] = core_cur
    
    # Yield scenario context
    yield sc
    
    # Close landing zone connection
    landing_zone_cur.close()
    landing_zone_conn.close()

    # Close core connection
    core_cur.close()
    core_conn.close()


# Shared steps 

@given("a type 1 source file")
def _(scenario_context: dict):
    with open('sources/source_1.json', 'r') as file:
        source_1 = json.load(file)
        scenario_context['source_1'] = source_1

@given("a type 2 source file")
def _(scenario_context: dict):
    with open('sources/source_2.json', 'r') as file:
        source_2 = json.load(file)
        scenario_context['source_2'] = source_2

@given("ETL is executed from landing zone to core")
def _(scenario_context: dict):
    # This demo is a mock data warehouse.
    # In an actual data warehouse, execute ETL from landing zone to core here.
    pass

@when("ETL is executed from sources to landing zone")
def _(scenario_context: dict):
    # This demo is a mock data warehouse.
    # In an actual data warehouse, execute ETL from sources to landing zone here.
    pass

@when("ETL is executed from landing zone to core")
def _(scenario_context: dict):
    # This demo is a mock data warehouse.
    # In an actual data warehouse, execute ETL from landing zone to core here.
    pass
