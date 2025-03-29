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
city = input("Enter a city name: ").strip()
# Check if the city is in the dictionary
if city in city_to_country:
    print(f"{city} is in {city_to_country[city]}")
else:
    print("City not found in the list")