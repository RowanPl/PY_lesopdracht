from root.API.apicall import *
from root.helper.apply_filters import apply_filters
from root.options.filtered_options import filtered_options

countries = []
options = {
    "region": "",
    "population": "",
    "borders": {
        "least": "",
        "most": ""
    },
    "languages": "",
    "currencies": ""
}


def main_code():
    global countries
    global options

    # Check if any filters are set
    filters_set = any(value != "" for value in options.values() if type(value) is not dict)
    filters_set = filters_set or any(value != "" for value in options["borders"].values())
    if not filters_set:
        option_choice = input(  # ask the user what they want to do
            "What do you want to do? \n 1. See the full data \n 2. Filter Data \n 9. Exit \n")
    else:
        option_choice = input(  # ask the user what they want to do
            "What do you want to do? \n 1. See the full data \n 2. Filter Data \n 3. See the filtered data \n 9. Exit "
            "\n")

    if option_choice == "1":
        if options["region"] != "":
            countries = get_data_region(options["region"])
        else:
            countries = get_data()
        json_text(countries)
        main_code()

    elif option_choice == "2":
        countries = filtered_options(options, countries)[1]
        main_code()

    elif option_choice == "3":
        # if any(value != "" for value in options.values()):
        #     countries = apply_filters(options, countries)  # Function to apply filters and retrieve filtered data
        countries = apply_filters(options, countries)  # Function to apply filters and retrieve filtered data
        json_text(countries)
        main_code()

    elif option_choice == "9":
        exit()

    else:
        print("Please enter a valid option")
        main_code()


if __name__ == '__main__':
    main_code()
