import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List App")

        self.tasks = []
        self.task_entry = tk.Entry(master, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.due_date_entry = tk.Entry(master, width=15)
        self.due_date_entry.grid(row=0, column=1, padx=10, pady=10)
        self.due_date_entry.insert(0, "Due Date (YYYY-MM-DD)")

        self.priority_entry = tk.Entry(master, width=15)
        self.priority_entry.grid(row=0, column=2, padx=10, pady=10)
        self.priority_entry.insert(0, "Priority (1-5)")

        self.add_button = tk.Button(master, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=3, padx=10, pady=10)

        self.task_listbox = tk.Listbox(master, width=60, height=15)
        self.task_listbox.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        self.display_tasks()

        self.mark_completed_button = tk.Button(master, text="Mark Completed", command=self.mark_completed)
        self.mark_completed_button.grid(row=2, column=0, padx=10, pady=10)

        self.update_task_button = tk.Button(master, text="Update Task", command=self.update_task)
        self.update_task_button.grid(row=2, column=1, padx=10, pady=10)

        self.remove_task_button = tk.Button(master, text="Remove Task", command=self.remove_task)
        self.remove_task_button.grid(row=2, column=2, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        due_date = self.due_date_entry.get()
        priority = self.priority_entry.get()

        if task and due_date and priority.isdigit():
            self.tasks.append({'task': task, 'due_date': due_date, 'priority': int(priority), 'completed': False})
            self.display_tasks()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields correctly.")

    def display_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for i, task in enumerate(self.tasks, start=1):
            status = "Completed" if task['completed'] else "Not Completed"
            self.task_listbox.insert(tk.END, f"{i}. {task['task']} - Due: {task['due_date']}, Priority: {task['priority']} - {status}")

    def mark_completed(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]['completed'] = True
            self.display_tasks()

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            new_description = simpledialog.askstring("Input", "Enter new task description:", parent=self.master)
            if new_description:
                self.tasks[index]['task'] = new_description
                self.display_tasks()

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            removed_task = self.tasks.pop(index)
            messagebox.showinfo("Removed Task", f"Task removed: {removed_task['task']}")
            self.display_tasks()

    def clear_entries(self):
        self.task_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.due_date_entry.insert(0, "Due Date (YYYY-MM-DD)")
        self.priority_entry.insert(0, "Priority (1-5)")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
