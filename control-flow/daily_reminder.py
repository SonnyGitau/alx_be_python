#prompt for user input
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()
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