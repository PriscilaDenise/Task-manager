# Task Manager Project

## Course Unit: Design and Analysis of Algorithms

### Group Members:
- **Muwanguzi Priscila Denise** - M23B23/010  
- **Mawejje JohnPaul** - M23B23/049  
- **Nicole Johnson** - S23B23/020  

---

## Overview
This project is a Python-based **Personal Scheduling Assistant** designed to help users manage tasks efficiently. It allows users to:
1. Input tasks.
2. Sort them by start time using the **Merge Sort Algorithm**.
3. Visualize schedules via a **Gantt Chart**.
4. Receive notifications for upcoming and missed tasks.

The system improves time management and productivity by providing clear task organization and timely alerts.

---

## Features

### 1. **Task Management**
Each task is represented by a `Task` class, which includes:
- **Attributes**:
  - `task_id`: A unique identifier for the task.
  - `name`: Task name or description.
  - `task_type`: Task category (e.g., personal, academic).
  - `start_time`: Task start time.
  - `end_time`: Task end time.
  - `priority`: Task priority level.
  - `deadline`: Task deadline.
- **Purpose**: Encapsulates all details related to a single task.

---

### 2. **Merge Sort Algorithm**
Tasks are sorted by their start times to ensure a clear, chronological schedule.

#### **Pseudocode**  
```plaintext
MERGE-SORT(array):
  if array.length <= 1:
    return
  mid = array.length / 2
  left_half = array[:mid]
  right_half = array[mid:]
  MERGE-SORT(left_half)
  MERGE-SORT(right_half)
  MERGE(left_half, right_half, array)

MERGE(left, right, array):
  i = j = k = 0
  while i < left.length and j < right.length:
    if left[i] <= right[j]:
      array[k] = left[i]
      i += 1
    else:
      array[k] = right[j]
      j += 1
    k += 1
  while i < left.length:
    array[k] = left[i]
    i += 1
    k += 1
  while j < right.length:
    array[k] = right[j]
    j += 1
    k += 1
```

#### **Why Merge Sort?**
- Efficient for large datasets: **O(n log n)** time complexity.
- Stable sorting ensures tasks retain their order when start times match.

---

### 3. **Gantt Chart Visualization**
A **Gantt Chart** provides a clear, color-coded overview of task schedules. It highlights task durations and overlaps.

#### **Pseudocode**  
```plaintext
FUNCTION plot_gantt_chart(tasks):
    INITIALIZE plot using matplotlib
    FOR each task IN tasks:
        DETERMINE color BASED ON task_type (e.g., "academic" is blue, "personal" is green)
        ADD task as a bar to the chart using task.start_time, task.end_time
    LABEL axes AND tasks
    DISPLAY the chart
```

#### **Library Used**:
- **`matplotlib.pyplot`**: Creates detailed and customizable charts.

---

### 4. **Notification System**
Users are alerted to upcoming and missed tasks through a notification system. The application supports **cross-platform notifications**.

#### **Notify Function**  
```plaintext
FUNCTION notify(title, message):
    TRY:
        RUN osascript command TO DISPLAY notification WITH title AND message
    CATCH Exception AS e:
        PRINT error message
```

#### **Check Notifications Function**  
```plaintext
FUNCTION check_notifications(tasks):
  FOR EACH task IN tasks:
    IF task is about to start:
      PRINT "Upcoming Task: " + task.name
      NOTIFY("Upcoming Task", task.name)
    IF task has been missed:
      PRINT "Missed Task: " + task.name
      NOTIFY("Missed Task", task.name)
```

#### **Libraries Used**:
- **`subprocess`**: Executes system commands (e.g., macOS `osascript` for notifications).
- **`plyer`**: Ensures compatibility across platforms (e.g., Windows, Linux).

---

## Program Flow

### **Main Function**
The entry point of the program, performing the following steps:
1. **User Input**: Prompt the user for task details (name, type, start time, end time, priority, deadline).
2. **Task Creation**: Create a `Task` object and add it to the task list.
3. **Task Sorting**: Sort tasks using the `merge_sort` algorithm.
4. **Notifications**: Check and notify users about upcoming and missed tasks.
5. **Gantt Chart**: Generate and display the Gantt chart.

#### **Pseudocode**  
```plaintext
FUNCTION main():
    PRINT welcome message
    INITIALIZE empty tasks list
    SET task_id TO 1

    LOOP UNTIL user opts to stop adding tasks:
        GET task details (name, type, start_time, end_time, priority, deadline) FROM user
        CREATE Task OBJECT WITH entered details
        APPEND task TO tasks list
        INCREMENT task_id
        ASK user if they want to add another task

    CALL merge_sort TO SORT tasks BY start_time
    CALL check_notifications TO IDENTIFY and alert for upcoming or missed tasks
    CALL plot_gantt_chart TO DISPLAY the Gantt chart
```

#### **Execution Block**  
```python
if __name__ == "__main__":
    main()
```

---

## Design Decisions
- **Task Class**: Encapsulates task-related data, making future extensions easier.
- **Merge Sort**: Optimal for task sorting due to its performance on large datasets.
- **Gantt Chart**: Provides clarity in visualizing schedules.
- **Dynamic Input Loop**: Enables flexibility by allowing users to define tasks iteratively.
- **Cross-Platform Notifications**: Improves user experience by ensuring timely alerts.

---

## Libraries Used
- **`datetime`**: Handles time and date logic.
- **`matplotlib.pyplot`**: Visualizes schedules with Gantt charts.
- **`subprocess`**: Executes system-level commands for native notifications.
- **`plyer`**: Supports notifications across multiple platforms.

---

## Execution
To run the program:
1. Ensure Python 3.x is installed.
2. Install required libraries:
   ```bash
   pip install matplotlib plyer
   ```
3. Execute the script:
   ```bash
   python task_manager.py
   ```

Enjoy managing your time effectively! 😊
