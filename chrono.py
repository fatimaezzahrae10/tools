import tkinter as tk
from tkinter import ttk
import time

class ChronometerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Chronometer with Laps")
        self.root.geometry("300x400")

        self.running = False
        self.start_time = None
        self.elapsed_time = 0
        self.lap_times = []

        # Display
        self.time_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36))
        self.time_label.pack(pady=20)

        # Buttons
        self.start_stop_button = ttk.Button(root, text="Start", command=self.toggle)
        self.start_stop_button.pack(pady=10)

        self.lap_button = ttk.Button(root, text="Lap", command=self.record_lap, state=tk.DISABLED)
        self.lap_button.pack(pady=10)

        self.reset_button = ttk.Button(root, text="Reset", command=self.reset, state=tk.DISABLED)
        self.reset_button.pack(pady=10)

        # Lap display
        self.lap_listbox = tk.Listbox(root, height=10, width=40)
        self.lap_listbox.pack(pady=10)

        # Update loop
        self.update_time()

    def toggle(self):
        if not self.running:
            self.running = True
            self.start_stop_button.config(text="Stop")
            self.lap_button.config(state=tk.NORMAL)
            self.reset_button.config(state=tk.NORMAL)
            self.start_time = time.time() - self.elapsed_time
        else:
            self.running = False
            self.start_stop_button.config(text="Start")

    def record_lap(self):
        if self.running:
            elapsed = self.elapsed_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            millis = int((elapsed - int(elapsed)) * 100)
            lap_time = f"{minutes:02}:{seconds:02}:{millis:02}"
            self.lap_times.append(lap_time)
            self.lap_listbox.insert(tk.END, f"Lap {len(self.lap_times)}: {lap_time}")

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.lap_times = []
        self.time_label.config(text="00:00:00")
        self.lap_listbox.delete(0, tk.END)
        self.start_stop_button.config(text="Start")
        self.lap_button.config(state=tk.DISABLED)
        self.reset_button.config(state=tk.DISABLED)

    def update_time(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            minutes = int(self.elapsed_time // 60)
            seconds = int(self.elapsed_time % 60)
            millis = int((self.elapsed_time - int(self.elapsed_time)) * 100)
            self.time_label.config(text=f"{minutes:02}:{seconds:02}:{millis:02}")

        self.root.after(10, self.update_time)

# Run the app
def main():
    root = tk.Tk()
    app = ChronometerApp(root)
    root.mainloop()
    
if __name__ == "__main__":
    main()
