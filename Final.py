import datetime
import matplotlib.pyplot as plt
from plyer import notification  # For desktop notifications

# Class Task
class Task:
    def __init__(self, task_id, name, task_type, start_time, end_time, priority, deadline):
        self.task_id = task_id
        self.name = name
        self.task_type = task_type  # "personal" or "academic"
        self.start_time = start_time
        self.end_time = end_time
        self.priority = priority
        self.deadline = deadline

# Sorting implementation
def merge_sort(tasks, key):
    if len(tasks) > 1:
        mid = len(tasks) // 2
        left_half = tasks[:mid]
        right_half = tasks[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if getattr(left_half[i], key) <= getattr(right_half[j], key):
                tasks[k] = left_half[i]
                i += 1
            else:
                tasks[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            tasks[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            tasks[k] = right_half[j]
            j += 1
            k += 1

# Visualization
def plot_gantt_chart(tasks):
    fig, ax = plt.subplots()
    for i, task in enumerate(tasks):
        color = 'tab:blue' if task.task_type == "academic" else 'tab:green'
        ax.broken_barh([(task.start_time, task.end_time - task.start_time)],(i - 0.4, 0.8), facecolors=color)
    ax.set_yticks(range(len(tasks)))
    ax.set_yticklabels([task.name for task in tasks])
    ax.set_xlabel('Time (Hours)')
    ax.set_title('Task Schedule')
    plt.show()

# Notifications
# def notify(title, message):
#     notification.notify(
#         title=title,
#         message=message,
#         app_name="Task Scheduler",
#         timeout=10
#     )
import subprocess

def notify(title, message):
    try:
        subprocess.run([
            "osascript", "-e",
            f'display notification "{message}" with title "{title}"'
        ])
    except Exception as e:
        print(f"Notification Error: {e}")


# Reminder system
def check_notifications(tasks):
    current_time = datetime.datetime.now().time()  # Get the current time
    
    for task in tasks:
        task_start = datetime.time(hour=task.start_time)  # Convert start time to datetime.time
        task_end = datetime.time(hour=task.end_time)      # Convert end time to datetime.time
        
        # Check for upcoming tasks (within 1 hour)
        if task_start > current_time and (datetime.datetime.combine(datetime.date.today(), task_start) - datetime.datetime.now()).seconds <= 3600:
            print(f"Reminder: Upcoming task '{task.name}' starting at {task.start_time}:00.")
            notify("Upcoming Task", f"Task '{task.name}' starts at {task.start_time}:00.")

        # Check for missed tasks
        elif task_end < current_time:
            print(f"Missed Task: You missed '{task.name}', which ended at {task.end_time}:00.")
            notify("Missed Task", f"Task '{task.name}' ended at {task.end_time}:00.")

# Main function
def main():
    print("Welcome to the Task Scheduler!")
    print("Enter tasks to create a Gantt chart and receive reminders.")
    
    tasks = []
    task_id = 1

    while True:
        print(f"\nEnter details for Task {task_id}:")
        name = input("Task Name: ")
        task_type = input("Task Type (personal/academic): ").lower()
        start_time = int(input("Start Time (e.g., 1 for 1:00): "))
        end_time = int(input("End Time (e.g., 5 for 5:00): "))
        priority = int(input("Priority (e.g., 10): "))
        deadline = int(input("Deadline (e.g., 5 for day 5): "))

        # Add task to the list
        tasks.append(Task(task_id, name, task_type, start_time, end_time, priority, deadline))
        task_id += 1

        another = input("Do you want to add another task? (yes/no): ").lower()
        if another != "yes":
            break

    # Sorting tasks by start time for better visualization
    merge_sort(tasks, "start_time")

    print("\nChecking for reminders and missed tasks...")
    check_notifications(tasks)  # Check reminders and missed tasks

    print("\nGenerating Gantt Chart...")
    plot_gantt_chart(tasks)

# Run the program
if __name__ == "__main__":
    main()
