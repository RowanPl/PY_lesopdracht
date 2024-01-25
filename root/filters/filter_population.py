def filter_population(countries, population):
    filtered_countries = []
    # Convert population to integer
    population = int(population)
    for country in countries:
        # Check if the country has a 'population' key and if the population value is numeric
        if 'population' in country and isinstance(country['population'], (int, float)):
            if int(country['population']) > population:
                filtered_countries.append(country)
        else:
            # Handle cases where the country does not have a 'population' key or the value is not numeric
            print(f"Skipping country {country.get('name', 'Unknown')} due to missing or invalid population data.")
    return filtered_countries
