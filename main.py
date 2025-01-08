import datetime

class Task:
    def __init__(self, task_name, deadline, status="Incomplete"):
        self.task_name = task_name
        self.deadline = deadline
        self.status = status

    def mark_as_complete(self):
        self.status = "Complete"

    def __str__(self):
        return f"Task: {self.task_name}, Deadline: {self.deadline}, Status: {self.status}"

class Web3Project:
    def __init__(self, project_name):
        self.project_name = project_name
        self.tasks = []

    def add_task(self, task_name, deadline):
        task = Task(task_name, deadline)
        self.tasks.append(task)

    def get_pending_tasks(self):
        return [task for task in self.tasks if task.status == "Incomplete"]

    def get_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Complete"]

    def show_project_status(self):
        print(f"Project: {self.project_name}")
        print("Pending Tasks:")
        for task in self.get_pending_tasks():
            print(task)
        print("Completed Tasks:")
        for task in self.get_completed_tasks():
            print(task)

# Create a project
project = Web3Project("Decentralized Finance Application")

# Add tasks to the project
project.add_task("Set up Testnet Environment", datetime.date(2025, 2, 1))
project.add_task("Write Whitepaper", datetime.date(2025, 3, 15))

# Mark a task as complete
project.tasks[0].mark_as_complete()

# Display project status
project.show_project_status()
