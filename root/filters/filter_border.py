def filter_border(countries, options):
    least = options['least']
    most = options['most']

    filtered_countries = []
    for country in countries:
        num_borders = len(country.get('borders', []))  # Get the number of borders; if 'borders' key is missing, return an empty list

        # Filter countries based on the number of borders
        if least <= num_borders <= most:
            filtered_countries.append(country)

    return filtered_countries
