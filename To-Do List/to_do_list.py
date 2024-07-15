import tkinter as tk
from tkinter import messagebox
import time

#Create the Main Window
root = tk.Tk()
root.title("TO-DO APP")

todo_list = []

def addTask():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:  
        messagebox.showwarning("Input Error", "Please enter a task.")


def viewTask():
    task_listbox.delete(0, tk.END)
    for task in todo_list:
        task_listbox.insert(tk.END, task)

def removeTask(taskNumber):
    try:
        selected_task_index = task_listbox.curseselection()[0]
        task_listbox.delete(selected_task_index)
        del todo_list[selected_task_index]
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")
       

#Create & place widgets
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_button = tk.Button(root, text = "Add Task", command=addTask)
add_button.pack(pady=5)

view_button = tk.Button(root, text = "View Task", command=viewTask)
view_button.pack(pady=5)

remove_button = tk.Button(root, text = "Remove Task", command = removeTask)
remove_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height = 10)
task_listbox.pack(pady=10)

#Start the main event loop
root.mainloop()
