# Definisco la classe Studente
class Studente:
    def __init__(self, nome, cognome, eta, matricola, voti):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = voti

    # Metodo che stampa una presentazione dello studente
    def presentati(self):
        print(f"Ciao, mi chiamo {self.nome} {self.cognome} e ho {self.eta} anni")

    def aggiungi_voto(self, voto):
        if voto >= 18:  # Controlla se il voto è valido (>= 18)
            self.voti.append(voto)
        else:  # Se il voto non è valido, stampa un messaggio di errore
            print(f"Errore: il voto {voto} non è valido.")

    def calcola_media(self):
        media = sum(self.voti) / len(self.voti)
        print(
            f"La media di {self.nome} {self.cognome} è: {media}"
        )  # Stampa la media con
        # il nome dello studente

    def studia(self, ore):
        print(f"Oggi ho studiato per {ore} ore")


studente1 = Studente("Chiara", "Rossi", 25, 20079577, [22, 27, 25, 30])
studente2 = Studente("Luca", "Grassi", 26, 20113630, [26, 28, 29, 27])
studente1.presentati()
studente2.presentati()
studente1.aggiungi_voto(30)
studente1.voti
studente2.aggiungi_voto(29)
studente2.voti
studente1.aggiungi_voto(15)
studente1.calcola_media()
studente2.calcola_media()
studente1.studia(8)
studente2.studia(3)
