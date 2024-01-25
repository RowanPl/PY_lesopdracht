def filter_border(countries, options):
    least = options['least']
    most = options['most']

    filtered_countries = []
    for country in countries:
        num_borders = len(country.get('borders', []))

        if least <= num_borders <= most:
            filtered_countries.append(country)

    return filtered_countries
