task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound =  input("Is it time-bound? (yes/no): ").lower()
#while priority not in ("high", "medium", "low"):
   # print("Please enter a valid priority: high, medium, or low: ")
    #priority 
match priority:
    case "high":
        message = f"High-priority task: {task}."
    case "medium":
        message = f"Medium-priority task: {task}."
    case "low":
        message = f"Low-priority task: {task}."

# Modify message if time-sensitive
if time_bound == "yes":
    message += " This task requires immediate attention today!"

# Provide the Customized Reminder
print(message)