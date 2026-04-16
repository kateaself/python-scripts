# Pseudocode:
# 1. Ask the user for their name
# 2. Ask for their resting heart rate
# 3. Ask how many hours they are awake per day
# 4. Convert hours awake into minutes
# 5. Calculate total heartbeats while awake
# 6. Print a personalized message with the result

# Ask the user for their name
name = input("What is your name? ")

# Ask for biological data
heart_rate = int(input("Enter your resting heart rate (beats per minute): "))
hours_awake = int(input("How many hours are you awake per day? "))

# Calculations
minutes_awake = hours_awake * 60
total_beats = heart_rate * minutes_awake

# Output results
print("Hello,", name + "!")
print("While you are awake, your heart beats about", total_beats, "times per day.")
