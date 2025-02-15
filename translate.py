import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from gtts import gTTS
import pygame
import os
import uuid
from datetime import datetime

class TranslatorApp:
    def __init__(self, root):
        self.root = root
        self.translator = Translator()
        pygame.mixer.init()
        
        # Language mapping (filtered)
        self.LANGUAGE_MAP = {
            "English": "en",
            "French": "fr",
            "Arabic": "ar",
            "Italian": "it",
            "Spanish": "es",
            "Japanese": "ja",
            "Chinese": "zh-cn",
            "Korean": "ko",
            "German": "de",
        }
        
        self.setup_ui()

    def setup_ui(self):
        self.root.title("Translator")
        self.root.geometry("500x600")
        
        # Input Text
        ttk.Label(self.root, text="Enter Text:", font=("Arial", 12)).pack(pady=10)
        self.input_entry = tk.Text(self.root, height=5, width=50)  # Use tk.Text instead of ttk.Text
        self.input_entry.pack(pady=5)

        # Language Selection
        language_frame = ttk.Frame(self.root)
        language_frame.pack(pady=10)

        # Use tk.StringVar instead of ttk.StringVar
        self.source_lang_var = tk.StringVar(value="English")
        self.target_lang_var = tk.StringVar(value="French")

        ttk.Label(language_frame, text="From:").grid(row=0, column=0, padx=5)
        self.source_lang_menu = ttk.Combobox(
            language_frame, 
            textvariable=self.source_lang_var,
            values=list(self.LANGUAGE_MAP.keys())
        )
        self.source_lang_menu.grid(row=0, column=1, padx=5)

        ttk.Label(language_frame, text="To:").grid(row=0, column=2, padx=5)
        self.target_lang_menu = ttk.Combobox(
            language_frame,
            textvariable=self.target_lang_var,
            values=list(self.LANGUAGE_MAP.keys())
        )
        self.target_lang_menu.grid(row=0, column=3, padx=5)

        # Translate Button
        ttk.Button(
            self.root,
            text="Translate",
            command=self.translate_text,
            style="primary.TButton"
        ).pack(pady=10)

        # Output Text
        ttk.Label(self.root, text="Translated Text:", font=("Arial", 12)).pack(pady=10)
        self.output_text = tk.Text(self.root, height=5, width=50)  # Use tk.Text here as well
        self.output_text.pack(pady=5)

        # Play Button
        ttk.Button(
            self.root,
            text="Read Translation",
            command=self.play_translation,
            style="success.TButton"
        ).pack(pady=10)

    def translate_text(self):
        input_text = self.input_entry.get("1.0", "end").strip()
        source_lang = self.LANGUAGE_MAP[self.source_lang_var.get()]
        target_lang = self.LANGUAGE_MAP[self.target_lang_var.get()]

        if not input_text:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", "Please enter text to translate.")
            return

        try:
            translation = self.translator.translate(
                input_text,
                src=source_lang,
                dest=target_lang
            )
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translation.text)
        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", f"Translation error: {e}")

    def play_translation(self):
        translation = self.output_text.get("1.0", "end").strip()
        if not translation:
            return

        try:
            filename = f"translation_{uuid.uuid4().hex}.mp3"
            tts = gTTS(translation, lang=self.LANGUAGE_MAP[self.target_lang_var.get()])
            tts.save(filename)
            
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()

            def cleanup():
                if os.path.exists(filename):
                    os.remove(filename)

            self.root.after(100, lambda: cleanup() 
                          if not pygame.mixer.music.get_busy() else None)

        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", f"Audio error: {e}")


# Main function to run the application
def main():
    root = tk.Tk()
    app = TranslatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
