import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("600x400")  # Set initial window size

        self.task_list = []
        self.setup_ui()
        self.load_tasks()

    def setup_ui(self):
        # Input field and Add button
        self.task_entry = ttk.Entry(self.root, width=40)
        self.task_entry.pack(pady=10)

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # Task display area
        self.task_frame = ttk.Frame(self.root)
        self.task_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Load the task list
        self.refresh_task_list()

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.task_list.append([task, "undone"])
            self.task_entry.delete(0, tk.END)
            self.refresh_task_list()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def toggle_task_status(self, index):
        task = self.task_list[index]
        task[1] = "done" if task[1] == "undone" else "undone"
        self.refresh_task_list()

    def delete_task(self, index):
        del self.task_list[index]
        self.refresh_task_list()

    def refresh_task_list(self):
        # Clear the current listbox
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Rebuild the task list
        for index, task in enumerate(self.task_list):
            task_text = task[0]
            status = "✓" if task[1] == "done" else "✗"
            
            # Create a frame for each task
            task_item_frame = ttk.Frame(self.task_frame)
            task_item_frame.pack(fill="x", padx=10, pady=5)

            # Label for the task
            task_label = ttk.Label(task_item_frame, text=f"{status} {task_text}", anchor="w", width=50)
            task_label.pack(side="left", fill="x")

            # Mark/Unmark button
            mark_button = ttk.Button(task_item_frame, text="Mark Done/Undone", command=lambda idx=index: self.toggle_task_status(idx))
            mark_button.pack(side="left", padx=5)

            # Delete button
            delete_button = ttk.Button(task_item_frame, text="Delete", command=lambda idx=index: self.delete_task(idx))
            delete_button.pack(side="right", padx=5)

        # Save tasks to file after refreshing
        self.save_tasks()

    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.task_list:
                file.write(f"{task[0]}|{task[1]}\n")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                for line in file:
                    task, status = line.strip().split("|")
                    self.task_list.append([task, status])
        except FileNotFoundError:
            pass

def main():
    root = ttk.Window(themename="superhero")
    app_instance = ToDoListApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
