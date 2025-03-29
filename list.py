# Initial Justice League list
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
# 1. Calculate the number of members
print("Number of members:", len(justice_league))
# 2. Add Batgirl and Nightwing
justice_league.extend(["Batgirl", "Nightwing"])
print("After recruiting Batgirl and Nightwing:", justice_league)
# 3. Move Wonder Woman to the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("After making Wonder Woman the leader:", justice_league)
# 4. Separate Aquaman and Flash by moving Superman in between them
justice_league.remove("Superman")
flash_index = justice_league.index("Flash")
justice_league.insert(flash_index, "Superman")
print("After separating Aquaman and Flash:", justice_league)
# 5. Replace the entire list with new members
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("After Superman assembles a new team:", justice_league)
# 6. Sort alphabetically
justice_league.sort()
print("After sorting alphabetically:", justice_league)
# Predicting the new leader (0th index)
print("New leader:", justice_league[0])