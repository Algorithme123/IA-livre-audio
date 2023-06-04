import pyttsx3
from PyPDF2 import PdfReader

# Initialisation du moteur de synthèse vocale
alicia = pyttsx3.init()
alicia.say("Bonjour Daniel, je suis la nouvelle version de ton IA et je suis Alicia")
alicia.say("La lecture du livre va commencer. Relaxez-vous et écoutez tranquillement.")

# Ouverture du fichier PDF
livre = open('livres/ok.pdf', 'rb')
lecture = PdfReader(livre)

# Extraction du contenu de la première page du livre
pages = lecture.pages[0]
texte = pages.extract_text()

# Lecture du contenu extrait à l'aide de la synthèse vocale
alicia.say(texte)

# Message de fin de lecture
alicia.say("J'ai terminé la lecture du livre. Si vous avez d'autres tâches à effectuer ou si vous souhaitez me confier d'autres livres, je suis prêt à les prendre en charge.")

# Exécution de la synthèse vocale
alicia.runAndWait()
