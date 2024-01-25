from root.api.apicall import get_data_region, get_data
from root.filters.filter_border import filter_border
from root.filters.filter_population import filter_population


def apply_filters(options, countries):
    if countries == [""] and options["region"] == "":
        countries = get_data()
    if options["region"] != "":
        countries = get_data_region(options["region"])

    filtered_countries = countries[:]



    if options["region"]:

        filtered_countries = [country for country in filtered_countries if country["region"] == options["region"]]
    if options["population"]:

        filtered_countries = filter_population(filtered_countries, options["population"])

    if options["borders"]["least"] and options["borders"]["most"]:

        filtered_countries = filter_border(filtered_countries, options["borders"])

    if options["languages"]:

        filtered_countries = [country for country in filtered_countries if options["languages"] in country["languages"]]

    if options["currencies"]:

        filtered_countries = [country for country in filtered_countries if options["currencies"] in country["currencies"]]

    return filtered_countries
