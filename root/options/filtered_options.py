from root.API.apicall import get_data
from root.helper.apply_filters import apply_filters
from root.filters.filter_border import filter_border
from root.filters.filter_population import filter_population
from root.filters.filter_region import filter_region

filter_options = ["region", "population", "borders", "languages", "currencies"]


def filtered_options(options, countries):
    if countries == []:
        countries = get_data()

    print("What do you want to filter on?")

    for i, option in enumerate(filter_options):
        print(f"{i + 1}. {option}")

    filter_choice = input("Enter your choice: ")

    if filter_choice == "1":
        options["region"] = filter_region()
    elif filter_choice == "2":
        options["population"] = input("What is the minimum population you want to filter on? ")
        countries = filter_population(countries, options["population"])
    elif filter_choice == "3":
        options["borders"]["least"] = int(input("What is the minimum amount of borders you want to filter on? "))
        options["borders"]["most"] = int(input("What is the maximum amount of borders you want to filter on? "))
        if options["borders"]["least"] > options["borders"]["most"]:
            print("The minimum amount of borders can't be higher than the maximum amount of borders")
            options["borders"] = {"least": 0, "most": 999}
            return filtered_options(options, countries)

        countries = filter_border(countries, options["borders"])
    elif filter_choice == "4":
        options["languages"] = input("What is the language you want to filter on? ")
    elif filter_choice == "5":
        options["currencies"] = input("What is the currency you want to filter on? ")
    elif filter_choice == "9":
        exit()
    else:
        print("Please enter a valid option")
        return filtered_options(options, countries)

    countries = apply_filters(options, countries)
    return options, countries
