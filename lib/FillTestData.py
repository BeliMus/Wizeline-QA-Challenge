import json
import lib.Constants as Constants


def fill_data(parameters):
    settings = open("./conf/settings.json")
    test_drivers = json.load(settings)
    test_data = []
    for driver in test_drivers['drivers']:
        data_to_add = []
        if driver.lower() == "chrome":
            data_to_add.append(Constants.CHROME)
            test_data.append(add_parameters(data_to_add, parameters))
        elif driver.lower() == "firefox":
            data_to_add.append(Constants.FIREFOX)
            test_data.append(add_parameters(data_to_add, parameters))
    if len(test_data) == 0:
        test_data.append([Constants.CHROME, *parameters])
    return test_data


def add_parameters(data_to_add, parameters):
    return data_to_add + parameters
