# Python_Data_Warehouse_Automated_Testing

```
# Cucumber Report
pytest .\tests\steps\test_contact.py --cucumberjson=./target/cucumber.json
```

```
# conftest.py
# Place inside the tests folder.
# File is a global place to store fixtures.
@pytest.fixture
def my_global_fixture():
    return { }
```

```
# pytest.ini
# Place this file at the root of the project.
# Register annotations here.
[pytest]
markers = 
    contact: Run the contact feature
    fuzzy: Run the fuzzy feature
```

```
# Before Step and After Step
@pytest.fixture
def before_and_after_each_step():
    print('before step')
    yield
    print('after step')
```

```
# Parallel (pytest-xdist)
pytest .\tests\steps\test* -n 10
```

```
# Print
pytest .\tests\steps\test* -s
```

```
# Link features
scenarios('../features/name_of.feature')
```

```
# Scenario Context
@pytest.fixture
def scenario_context():
    return { }

@given('scenario context is used')
def _(scenario_context):
    pass
```

```
# Pass variable from step to step definition
@when(parsers.parse('the number is less than {some_number:d}))
def _(context, some_number):
    pass
```