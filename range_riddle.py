#Objective: The aim of this assignment is to
#  deepen your understanding of Python's range() function.
# Task 1: Your Mood Today Write a program that prints off
#  different moods for each day of the week. Create a list 
# of moods such as "Happy", "Sad", "Energetic", and "Calm". 
# Using the range() function, loop through every day of the
#  week and for each day, randomly select a mood from the
#  list and print it. Ensure that your program includes the
#  use of the random module to select the mood.
# 
# Example Outcome: An example output could be "On Wednesday, 
# you were feeling happy." "On Thursday you were feeling sad."

import random
my_moods=["sad", "happy", "angry", "bored", "lonely", "tired", "energetic"]
week_days=["Sunday","Monday","Tuesday","Wednesday", "Thursday", "Friday", "Saturday"]

for day in range(7):
    todays_mood=random.choice(my_moods)
    print(f"On {week_days[day]} you were feeling {todays_mood}.")
    