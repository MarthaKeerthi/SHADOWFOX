city_to_country = {
    "Sydney": "Australia",
    "Melbourne": "Australia",
    "Brisbane": "Australia",
    "Perth": "Australia",
    "Dubai": "UAE",
    "Abu Dhabi": "UAE",
    "Sharjah": "UAE",
    "Ajman": "UAE",
    "Mumbai": "India",
    "Bangalore": "India",
    "Chennai": "India",
    "Delhi": "India"
}
# Get user input
city1 = input("Enter the first city: ").strip()
city2 = input("Enter the second city: ").strip()
# Check if both cities are in the dictionary
if city1 in city_to_country and city2 in city_to_country:
    if city_to_country[city1] == city_to_country[city2]:
        print(f"Both cities are in {city_to_country[city1]}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list")