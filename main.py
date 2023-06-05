import pyttsx3
import tkinter as tk
from tkinter import filedialog
from PyPDF2 import PdfReader
import threading


class LecteurLivre(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("IA: Lecteur de Livres")
        self.configure(bg="lightblue")

        self.all_pages_marquee = []
        #progression de la lecture
        self.page_actuelle=0

        # variable permettant de stocker le chemin du livre
        self.choix_du_livre = tk.StringVar()

        self.label = tk.Label(self, text="Sélectionnez un livre au format PDF")
        self.label.pack(pady=10)
        self.label.config(fg="black", font=("Arial", 20, "bold"))




        self.btn_choix = tk.Button(self, text="Parcourir", command=self.livre_choisie, relief=tk.RAISED, fg="black", font=("Arial", 12), width=10, height=2, borderwidth=2)
        self.btn_choix.pack(pady=5)

        self.btn_lecture = tk.Button(self, text="Commencer la lecture", command=self.lecture_du_livre, state=tk.DISABLED, relief=tk.RAISED, fg="black", font=("Arial", 12), width=17, height=3, borderwidth=2)
        self.btn_lecture.pack(pady=5)

        self.btn_marquer_page= tk.Button(self, text="Marquer la page", command=self.marquer_page_thread)
        self.btn_marquer_page.pack(pady=5)

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
                    self.update_idletasks()

                self.alicia.say(text)
                self.alicia.runAndWait()

                self.page_actuelle = len(lecture.pages)

                self.label.config(text="J'ai terminé la lecture du livre. Si vous avez d'autres tâches à effectuer ou si vous souhaitez me confier d'autres livres, je suis prêt à les prendre en charge.")
                self.btn_lecture.config(state=tk.DISABLED)

            except Exception as e:
                self.label.config(text="Une erreur s'est produite lors de la lecture du livre.")
                print(e)

    def marquer_page(self):
        page_marques = self.page_actuelle + 1
        self.all_pages_marquee.append(page_marques)
        print("Page Marquée : ", page_marques)

    def marquer_page_thread(self):
        threading.Thread(target=self.marquer_page).start()

    def reprendre_la_lecture(self):
        if(self.all_pages_marquee):
            derniere_page_marque = self.all_pages_marquee[-1]
            self.page_actuelle = derniere_page_marque -1
            self.lecture_du_livre()
        else:
            print("Aucune page marquee")

if __name__ == "__main__":
    application = LecteurLivre()
    application.mainloop()

