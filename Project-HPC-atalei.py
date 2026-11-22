# This library is necessary to get input from a text file.
# Note that this is intended for use on the clusters - the
# regular python library is simply "ast"
from asteval import Interpreter
aeval = Interpreter()

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']


# Insert your weekly report function
# Ensure the function takes 3 pieces of input - the task dictionary,
# habit dictionary, and file name to read the data.

def weekly_report(habits, tasks, file_name):
    print(f"\n===== Weekly Report for {file_name} =====")

    print("\nHabits:")
    if not habits:
        print("There are no habits being tracked.")
    else:
        for habit_name, habit_days in habits.items():
            count = sum(1 for done in habit_days.values() if done)
            print(f"  {habit_name}: {count}/7 days complete")

    print("\nTasks:")
    completed = []
    not_completed = []
    for day, day_tasks in tasks.items():
        for task_name, done in day_tasks.items():
            if done:
                completed.append(f"{task_name} ({day})")
            else:
                not_completed.append(f"{task_name} ({day})")

    if not completed and not not_completed:
        print("There are no tasks.")
    else:
        print("  Completed:")
        if not completed:
            print("    None")
        for item in completed:
            print(f"    {item}")
        print("  Not completed:")
        if not not_completed:
            print("    None")
        for item in not_completed:
            print(f"    {item}")


# Provide the list of files to process.
# The dictionaries.txt files each contain a list of
# two dictionaries, the first being for habits and
# the second for tasks. 
#
# Note that the files and this python script should be in the
# same directory when you run it.
file_list = [
    "dictionaries_1.txt",
    "dictionaries_2.txt",
    "dictionaries_3.txt",
    "dictionaries_4.txt",
    "dictionaries_5.txt",
    "dictionaries_6.txt",
    "dictionaries_7.txt",
    "dictionaries_8.txt",
    "dictionaries_9.txt",
    "dictionaries_10.txt",
]

# This section will loop through the files in the list above, and 
# run the weekly_report() function for each file. 
#
# The use of the ast library allows you to read text files
# that contain Python structures, in this case a list of dictionaries
#
# This code loops through each file, assigns the list of dictionaries
# as the variable 'data', then gives the weekly_report() function
# the appropriate input.
#
# Ensure you edit the final line so it matches your function name,
# and supply the appropriate input.
for file_name in file_list:
    with open(file_name) as f:
        content = f.read()
        data = aeval(content)
        weekly_report(data[0], data[1], file_name)