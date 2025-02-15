import tkinter as tk
from tkinter import Toplevel, messagebox
from datetime import datetime  # Import the datetime module

# Nom du fichier pour stocker les informations
FICHIER = "expressions.txt"

class SentimentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do App avec Émojis")
        self.root.geometry("400x400")  # Taille de la fenêtre principale

        # Cadre pour les émojis
        self.frame_emoji = tk.Frame(self.root)
        self.frame_emoji.pack(pady=20)

        # Création des boutons pour les émotions
        self.create_emoji_buttons()

        # Bouton pour ouvrir la zone d'expression
        self.btn_ouvrir_fenetre = tk.Button(self.root, text="Ouvrir zone d'expression", font=("Arial", 14), bg="green", fg="white", command=self.ouvrir_fenetre_expression)
        self.btn_ouvrir_fenetre.pack(pady=10)

        # Bouton pour afficher les expressions enregistrées
        self.btn_afficher_expressions = tk.Button(self.root, text="Voir les expressions", font=("Arial", 14), bg="blue", fg="white", command=self.afficher_expressions)
        self.btn_afficher_expressions.pack(pady=10)

        # Message affiché
        self.label_message = tk.Label(self.root, text="", font=("Arial", 12), fg="blue")
        self.label_message.pack(pady=10)

    def create_emoji_buttons(self):
        """Create buttons for different emojis and assign actions."""
        emojis = [
            ("😡", "Exprime ta colère !", "red"),
            ("😐", "Reste calme...", "yellow"),
            ("😊", "C'est une belle journée !", "pink")
        ]
        
        for idx, (emoji, message, color) in enumerate(emojis):
            btn = tk.Button(self.frame_emoji, text=emoji, font=("Arial", 20), bg=color, fg="white", command=lambda msg=message: self.update_label(msg))
            btn.grid(row=0, column=idx, padx=10)

    def update_label(self, message):
        """Update the message label with the chosen emoji's message."""
        self.label_message.config(text=message)

    def ajouter_emoji(self, zone_texte, emoji):
        """Ajoute un emoji à la zone de texte au curseur actuel."""
        zone_texte.insert(tk.END, emoji)

    def enregistrer_texte(self, zone_texte, fenetre_actuelle):
        """Enregistre le contenu de la zone de texte dans le fichier avec un horodatage."""
        contenu = zone_texte.get("1.0", tk.END).strip()  # Récupère le texte
        if contenu:
            # Obtenir l'horodatage actuel
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Ouvrir le fichier en mode ajout
            with open(FICHIER, "a", encoding="utf-8") as fichier:
                fichier.write(f"Date et Heure: {timestamp}\n")  # Ajouter l'horodatage
                fichier.write(contenu + "\n---------------\n")  # Ajouter l'expression et un séparateur

            # Afficher une boîte de dialogue de confirmation
            messagebox.showinfo("Succès", "L'expression a été enregistrée avec succès!")

        # Fermer la fenêtre actuelle après l'enregistrement
        fenetre_actuelle.destroy()

    def ouvrir_fenetre_expression(self):
        """Ouvre une nouvelle fenêtre avec une zone de texte vide pour écrire."""
        fenetre_expression = Toplevel(self.root)
        fenetre_expression.title("Exprime tes sentiments")
        fenetre_expression.geometry("400x400")  # Taille de la fenêtre

        # Label d'instruction
        label_instruction = tk.Label(fenetre_expression, text="Écris ici ce que tu ressens :", font=("Arial", 12))
        label_instruction.pack(pady=10)

        # Zone de texte pour écrire
        zone_texte = tk.Text(fenetre_expression, width=40, height=10, font=("Arial", 12))
        zone_texte.pack(pady=10)

        # Frame pour les émojis
        frame_emoji = tk.Frame(fenetre_expression)
        frame_emoji.pack(pady=10)

        # Emojis à afficher
        emojis = ["😡", "😐", "😊", "😂", "😍", "😎"]

        # Créer des boutons pour chaque emoji
        for emoji in emojis:
            btn_emoji = tk.Button(frame_emoji, text=emoji, font=("Arial", 20), command=lambda e=emoji: self.ajouter_emoji(zone_texte, e))
            btn_emoji.pack(side=tk.LEFT, padx=5)

        # Bouton pour enregistrer et fermer la fenêtre
        btn_enregistrer = tk.Button(fenetre_expression, text="Enregistrer", bg="green", fg="white", 
                                    command=lambda: self.enregistrer_texte(zone_texte, fenetre_expression))
        btn_enregistrer.pack(pady=5)

        # Bouton pour fermer la fenêtre sans enregistrer
        btn_fermer = tk.Button(fenetre_expression, text="Fermer", command=fenetre_expression.destroy, bg="lightblue")
        btn_fermer.pack(pady=5)

    def afficher_expressions(self):
        """Affiche les expressions sauvegardées dans une nouvelle fenêtre."""
        fenetre_affichage = Toplevel(self.root)
        fenetre_affichage.title("Expressions enregistrées")
        fenetre_affichage.geometry("400x300")  # Taille de la fenêtre

        # Lire le contenu du fichier
        try:
            with open(FICHIER, "r", encoding="utf-8") as fichier:
                contenu = fichier.read()
                if contenu:
                    # Afficher le contenu du fichier dans une zone de texte en lecture seule
                    zone_affichage = tk.Text(fenetre_affichage, width=50, height=15, font=("Arial", 12))
                    zone_affichage.insert(tk.END, contenu)
                    zone_affichage.config(state=tk.DISABLED)  # Rendre la zone de texte non modifiable
                    zone_affichage.pack(pady=10)
                else:
                    tk.Label(fenetre_affichage, text="Aucune expression enregistrée.", font=("Arial", 12)).pack(pady=10)
        except FileNotFoundError:
            tk.Label(fenetre_affichage, text="Aucun fichier trouvé. Aucune expression enregistrée.", font=("Arial", 12)).pack(pady=10)


def main():
    # Crée la fenêtre principale et lance l'application
    root = tk.Tk()
    app = SentimentApp(root)
    root.mainloop()
    
main()
