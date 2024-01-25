from root.API.apicall import get_data_region, get_data
from root.filters.filter_border import filter_border
from root.filters.filter_population import filter_population


def apply_filters(options, countries):
    if countries == [""] and options["region"] == "":
        countries = get_data()
    if options["region"] != "":
        countries = get_data_region(options["region"])

    filtered_countries = countries[:]  # Make a copy of the original list


    # Apply filters based on the options dictionary
    if options["region"]:
        # Filter countries by region
        filtered_countries = [country for country in filtered_countries if country["region"] == options["region"]]
    if options["population"]:
        # Filter countries by population
        filtered_countries = filter_population(filtered_countries, options["population"])

    if options["borders"]["least"] and options["borders"]["most"]:
        # Filter countries by number of borders
        filtered_countries = filter_border(filtered_countries, options["borders"])

    if options["languages"]:
        # Filter countries by languages spoken
        filtered_countries = [country for country in filtered_countries if options["languages"] in country["languages"]]

    if options["currencies"]:
        # Filter countries by currencies
        filtered_countries = [country for country in filtered_countries if options["currencies"] in country["currencies"]]

    return filtered_countries
