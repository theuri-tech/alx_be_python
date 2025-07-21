# Program to create a single, priority task reminder.
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while priority not in ("high", "medium", "low"):
    priority = input("Please enter a valid priority; high, medium, low: ")
while time_bound not in ("yes", "no"):
    time_bound = input("Kindly type yes or no: ")
match priority:
    case "high":
        reminder = f"{task} is a high priority task"
    case "medium":
        reminder = f"{task} is a medium priority task"
    case "low":
        reminder = f"{task} is a low priority task "
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
else:
    reminder = f"{reminder}. Consider completing it when you have free time!"
print(f"Reminder: {reminder}")