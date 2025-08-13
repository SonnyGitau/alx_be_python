#prompt for user input
task = input("Enter your task ")
priority = input("Priority (high, medium, low) ")
time_bound = input("Is the task time-bound? (yes or no) ")
# Provide a customized reminder using match case
match priority:
    case "high":
        reminder = f"Reminder: You have a high priority task - '{task}'."
    case "medium":
        reminder = f"Reminder: You have a medium  priority task - '{task}'."
    case "low":
        reminder = f"Reminder: You have a low priority task - '{task}'."
    case _:
         reminder = f"Reminder: You have a task - '{task}' with unspecified priority."
     # Modify message if the task is time-bound
if time_bound == "yes":  
    reminder += " This is time-sensitive task that requires immediate attention today!"
# Print the customized reminder
print(reminder)