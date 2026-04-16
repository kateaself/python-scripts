# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
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