def filter_population(countries, population):
    filtered_countries = []

    population = int(population)
    for country in countries:
        if 'population' in country and isinstance(country['population'], (int, float)):
            if int(country['population']) > population:
                filtered_countries.append(country)
        else:

            print(f"Skipping country {country.get('name', 'Unknown')} due to missing or invalid population data.")
    return filtered_countries
