import random
# Number of rolls
num_rolls = 20
# Counters
count_6 = 0
count_1 = 0
count_two_6s = 0
previous_roll = 0  # To track consecutive rolls
# Simulate rolling the die
for _ in range(num_rolls):
    roll = random.randint(1, 6)  # Roll the die
    print(roll, end=" ")  # Display rolls

    if roll == 6:
        count_6 += 1
        if previous_roll == 6:
            count_two_6s += 1  # Check for consecutive sixes
    if roll == 1:
        count_1 += 1
    previous_roll = roll  # Update previous roll
# Print statistics
print("\nStatistics:")
print("Number of times rolled a 6:", count_6)
print("Number of times rolled a 1:", count_1)
print("Number of times two 6s appeared in a row:", count_two_6s)