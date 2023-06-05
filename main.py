import pyttsx3
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader


class LecteurLivre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("IA: Lecteur de Livres")
        self.configure(bg="lightblue")

        # variable permettant de stocker le chemin du livre
        self.choix_du_livre = tk.StringVar()

        self.label = tk.Label(self, text="Sélectionnez un livre au format PDF")
        self.label.pack(pady=10)
        self.label.config(fg="black", font=("Arial", 20, "bold"))

        self.btn_choix = tk.Button(self, text="Parcourir", command=self.livre_choisie)
        self.btn_choix.pack(pady=5)

        self.btn_lecture = tk.Button(self, text="Commencer la lecture", command=self.lecture_du_livre, state=tk.DISABLED)
        self.btn_lecture.pack(pady=5)

        self.alicia = pyttsx3.init()

    def livre_choisie(self):
        chemin_livre = filedialog.askopenfilename(filetypes=[("Fichiers PDF", "*.pdf")])
        self.choix_du_livre.set(chemin_livre)

        if chemin_livre:
            self.btn_lecture.config(state=tk.NORMAL)

    def lecture_du_livre(self):
        chemin_livre = self.choix_du_livre.get()

        if chemin_livre:
            try:
                livre = open(chemin_livre, 'rb')
                lecture = PdfReader(livre)
                text = ""
                for page in lecture.pages:
                    text += page.extract_text()

                self.alicia.say(text)
                self.alicia.runAndWait()

                self.label.config(text="J'ai terminé la lecture du livre. Si vous avez d'autres tâches à effectuer ou si vous souhaitez me confier d'autres livres, je suis prêt à les prendre en charge.")
                self.btn_lecture.config(state=tk.DISABLED)

            except Exception as e:
                self.label.config(text="Une erreur s'est produite lors de la lecture du livre.")
                print(e)

if __name__ == "__main__":
    application = LecteurLivre()
    application.mainloop()

