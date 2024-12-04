import json

from pytest_bdd import scenario, scenarios, given, when, then, parsers


scenarios('../features/source_2_to_landing_zone.feature')

@then("all orders from type 2 source arrive in the landing zone")
def _(scenario_context: dict):
    # Get all orders in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = """SELECT full_name, first_name, last_name, band_name, album_name, order_location FROM orders 
            JOIN customers ON orders.customer_id = customers.customer_id 
            JOIN albums ON customers.album_id = albums.album_id
            """
    landing_zone_cur.execute(sql)
    lz_orders = landing_zone_cur.fetchall()

    # Get source 2
    source_2 = scenario_context['source_2']

    # Verify all orders from source 2 are in the landing zone
    for source_2_order in source_2["Orders"]:
        found = False
        for lz_order in lz_orders:
            lz_first_name = lz_order[1]
            lz_last_name = lz_order[2]
            if not lz_order[0] == "":
                lz_first_name = lz_order[0].split(' ')[0]
                lz_last_name = lz_order[0].split(' ')[1]
            if (source_2_order["Customer"]["FirstName"] == lz_first_name and
                source_2_order["Customer"]["LastName"] == lz_last_name and
                source_2_order["OrderLocation"] == lz_order[5] and 
                source_2_order["Album"]["AlbumName"] == lz_order[4] and
                source_2_order["Album"]["BandName"] == lz_order[3]):
                found = True
        error_message = "Order from source 2 was not found in landing zone: " + source_2_order["Customer"]["FirstName"] + ', ' + source_2_order["Customer"]["LastName"] + ', ' + source_2_order["OrderLocation"] + ', ' + source_2_order["Album"]["BandName"] + ', ' + source_2_order["Album"]["AlbumName"]
        assert found == True, error_message

@then("all albums from type 2 source arrive in the landing zone")
def _(scenario_context: dict):
    # Get albums in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT band_name, album_name FROM albums;"
    landing_zone_cur.execute(sql)
    lz_albums = landing_zone_cur.fetchall()

    # Get source 2
    source_2 = scenario_context['source_2']

    # Verify all orders from source 2 are in the landing zone
    for source_2_order in source_2["Orders"]:
        found = False
        for lz_album in lz_albums:
            if (source_2_order["Album"]["AlbumName"] == lz_album[1] and 
                source_2_order["Album"]["BandName"] == lz_album[0]):
                found = True
        assert found == True, "Album from source 2 was not found in landing zone: " + source_2_order["Album"]["BandName"] + ', ' + source_2_order["Album"]["AlbumName"]

@then("all customers from type 2 source arrive in the landing zone")
def _(scenario_context: dict):
    # Get customers in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT full_name, first_name, last_name FROM customers;"
    landing_zone_cur.execute(sql)
    lz_customers = landing_zone_cur.fetchall()

    # Get source 2
    source_2 = scenario_context['source_2']

    # Verify all customers from source 2 are in the landing zone 
    for source_2_order in source_2["Orders"]:
        source_2_first_name = source_2_order["Customer"]["FirstName"]
        source_2_last_name = source_2_order["Customer"]["LastName"]
        found = False
        for lz_customer in lz_customers:
            if (source_2_first_name == lz_customer[1] and 
                source_2_last_name == lz_customer[2]):
                found = True
        assert found == True, "Customer from source 2 was not found in the landing zone: " + source_2_first_name + ' ' + source_2_last_name