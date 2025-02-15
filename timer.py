import tkinter as tk
from time import strftime, localtime
import pygame

# Variables globales pour le timer
time_left = 0
running = False

# Initialize pygame mixer for playing audio
pygame.mixer.init()

# Load your audio file (make sure to place your audio file in the same directory or provide the path)
audio_file = "iphone_alarm.mp3"  # Replace with your actual audio file path

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Timer")
        self.root.geometry("400x300")
        self.root.configure(bg="#282c34")

        # Initialize time variables
        self.time_left = 0
        self.running = False

        # Set up the UI components
        self.setup_ui()

    def setup_ui(self):
        """Sets up the UI components for the Timer app."""
        # Affichage du titre
        title_label = tk.Label(self.root, text="Timer", font=("Arial", 24, "bold"), fg="#61afef", bg="#282c34")
        title_label.pack(pady=5)

        # Affichage de l'heure actuelle
        self.clock_label = tk.Label(self.root, font=("Arial", 14), fg="#98c379", bg="#282c34")
        self.clock_label.pack(pady=5)
        self.update_clock()

        # Zone pour écrire les minutes
        entry_frame = tk.Frame(self.root, bg="#282c34")
        entry_frame.pack(pady=20)

        tk.Label(entry_frame, text="Minutes :", font=("Arial", 14), fg="#ffffff", bg="#282c34").pack(side="left", padx=5)
        self.entry_minutes = tk.Entry(entry_frame, font=("Arial", 14), width=5, justify="center")
        self.entry_minutes.pack(side="left", padx=5)

        set_button = tk.Button(
            entry_frame,
            text="Set",
            command=self.timer_set,
            font=("Arial", 12),
            bg="#61afef",
            fg="#ffffff",
            activebackground="#528bff",
            activeforeground="#ffffff",
            relief="raised"
        )
        set_button.pack(side="left", padx=10)

        # Affichage du timer
        self.timer_label = tk.Label(self.root, text="00:00", font=("Arial", 48, "bold"), fg="#e06c75", bg="#282c34")
        self.timer_label.pack(pady=20)

        # Boutons pour démarrer et arrêter
        button_frame = tk.Frame(self.root, bg="#282c34")
        button_frame.pack(pady=10)

        start_button = tk.Button(
            button_frame,
            text="Start",
            command=self.timer_start,
            font=("Arial", 12),
            bg="#98c379",
            fg="#ffffff",
            activebackground="#6abf69",
            activeforeground="#ffffff",
            relief="raised"
        )
        start_button.grid(row=0, column=0, padx=10)

        stop_button = tk.Button(
            button_frame,
            text="Stop",
            command=self.timer_stop,
            font=("Arial", 12),
            bg="#e06c75",
            fg="#ffffff",
            activebackground="#d32f2f",
            activeforeground="#ffffff",
            relief="raised"
        )
        stop_button.grid(row=0, column=1, padx=10)

    def update_clock(self):
        """Met à jour l'affichage de l'heure exacte."""
        current_time = strftime("%H:%M:%S", localtime())
        self.clock_label.config(text=current_time)
        self.clock_label.after(1000, self.update_clock)

    def update_timer(self):
        """Met à jour l'affichage du temps restant."""
        if self.running and self.time_left > 0:
            self.time_left -= 1
            minutes = self.time_left // 60
            seconds = self.time_left % 60
            self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
            self.timer_label.after(1000, self.update_timer)
        elif self.time_left == 0:
            self.running = False
            self.timer_label.config(text="00:00")
            self.play_alarm()  # Play alarm sound when timer reaches 0

    def play_alarm(self):
        """Play an alarm sound when the timer finishes."""
        pygame.mixer.music.load(audio_file)
        pygame.mixer.music.play()

    def timer_start(self):
        """Démarre le timer."""
        if not self.running and self.time_left > 0:
            self.running = True
            self.update_timer()

    def timer_set(self):
        """Initialise le temps restant avec les minutes spécifiées."""
        self.running = False
        minutes = int(self.entry_minutes.get()) if self.entry_minutes.get().isdigit() else 0
        self.time_left = minutes * 60
        self.timer_label.config(text=f"{minutes:02}:00")

    def timer_stop(self):
        """Arrête le timer."""
        self.running = False

def main():
    app = tk.Tk()
    app_instance = TimerApp(app)
    app.mainloop()
    
if __name__ == "__main__":
    main()
