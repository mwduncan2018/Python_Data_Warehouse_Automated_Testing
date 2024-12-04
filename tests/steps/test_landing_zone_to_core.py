import json

from pytest_bdd import scenario, scenarios, given, when, then, parsers


scenarios('../features/landing_zone_to_core.feature')

@then("orders from the landing zone arrive in the core db")
def _(scenario_context: dict):
    # Get orders in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = """SELECT full_name, first_name, last_name, band_name, album_name, order_location FROM orders 
            JOIN customers ON orders.customer_id = customers.customer_id 
            JOIN albums ON customers.album_id = albums.album_id
            """
    landing_zone_cur.execute(sql)
    lz_orders = landing_zone_cur.fetchall()

    # Get orders in core 
    core_cur = scenario_context['core_cur']
    sql = """SELECT first_name, last_name, band_name, album_name, order_location FROM orders 
            JOIN customers ON orders.customer_id = customers.customer_id 
            JOIN albums ON customers.album_id = albums.album_id
            """
    core_cur.execute(sql)
    core_orders = core_cur.fetchall()

    # Verify orders in the landing zone appears in the core
    lz_order = lz_orders[0]
    if (lz_order[1] == "" and lz_order[2] == ""):
        lz_order_first_name = lz_order[0].split(' ')[0]
        lz_order_last_name = lz_order[0].split(' ')[1]

    for core_order in core_orders:
        if (core_order[0] == lz_order_first_name and core_order[1] == lz_order_last_name):
            assert core_order[2] == lz_order[3] # Verify band name
            assert core_order[3] == lz_order[4] # Verify album name
            assert core_order[4] == lz_order[5] # Verify location

    if (lz_order[1] == "" and lz_order[2] == ""):
        lz_order_first_name = lz_order[0].split(' ')[0]
        lz_order_last_name = lz_order[0].split(' ')[1]

    for core_order in core_orders:
        if (core_order[0] == lz_order_first_name and core_order[1] == lz_order_last_name):
            assert core_order[2] == lz_order[3] # Verify band name
            assert core_order[3] == lz_order[4] # Verify album name
            assert core_order[4] == lz_order[5] # Verify location

@then("there are no duplicate orders")
def _(scenario_context: dict):
    # Get all orders in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = """SELECT full_name, first_name, last_name, band_name, album_name, order_location FROM orders 
            JOIN customers ON orders.customer_id = customers.customer_id 
            JOIN albums ON customers.album_id = albums.album_id
            """
    landing_zone_cur.execute(sql)
    lz_orders = landing_zone_cur.fetchall()

    # Get all orders in core 
    core_cur = scenario_context['core_cur']
    sql = """SELECT first_name, last_name, band_name, album_name, order_location FROM orders 
            JOIN customers ON orders.customer_id = customers.customer_id 
            JOIN albums ON customers.album_id = albums.album_id
            """
    core_cur.execute(sql)
    core_orders = core_cur.fetchall()

    for lz_order in lz_orders:
        count = 0
        for core_order in core_orders:
            if ((core_order[0] == lz_order[1] or core_order[0] == lz_order[0].split(' ')[0]) and # First name match
                (core_order[1] == lz_order[2] or core_order[1] == lz_order[0].split(' ')[1]) and # Last name match
                (core_order[2] == lz_order[3]) and # Band match
                (core_order[3] == lz_order[4]) and # Album match
                (core_order[4] == lz_order[5])): # Location match
                count += 1
                if (count == 2):
                    error_message = "Duplicate order should not occur: " + str(core_order)
                    assert count == 1, error_message

@then("albums from the landing zone arrive in the core db")
def _(scenario_context: dict):
    # Get albums in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT band_name, album_name FROM albums;"
    landing_zone_cur.execute(sql)
    lz_albums = landing_zone_cur.fetchall()

    # Get albums in core 
    core_cur = scenario_context['core_cur']
    sql = "SELECT band_name, album_name FROM albums;"
    core_cur.execute(sql)
    core_albums = core_cur.fetchall()

    # Verify orders in the landing zone appears in the core
    for lz_album in lz_albums:
        found = False
        for core_album in core_albums:
            if (lz_album[0] == core_album[0] and lz_album[1] == core_album[1]):
                found = True
        assert found == True, "Album not found in core: " + str(lz_album)

@then("there are no duplicate albums")
def _(scenario_context: dict):
    # Get albums in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT band_name, album_name FROM albums;"
    landing_zone_cur.execute(sql)
    lz_albums = landing_zone_cur.fetchall()

    # Get albums in core 
    core_cur = scenario_context['core_cur']
    sql = "SELECT band_name, album_name FROM albums;"
    core_cur.execute(sql)
    core_albums = core_cur.fetchall()

    # Verify no duplicate albums appear in the core
    for lz_album in lz_albums:
        count = 0
        for core_album in core_albums:
            if (lz_album[0] == core_album[0] and lz_album[1] == core_album[1]):
                count += 1
        assert count == 1, "Duplicate albums should not occur: " + str(core_album)

@then("temperature is displayed as fahrenheit")
def _(scenario_context: dict):
    pass

@then("customers from the landing zone arrive in the core db")
def _(scenario_context: dict):
    # Get customers in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT full_name, first_name, last_name FROM customers;"
    landing_zone_cur.execute(sql)
    lz_customers = landing_zone_cur.fetchall()

    # Get customers in core 
    core_cur = scenario_context['core_cur']
    sql = "SELECT first_name, last_name FROM customers;"
    core_cur.execute(sql)
    core_customers = core_cur.fetchall()

    # Verify customers appear in the core
    for lz_customer in lz_customers:
        lz_first_name = lz_customer[1]
        lz_last_name = lz_customer[2]
        if not (lz_customer[0] == ""):
            lz_first_name = lz_customer[0].split(' ')[0]
            lz_last_name = lz_customer[0].split(' ')[1]
        found = False
        for core_customer in core_customers:
            if (lz_first_name == core_customer[0] and lz_last_name == core_customer[1]):
                found = True
        assert found == True, "Customer not found in core: " + str(lz_first_name + ' ' + lz_last_name)
    
@then("there are no duplicate customers")
def _(scenario_context: dict):
    # Get customers in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT full_name, first_name, last_name FROM customers;"
    landing_zone_cur.execute(sql)
    lz_customers = landing_zone_cur.fetchall()

    # Get customers in core 
    core_cur = scenario_context['core_cur']
    sql = "SELECT first_name, last_name FROM customers;"
    core_cur.execute(sql)
    core_customers = core_cur.fetchall()

    # Verify there are no duplicate customers
    for lz_customer in lz_customers:
        lz_first_name = lz_customer[1]
        lz_last_name = lz_customer[2]
        if not (lz_customer[0] == ""):
            lz_first_name = lz_customer[0].split(' ')[0]
            lz_last_name = lz_customer[0].split(' ')[1]
        count = 0
        for core_customer in core_customers:
            if (lz_first_name == core_customer[0] and lz_last_name == core_customer[1]):
                count += 1
        assert count == 1, "Duplicate customer should not occur: " +lz_first_name + ' ' + lz_last_name

@then("the Full Name field has been converted to First Name and Last Name")
def _(scenario_context: dict):
    # Get customers in the landing zone
    landing_zone_cur = scenario_context['landing_zone_cur']
    sql = "SELECT full_name, first_name, last_name FROM customers;"
    landing_zone_cur.execute(sql)
    lz_customers = landing_zone_cur.fetchall()

    # Get customers in core 
    core_cur = scenario_context['core_cur']
    sql = "SELECT first_name, last_name FROM customers;"
    core_cur.execute(sql)
    core_customers = core_cur.fetchall()

    # Verify the full name field has been converted to first name and last name
    for lz_customer in lz_customers:
        if not (lz_customer[0] == ""):
            lz_first_name = lz_customer[0].split(' ')[0]
            lz_last_name = lz_customer[0].split(' ')[1]
            found = False
            for core_customer in core_customers:
                if (lz_first_name == core_customer[0] and lz_last_name == core_customer[1]):
                    found = True
            assert found == True, "Full name field was not converted: " + str(lz_first_name + ' ' + lz_last_name)