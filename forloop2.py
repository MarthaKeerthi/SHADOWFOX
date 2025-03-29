total_jumping_jacks = 100
jumping_jacks_per_set = 10
completed_jumping_jacks = 0
while completed_jumping_jacks < total_jumping_jacks:
    # Perform 10 jumping jacks
    completed_jumping_jacks += jumping_jacks_per_set
    print(f"You have completed {completed_jumping_jacks} jumping jacks.")
    # Check if the workout is complete
    if completed_jumping_jacks >= total_jumping_jacks:
        print("Congratulations! You completed the workout.")
        break
    # Ask if the user is tired
    tired = input("Are you tired? (yes/y or no/n): ").strip().lower()
    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/y or no/n): ").strip().lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed_jumping_jacks} jumping jacks.")
            break
        else:
            remaining = total_jumping_jacks - completed_jumping_jacks
            print(f"{remaining} jumping jacks remaining. Keep going!")