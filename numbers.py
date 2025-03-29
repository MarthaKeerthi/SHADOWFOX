def formatted_string(num, char):
    return "Formatted Output: {} {}".format(num, char)
result = formatted_string(145, 'o')
print(result)
#calculating area
pi = 3.14
radius = 84
# Area of the pond
pond_area = pi * (radius ** 2)
# Water calculation
water_per_sq_meter = 1.4
total_water = pond_area * water_per_sq_meter
# Print without decimals
print("Total Water in Pond:", int(total_water))
#speed
distance = 490  # meters
time = 7 * 60  # converting minutes to seconds
# Speed calculation
speed = distance / time
# Print without decimals
print("Speed:", int(speed))