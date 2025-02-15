
import tkinter as tk
from tkinter import ttk
import subprocess
import ttkbootstrap as ttk

def launch_unit_converter():
    subprocess.Popen(["python", "unit.py"])

def launch_calculator():
    subprocess.Popen(["python", "calc.py"])

def launch_chronometer():
    subprocess.Popen(["python", "chrono.py"])

def launch_sentiment_app():
    subprocess.Popen(["python", "journal.py"])

def launch_timer():
    subprocess.Popen(["python", "timer.py"])
    
def launch_to_do_list():
    subprocess.Popen(["python", "todo_list.py"])

def launch_translate():
    subprocess.Popen(["python", "translate.py"])


# Create the main window
root = tk.Tk()
root.title("Program Launcher")
root.geometry("300x300")

# Add buttons for different programs
launch_button_calc = ttk.Button(root, text="Launch Calculator", command=launch_calculator)
launch_button_calc.pack(expand=True, padx=20, pady=5)

launch_button_chrono = ttk.Button(root, text="Launch Chronometer", command=launch_chronometer)
launch_button_chrono.pack(expand=True, padx=20, pady=5)

launch_button_sentiment = ttk.Button(root, text="Launch Sentiment App", command=launch_sentiment_app)
launch_button_sentiment.pack(expand=True, padx=20, pady=5)

launch_button_timer = ttk.Button(root, text="Launch Timer", command=launch_timer)
launch_button_timer.pack(expand=True, padx=20, pady=5)

launch_button_todolist = ttk.Button(root, text="Launch To-Do List", command=launch_to_do_list)
launch_button_todolist.pack(expand=True, padx=20, pady=5)

launch_button_unit_converter = ttk.Button(root, text="Launch Unit Converter", command=launch_unit_converter)
launch_button_unit_converter.pack(expand=True, padx=20, pady=5)

launch_button_translate = ttk.Button(root, text="Launch Translate", command=launch_translate)
launch_button_translate.pack(expand=True, padx=20, pady=5)

# Run the main event loop
root.mainloop()
