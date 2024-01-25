regions = ["Africa", "Americas", "Asia", "Europe", "Oceania", "Polar"]


def filter_region():

    print("What region do you want to filter on?")
    for i, region in enumerate(regions):
        print(f"{i + 1}. {region}")
    region_choice = input("Enter your choice: ")
    if region_choice.isdigit() and 0 < int(region_choice) <= len(regions):
        region = regions[int(region_choice) - 1]
        return region
    else:
        print("Please enter a valid option")
