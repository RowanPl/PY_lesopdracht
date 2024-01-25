
def json_text(filtered_data):
    for country in filtered_data:

        print("---------------------------")
        print(country['name']['common'] + " (" + country['flag'] + ")")

        if 'capital' in country:
            print(country['capital'])
        print(country['region'])
        if 'subregion' in country:
            print(country['subregion'])
        print(country['population'])
        if 'borders' in country:
            print("has " + str(len(country['borders'])) + " borders")
        else:
            print("has no borders")
    print("\ntotal of countries: " + str(len(filtered_data)) + " countries")